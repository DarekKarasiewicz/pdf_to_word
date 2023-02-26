import sys

# QT imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QLabel
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap

# Others
from pdf2docx import parse



class Drop_File_Box(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(500,500)
        pixmap= QPixmap("pdf_to_word.png")
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

            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    self.file_list.append(str(url.toLocalFile()))
                else:
                    self.file_list.append(str(url.toString()))
        else:
            event.ignore()


        preaty_string =""
        for file in self.file_list:
            x = file.split("/")
            preaty_string +=  x[-1] + "\n"

        self.setText(f"\n\n {preaty_string} \n\n ")

def convert_files_to_pdf(paths):
    "/home/karas/Desktop/pytania-nasze-Dziekańska.pdf"
    for path in paths:
        file_name = path.split("/")[-1]
        if file_name.split(".")[-1] == "pdf":
            new_path = path.replace(path.split("/")[-1],path.split("/")[-1].split(".")[0] + ".docx")
            try :
                parse(path, new_path)

            except:
                print("something went wrong")


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.drop_file_box= Drop_File_Box(self)

        self.btn = QPushButton('Convert', self)
        self.btn.setGeometry(200, 400, 100, 50)

        self.btn.clicked.connect(lambda: convert_files_to_pdf(self.drop_file_box.file_list))



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main_Window()
    window.show()

    sys.exit(app.exec_())
