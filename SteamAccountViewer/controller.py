from PyQt5.QtWidgets import *
from view import *
from steam.webapi import WebAPI
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from steam.steamid import SteamID
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


class Controller(QMainWindow, Ui_MainWindow):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submit_pushButton.clicked.connect(lambda: self.on_submit_press())
        self.page_pushButton.clicked.connect(lambda: self.next_page())
        self.manager = QNetworkAccessManager()
        self.api = WebAPI(key=os.getenv("API_KEY"))

    def on_submit_press(self):

        steam_id_input = self.steamid_lineEdit.text().strip().lower()
        steam_id = self.convert_to_steamid64(steam_id_input)

        try:
            persona_name, profile_picture_url = self.get_name_and_picture(steam_id)
            self.persona_name_label.setText(persona_name)
            self.display_profile_picture(profile_picture_url)
            if self.check_if_public(steam_id):
                recent_games = self.get_recent_games(steam_id)
                self.display_recent_games(recent_games)
                self.get_level(steam_id)
                self.get_creation_date(steam_id)
                self.get_friend_count(steam_id)
            else:
                self.main_stackedWidget.setCurrentIndex(1)
                self.info_stackedWidget.setCurrentIndex(1)
                self.page_pushButton.hide()
            self.main_stackedWidget.setCurrentIndex(1)
        except Exception as e:
            print("Try again: ", e)

    def check_if_public(self, steam_id):
        response = self.api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id)
        community_visibility_state = response["response"]["players"][0]["communityvisibilitystate"]

        if community_visibility_state == 1:
            return False
        elif community_visibility_state == 3:
            return True

    def next_page(self):

        # Get the current index and total number of pages in the QStackedWidget
        current_index = self.info_stackedWidget.currentIndex()
        total_pages = self.info_stackedWidget.count()

        # Increment the index and wrap around if necessary
        next_index = (current_index + 1) % total_pages

        # Set the new index for the QStackedWidget

        # Skip page 1 because that is the private profile page
        if next_index != 1:
            self.info_stackedWidget.setCurrentIndex(next_index)
        else:
            self.info_stackedWidget.setCurrentIndex(next_index + 1)

    def convert_to_steamid64(self, steam_id):
        steam_id = SteamID.from_url(steam_id)
        steam_id = steam_id.as_64
        return steam_id

    def display_recent_games(self, recent_games):
        padded_list = recent_games + [''] * (3 - len(recent_games))

        self.recent_game_1_label.setText(padded_list[0])
        self.recent_game_2_label.setText(padded_list[1])
        self.recent_game_3_label.setText(padded_list[2])

    def get_name_and_picture(self, steam_id):
        try:
            response = self.api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id)
            persona_name = response["response"]["players"][0]["personaname"]
            profile_picture_url = response["response"]["players"][0]["avatarfull"]
            return persona_name, profile_picture_url

        except Exception as e:
            print("Try again: ", e)
            raise e

    def get_recent_games(self, steam_id):
        try:
            game_count = 3
            response = self.api.call('IPlayerService.GetRecentlyPlayedGames', steamid=steam_id,
                                     count=game_count)
            recent_games = []
            for game in response['response']['games']:
                recent_games.append(game['name'])

            return recent_games
        except Exception as e:
            print("Try again: ", e)
            raise e

    def get_level(self, steam_id):
        response = self.api.call('IPlayerService.GetSteamLevel', steamid=steam_id)
        account_level = response['response']['player_level']
        self.account_level_label.setText(f'Account level: {account_level}')

    def get_friend_count(self, steam_id):
        response = self.api.call('ISteamUser.GetFriendList', steamid=steam_id)
        friend_count = len(response['friendslist']['friends'])
        self.friend_count_label.setText(f'Friend count: {friend_count}')

    def get_creation_date(self, steam_id):
        response = self.api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id)
        creation_time = response['response']['players'][0]['timecreated']
        creation_date = datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        self.creation_date_label.setText(f'Member since: {creation_date}')

    def display_profile_picture(self, profile_picture_url):
        def handle_image_download(reply):
            if reply.error() == QNetworkReply.NoError:
                data = reply.readAll()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.profile_picture_label.setPixmap(pixmap)
                self.profile_picture_label.setAlignment(Qt.AlignCenter)
                self.profile_picture_label.setScaledContents(True)
            else:
                print("Error: ", reply.errorString())

        url = QUrl(profile_picture_url)
        request = QNetworkRequest(url)
        reply = self.manager.get(request)
        reply.finished.connect(lambda: handle_image_download(reply))
