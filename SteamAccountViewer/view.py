# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SteamAccountViewer/view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 600)
        MainWindow.setStyleSheet("background-color: rgb(42, 71, 94)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.main_stackedWidget.setGeometry(QtCore.QRect(10, 70, 451, 521))
        self.main_stackedWidget.setObjectName("main_stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.submit_pushButton = QtWidgets.QPushButton(self.page_3)
        self.submit_pushButton.setGeometry(QtCore.QRect(150, 170, 131, 23))
        self.submit_pushButton.setStyleSheet("background-color: rgb(33, 101, 138);\n"
"color: rgb(235, 235, 235)")
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.page_3)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 361, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(235, 235, 235)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.steamid_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.steamid_lineEdit.setStyleSheet("\n"
"color: rgb(144, 144, 144);\n"
"background-color: rgb(42, 63, 90)\n"
"")
        self.steamid_lineEdit.setText("")
        self.steamid_lineEdit.setObjectName("steamid_lineEdit")
        self.gridLayout.addWidget(self.steamid_lineEdit, 0, 1, 1, 1)
        self.main_stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.profile_picture_label = QtWidgets.QLabel(self.page_4)
        self.profile_picture_label.setGeometry(QtCore.QRect(50, 30, 128, 128))
        self.profile_picture_label.setObjectName("profile_picture_label")
        self.info_stackedWidget = QtWidgets.QStackedWidget(self.page_4)
        self.info_stackedWidget.setGeometry(QtCore.QRect(220, 10, 221, 281))
        self.info_stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_stackedWidget.setObjectName("info_stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_5)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 211, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.creation_date_label = QtWidgets.QLabel(self.layoutWidget1)
        self.creation_date_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.creation_date_label.setObjectName("creation_date_label")
        self.verticalLayout.addWidget(self.creation_date_label)
        self.account_level_label = QtWidgets.QLabel(self.layoutWidget1)
        self.account_level_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.account_level_label.setObjectName("account_level_label")
        self.verticalLayout.addWidget(self.account_level_label)
        self.friend_count_label = QtWidgets.QLabel(self.layoutWidget1)
        self.friend_count_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.friend_count_label.setObjectName("friend_count_label")
        self.verticalLayout.addWidget(self.friend_count_label)
        self.info_stackedWidget.addWidget(self.page_5)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 169, 55))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setObjectName("label_5")
        self.info_stackedWidget.addWidget(self.page)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.layoutWidget2 = QtWidgets.QWidget(self.page_6)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 10, 211, 271))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.recent_game_1_label = QtWidgets.QLabel(self.layoutWidget2)
        self.recent_game_1_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.recent_game_1_label.setObjectName("recent_game_1_label")
        self.verticalLayout_2.addWidget(self.recent_game_1_label)
        self.recent_game_2_label = QtWidgets.QLabel(self.layoutWidget2)
        self.recent_game_2_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.recent_game_2_label.setText("")
        self.recent_game_2_label.setObjectName("recent_game_2_label")
        self.verticalLayout_2.addWidget(self.recent_game_2_label)
        self.recent_game_3_label = QtWidgets.QLabel(self.layoutWidget2)
        self.recent_game_3_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.recent_game_3_label.setText("")
        self.recent_game_3_label.setObjectName("recent_game_3_label")
        self.verticalLayout_2.addWidget(self.recent_game_3_label)
        self.info_stackedWidget.addWidget(self.page_6)
        self.persona_name_label = QtWidgets.QLabel(self.page_4)
        self.persona_name_label.setGeometry(QtCore.QRect(60, 170, 81, 21))
        self.persona_name_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.persona_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.persona_name_label.setObjectName("persona_name_label")
        self.page_pushButton = QtWidgets.QPushButton(self.page_4)
        self.page_pushButton.setGeometry(QtCore.QRect(290, 310, 75, 23))
        self.page_pushButton.setStyleSheet("background-color: rgb(33, 101, 138);\n"
"color: rgb(235, 235, 235)")
        self.page_pushButton.setObjectName("page_pushButton")
        self.ban_status_stackedWidget = QtWidgets.QStackedWidget(self.page_4)
        self.ban_status_stackedWidget.setGeometry(QtCore.QRect(0, 280, 211, 211))
        self.ban_status_stackedWidget.setObjectName("ban_status_stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.economy_ban_label = QtWidgets.QLabel(self.page_2)
        self.economy_ban_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.economy_ban_label.setObjectName("economy_ban_label")
        self.verticalLayout_3.addWidget(self.economy_ban_label)
        self.vac_ban_label = QtWidgets.QLabel(self.page_2)
        self.vac_ban_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.vac_ban_label.setObjectName("vac_ban_label")
        self.verticalLayout_3.addWidget(self.vac_ban_label)
        self.community_ban_label = QtWidgets.QLabel(self.page_2)
        self.community_ban_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.community_ban_label.setObjectName("community_ban_label")
        self.verticalLayout_3.addWidget(self.community_ban_label)
        self.game_ban_label = QtWidgets.QLabel(self.page_2)
        self.game_ban_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.game_ban_label.setObjectName("game_ban_label")
        self.verticalLayout_3.addWidget(self.game_ban_label)
        self.days_since_ban_label = QtWidgets.QLabel(self.page_2)
        self.days_since_ban_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.days_since_ban_label.setObjectName("days_since_ban_label")
        self.verticalLayout_3.addWidget(self.days_since_ban_label)
        self.ban_status_stackedWidget.addWidget(self.page_2)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_7 = QtWidgets.QLabel(self.page_7)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 161, 28))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.ban_status_stackedWidget.addWidget(self.page_7)
        self.view_another_pushButton = QtWidgets.QPushButton(self.page_4)
        self.view_another_pushButton.setGeometry(QtCore.QRect(40, 210, 121, 23))
        self.view_another_pushButton.setStyleSheet("background-color: rgb(33, 101, 138);\n"
"color: rgb(235, 235, 235)")
        self.view_another_pushButton.setObjectName("view_another_pushButton")
        self.main_stackedWidget.addWidget(self.page_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(235, 235, 235);\n"
"background-color: rgb(23, 26, 33)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_stackedWidget.setCurrentIndex(0)
        self.info_stackedWidget.setCurrentIndex(0)
        self.ban_status_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label_2.setText(_translate("MainWindow", "Enter a valid steam id here:"))
        self.profile_picture_label.setText(_translate("MainWindow", "ProfilePicturePlaceholder"))
        self.label_3.setText(_translate("MainWindow", "Profile Data"))
        self.creation_date_label.setText(_translate("MainWindow", "Member since: Not available"))
        self.account_level_label.setText(_translate("MainWindow", "Account level: Not available"))
        self.friend_count_label.setText(_translate("MainWindow", "Friend count: Not available"))
        self.label_5.setText(_translate("MainWindow", "This profile is private."))
        self.label_4.setText(_translate("MainWindow", "Recently Played Games"))
        self.recent_game_1_label.setText(_translate("MainWindow", "No recent games found!"))
        self.persona_name_label.setText(_translate("MainWindow", "PersonaName"))
        self.page_pushButton.setText(_translate("MainWindow", "Page ->"))
        self.label_6.setText(_translate("MainWindow", "Bans on record:"))
        self.economy_ban_label.setText(_translate("MainWindow", "Trade Ban: None"))
        self.vac_ban_label.setText(_translate("MainWindow", "VAC Ban: None"))
        self.community_ban_label.setText(_translate("MainWindow", "Community Ban: None"))
        self.game_ban_label.setText(_translate("MainWindow", "Game Bans: None"))
        self.days_since_ban_label.setText(_translate("MainWindow", "Days since last ban: None on record."))
        self.label_7.setText(_translate("MainWindow", "No bans on record."))
        self.view_another_pushButton.setText(_translate("MainWindow", "View another profile"))
        self.label.setText(_translate("MainWindow", "Steam User Viewer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
