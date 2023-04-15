from controller import *


def main():
    application = QApplication([])
    window = Controller()
    window.setFixedSize(400, 550)
    window.setWindowTitle("Final Project_1")
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()

