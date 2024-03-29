from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pytube import YouTube
import os 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 493)
        MainWindow.setStyleSheet("background-color:rgb(150, 150, 150)rgb(195, 195, 195)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(160, 160, 380, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_link.setFont(font)
        self.txt_link.setStyleSheet("background-color: white;\n"
                                    "border-style: outset;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;")
        self.txt_link.setObjectName("txt_link")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(260, 260, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_download.setFont(font)
        self.bt_download.setStyleSheet("QPushButton{\n"
                                        "\n"
                                        "background-color: rgb(0, 255, 127);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "border-color: black;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgb(0, 255, 127);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "border-color: white;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.bt_download.setObjectName("bt_download")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.rb_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp3.setGeometry(QtCore.QRect(240, 210, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_mp3.setFont(font)
        self.rb_mp3.setChecked(True)
        self.rb_mp3.setObjectName("rb_mp3")
        self.rb_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp4.setGeometry(QtCore.QRect(370, 210, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_mp4.setFont(font)
        self.rb_mp4.setObjectName("rb_mp4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 291, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("main/YouTube-Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName("menubar")
        self.menuYoutubedownload = QtWidgets.QMenu(self.menubar)
        self.menuYoutubedownload.setObjectName("menuYoutubedownload")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuYoutubedownload.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bt_download.clicked.connect(self.download)

    def download(self):
        try:
            if self.rb_mp4.isChecked() == True:
                url = self.txt_link.text()
                youtube_downloader = YouTube(url)
                movie = youtube_downloader.streams.get_highest_resolution()
                movie.download()
                QMessageBox.information(self.centralwidget, "Download Concluído", f"Download do vídeo {url} concluído com sucesso!")
            elif self.rb_mp3.isChecked() == True:
                url = self.txt_link.text()
                youtube_downloader = YouTube(url)
                song = youtube_downloader.streams.filter(only_audio=True).first()
                out_file = song.download() 
                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"
                os.rename(out_file, new_file)
                QMessageBox.information(self.centralwidget, "Download Concluído", f"Download do vídeo {url} concluído com sucesso!")
        except:
            QMessageBox.critical(self.centralwidget, "Video Não Encontrado", f"Não encontramos o vídeo em questão!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Link:"))
        self.rb_mp3.setText(_translate("MainWindow", "Mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "Mp4"))
        self.menuYoutubedownload.setTitle(_translate("MainWindow", "Youtubedownload"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
