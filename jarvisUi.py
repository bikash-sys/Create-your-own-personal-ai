from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(984, 572)

        jarvisUi.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        jarvisUi.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        jarvisUi.setWindowIcon(QtGui.QIcon(".\\Material\\icon.png"))

        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")

        # Background label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Middle AI Animation GIF - Centered and Sized
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(102, 30, 780, 550))  # Centered
        self.label_3.setStyleSheet("background: transparent;")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.movie_center = QtGui.QMovie(r"C:\Users\tiktok\Downloads\Circle Waves GIF by futur21.gif")
        self.label_3.setMovie(self.movie_center)
        self.movie_center.start()

        # Logo GIF
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 20, 261, 221))
        self.label_5.setPixmap(QtGui.QPixmap(".\\Material\\logo.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        # Left bottom text
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent; border: none; color: white;")
        self.textBrowser.setObjectName("textBrowser")

        # Right next to it
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent; border: none; color: white;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        # Left corner animation
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.label_2.setPixmap(QtGui.QPixmap(".\\Material\\new.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        # Start Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
        self.pushButton.setStyleSheet("""
            font: 8pt "Segoe Print";
            color: yellow;
            background-color: rgba(0, 0, 0, 100);
            border: 1px solid yellow;
            border-radius: 5px;
        """)
        self.pushButton.setObjectName("pushButton")

        # Stop Button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
        self.pushButton_2.setStyleSheet("""
            font: 8pt "Verdana";
            color: red;
            background-color: rgba(0, 0, 0, 100);
            border: 1px solid red;
            border-radius: 5px;
        """)
        self.pushButton_2.setObjectName("pushButton_2")

        jarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

        # Connect buttons to actions
        self.pushButton.clicked.connect(self.start_action)
        self.pushButton_2.clicked.connect(self.stop_action)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "Jarvis UI"))
        self.pushButton.setText(_translate("jarvisUi", "Start"))
        self.pushButton_2.setText(_translate("jarvisUi", "Stop"))

    def start_action(self):
        print("🟢 Jarvis Started")
        self.textBrowser.setText("Jarvis")
        self.textBrowser_2.setText("Running...")

    def stop_action(self):
        print("🔴 Jarvis Stopped")
        self.textBrowser.setText("Jarvis")
        self.textBrowser_2.setText("Stopped")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
