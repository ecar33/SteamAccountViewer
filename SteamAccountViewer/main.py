"""Main module of the SteamUserViewer application."""

from controller import *


def main():
    """
    Initialize and run the SteamUserViewer application.

    This function creates a QApplication, sets up a Controller instance with a fixed size
    and a window title, and then shows the window. It finally starts the QApplication event loop.
    """

    application = QApplication([])
    window = Controller()
    window.setFixedSize(450, 550)
    window.setWindowTitle("SteamUserViewer")
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()

