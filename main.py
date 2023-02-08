import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QPushButton, QLabel
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap

class Drop_File_Box(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(500,500)
        pixmap= QPixmap("./pdf_to_word.png")
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)
        self.file_list = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.file_list = links
            print(self.file_list)

        else:
            event.ignore()

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.drop_file_box= Drop_File_Box(self)

        self.btn = QPushButton('Get Value', self)
        self.btn.setGeometry(200, 400, 100, 50)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main_Window()
    window.show()

    sys.exit(app.exec_())
