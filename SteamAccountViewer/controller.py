from PyQt5.QtWidgets import *
from view import *
from steam.webapi import WebAPI
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from dotenv import load_dotenv
import os
from datetime import datetime
import requests
from steam.steamid import SteamID

load_dotenv()

def convert_to_steamid64(steam_id):
    """
            Convert a Steam ID to its 64-bit format.

            Args:
                steam_id (str): The Steam ID to convert.

            Returns:
                int: The 64-bit representation of the Steam ID.
            """

    steam_id = SteamID.from_url(steam_id)
    steam_id = steam_id.as_64
    return steam_id

class Controller(QMainWindow, Ui_MainWindow):
    """Controller class responsible for handling user interactions and managing application logic."""
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

    def __init__(self, *args, **kwargs):
        """
        Initialize the Controller instance and set up the user interface.

        Connects signals from UI elements to appropriate slots and sets focus on the steamid_lineEdit input field.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submit_pushButton.clicked.connect(lambda: self.on_submit_press())
        self.page_pushButton.clicked.connect(lambda: self.next_page())
        self.view_another_pushButton.clicked.connect(lambda: self.on_view_another_press())
        self.manager = QNetworkAccessManager()
        self.api = WebAPI(key=os.getenv("API_KEY"))
        self.steamid_lineEdit.setFocus()

    def on_submit_press(self):
        """
        Handle the submit button press event.

        Retrieves and processes user input, updates UI elements with relevant data, and handles errors.
        """

        steam_id_input = self.steamid_lineEdit.text().strip().lower()
        steam_id = str(convert_to_steamid64(steam_id_input))

        try:
            persona_name, profile_picture_url = self.get_name_and_picture(steam_id)
            self.persona_name_label.setText(persona_name)
            self.display_profile_picture(profile_picture_url)
            self.get_ban_status(steam_id)
            if self.check_if_public(steam_id):
                self.get_recent_games(steam_id)
                self.get_level(steam_id)
                self.get_creation_date(steam_id)
                self.get_friend_count(steam_id)
                self.main_stackedWidget.setCurrentIndex(1)
                self.info_stackedWidget.setCurrentIndex(0)
            else:
                self.get_ban_status(steam_id)
                self.info_stackedWidget.setCurrentIndex(1)
                self.page_pushButton.hide()
                self.main_stackedWidget.setCurrentIndex(1)
        except Exception as e:
            print("Try again: ", e)

    def on_view_another_press(self):
        """
        Handle the view_another button press event.

        Resets UI elements to their default state, allowing the user to view another Steam profile.
        """

        self.main_stackedWidget.setCurrentIndex(0)
        self.steamid_lineEdit.setText('')
        self.steamid_lineEdit.setFocus()
        self.reset_to_default_values()

    def reset_to_default_values(self):
        """
               Reset the UI elements to their default values.

               This method is used to clear the displayed user information and reset the labels to their initial state.
               """

        self.vac_ban_label.setText('VAC Ban: None')
        self.community_ban_label.setText('Community Ban: None')
        self.game_ban_label.setText('Game Bans: None')
        self.economy_ban_label.setText('Trade Ban: None')
        self.days_since_ban_label.setText('Days since last ban: None on record.')

        self.creation_date_label.setText('Member since: Not available')
        self.friend_count_label.setText('Friend count: Not available')
        self.account_level_label.setText('Account level: Not available')

        self.recent_game_1_label.setText("No recent games found!")
        self.recent_game_2_label.setText('')
        self.recent_game_3_label.setText('')

    def check_if_public(self, steam_id: str) -> bool:
        """
              Check if the Steam profile is public.

              Args:
                  steam_id (str): The Steam ID of the user.

              Returns:
                  bool: True if the profile is public, False if private, None if error is raised.

              Raises:
                Exception: If the API request fails or the Steam ID is invalid.
            """

        try:
            response = self.api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id)
            community_visibility_state = response["response"]["players"][0]["communityvisibilitystate"]

            if community_visibility_state in [1, 2]:
                return False
            elif community_visibility_state == 3:
                return True


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:
            print(f"An error occurred during the API request: {e}")
            return None

    def next_page(self):
        """
               Navigate to the next page in the info_stackedWidget.

               This method increments the current index of the info_stackedWidget, wrapping around if necessary,
               and skips the private profile page (page 1).
               """

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


    def get_name_and_picture(self, steam_id: str) -> tuple[str, str]:
        """
            Retrieve and return the user's persona name and profile picture URL from Steam.

            This function uses the Steam API to fetch the user's persona name and profile
            picture URL using their Steam ID. It returns the name and URL as a tuple.
            If the API request fails or the Steam ID is invalid, an exception will be raised.

            Args:
                steam_id (str): The Steam ID of the user.

            Returns:
                tuple: A tuple containing the user's persona name (str) and profile picture URL (str).

            Raises:
                Exception: If the API request fails or the Steam ID is invalid.
            """

        try:
            response = self.api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id)
            persona_name = response["response"]["players"][0]["personaname"]
            profile_picture_url = response["response"]["players"][0]["avatarfull"]
            return persona_name, profile_picture_url


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:
            print(f"An error occurred during the API request: {e}")

    def get_ban_status(self, steam_id):
        """
        Retrieve and display the ban status of a Steam user.

        This function uses the Steam API to fetch ban information for a user based on their
        Steam ID. The ban information is then passed to the display_bans method to update
        the user interface with the ban status.

        Args:
            steam_id (str): The Steam ID of the user.

        Returns:
            None

        Raises:
            Exception: If the API request fails or the Steam ID is invalid.
        """

        try:
            response = self.api.call('ISteamUser.GetPlayerBans', steamids=steam_id)
            player_ban_info = response['players'][0]
            self.display_bans(player_ban_info)


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:
            print(f"An error occurred during the API request: {e}")

    def display_bans(self, player_ban_info: dict):
        """
        Update the user interface with the ban information of a Steam user.

        This function takes ban information from the Steam API and updates the user interface
        with the user's ban status, including community, trade, VAC, game bans, and days since
        the last ban.

        Args:
            player_ban_info (dict): A dictionary containing the ban information for the user.

        Returns:
            None
        """

        flag = False
        if player_ban_info["CommunityBanned"]:
            self.community_ban_label.setText('Community Ban: Banned')
            flag = True
        if player_ban_info["EconomyBan"] in ["banned", "probation"]:
            self.economy_ban_label.setText('Trade Ban: Banned')
            flag = True
        if player_ban_info["VACBanned"]:
            self.vac_ban_label.setText('VAC Ban: Banned')
            flag = True
        if player_ban_info["NumberOfGameBans"]:
            self.game_ban_label.setText(f'Game Bans: {player_ban_info["NumberOfGameBans"]}')
            flag = True
        if player_ban_info["DaysSinceLastBan"]:
            self.days_since_ban_label.setText(f'Days since last ban: {player_ban_info["DaysSinceLastBan"]}')
            flag = True
        else:
            self.ban_status_stackedWidget.setCurrentIndex(1)

        if flag:
            self.ban_status_stackedWidget.setCurrentIndex(0)

    def get_recent_games(self, steam_id: str):
        """
            Retrieve and display the recent games played by a Steam user.

            This function uses the Steam API to fetch the recent games played by a user based on
            their Steam ID. It then passes the list of recent games to the display_recent_games
            method to update the user interface.

            Args:
                steam_id (str): The Steam ID of the user.

            Returns:
                None

            Raises:
                Exception: If the API request fails or the Steam ID is invalid.
        """

        try:
            game_count = 3
            response = self.api.call('IPlayerService.GetRecentlyPlayedGames', steamid=steam_id,
                                     count=game_count)
            recent_games = []
            if response['response'] and response['response']['total_count'] > 0:
                for game in response['response']['games']:
                    recent_games.append(game['name'])
                self.display_recent_games(recent_games)
            else:
                return None


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:

            print(f"An error occurred during the API request: {e}")

    def display_recent_games(self, recent_games: list[str]):
        """
           Display the recent games played by the user.

           This function takes a list of recent games and displays them on the user interface.
           If the user has played fewer than three games recently, the remaining labels will
           be empty.

           Args:
               recent_games (list[str]): List of recent games played by the user, with a maximum of 3 items.
           """

        padded_list = recent_games + [''] * (3 - len(recent_games))

        self.recent_game_1_label.setText(padded_list[0])
        self.recent_game_2_label.setText(padded_list[1])
        self.recent_game_3_label.setText(padded_list[2])

    def get_level(self, steam_id: str):
        """
           Retrieve and display the Steam account level of a user.

           This function uses the Steam API to fetch the account level of a user based on
           their Steam ID. It then updates the user interface with the account level.

           Args:
               steam_id (str): The Steam ID of the user.

           Returns:
               None

           Raises:
                Exception: If the API request fails or the Steam ID is invalid.
        """

        try:
            response = self.api.call('IPlayerService.GetSteamLevel', steamid=steam_id)
            account_level = response['response']['player_level']
            self.account_level_label.setText(f'Account level: {account_level}')


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:

            print(f"An error occurred during the API request: {e}")

    def get_friend_count(self, steam_id: str):
        """
            Retrieve and display the friend count of a Steam user.

            This function uses the Steam API to fetch the friend count of a user based on
            their Steam ID. It then updates the user interface with the friend count.

            Args:
                steam_id (str): The Steam ID of the user.

            Returns:
                None

            Raises:
                Exception: If the API request fails or the Steam ID is invalid.
            """
        try:
            response = self.api.call('ISteamUser.GetFriendList', steamid=steam_id)
            friend_count = len(response['friendslist']['friends'])
            self.friend_count_label.setText(f'Friend count: {friend_count}')


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:
            print(f"An error occurred during the API request: {e}")

    def get_creation_date(self, steam_id: str):
        """
            Retrieve and display the account creation date of a Steam user.

            This function uses the Steam API to fetch the account creation date of a user based
            on their Steam ID. It then updates the user interface with the creation date.

            Args:
                steam_id (str): The Steam ID of the user.

            Returns:
                None

            Raises:
                Exception: If the API request fails or the Steam ID is invalid.
            """

        try:
            response = self.api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id)
            creation_time = response['response']['players'][0]['timecreated']
            creation_date = datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            self.creation_date_label.setText(f'Member since: {creation_date}')


        except(requests.exceptions.RequestException, requests.exceptions.Timeout,
               requests.exceptions.TooManyRedirects, requests.exceptions.HTTPError,
               requests.exceptions.ConnectionError) as e:
            print(f"An error occurred during the API request: {e}")

    def display_profile_picture(self, profile_picture_url: str):
        """
        Download and display a profile picture from the given URL.

        Downloads the profile picture from the specified URL and displays it in a QLabel
        widget on the user interface. If the download is successful, the profile picture is
        displayed scaled to fit the label. If the download fails, an error message is printed
        to the console.

        Args:
            profile_picture_url (str): The URL of the profile picture to download and display.

        Returns:
            None
        """

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

        def start_image_download():
            url = QUrl(profile_picture_url)
            request = QNetworkRequest(url)
            reply = self.manager.get(request)
            reply.finished.connect(lambda: handle_image_download(reply))

        delay_ms = 500  # Delay in milliseconds (1000 ms = 1 second)
        QTimer.singleShot(delay_ms, start_image_download)
