from controller import *


def main():
    application = QApplication([])
    window = Controller()
    window.setFixedSize(450, 550)
    window.setWindowTitle("SteamUserViewer")
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()

