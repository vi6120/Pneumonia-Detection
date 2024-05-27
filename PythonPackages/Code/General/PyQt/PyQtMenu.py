import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
    
    
class HoLoginGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login fuer heise online")
    
        self.zentralesWidget = QWidget(self)
        self.setCentralWidget(self.zentralesWidget)
    
        self.layout = QGridLayout()
        self.zentralesWidget.setLayout(self.layout)
    
        self.menu()
        self.widgets()
    
    def widgets(self):
        self.labelBeschreibungstext = QLabel("Gib deine Logindaten fuer heise online ein \n und druecke dann den Button.")
        self.labelBeschreibungstext.setAlignment(Qt.AlignCenter)
    
        self.labelBenutzername = QLabel("Benutzername:")
        self.labelPasswort = QLabel("Passwort:")
    
        self.eingabeBenutzername = QLineEdit()
        self.eingabeBenutzername.setFixedWidth(120)
    
        self.eingabePasswort = QLineEdit()
        self.eingabePasswort.setEchoMode(QLineEdit.Password)
        self.eingabePasswort.setFixedWidth(120)
    
        self.buttonEinloggen = QPushButton("Einloggen")
        self.buttonEinloggen.setFixedWidth(120)
        self.buttonEinloggen.clicked.connect(self.buttonGeklickt)
    
        self.layout.addWidget(self.labelBeschreibungstext, 0, 0, 1, 2, alignment=Qt.AlignBottom)
        self.layout.addWidget(self.labelBenutzername, 1, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(self.labelPasswort, 2, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(self.eingabeBenutzername, 1, 1, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.eingabePasswort, 2, 1, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.buttonEinloggen, 3, 0, 1, 2, alignment=Qt.AlignCenter | Qt.AlignTop)
    
    def menu(self):
        self.menu = self.menuBar().addMenu("&Datei")
        self.menu.addAction("&Beenden", self.close)
    
    def buttonGeklickt(self):
        self.benutzername = self.eingabeBenutzername.text()
        self.passwort = self.eingabePasswort.text()
    
        self.fake_browser = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
        self.login_daten = {"username": self.benutzername, "password": self.passwort, "action": "/sso/login/login"}
    
        self.login = requests.Session().post(url="https://www.heise.de/sso/login/login",
                                             data=self.login_daten,
                                             headers=self.fake_browser)
    
        if "Der Benutzername oder das Passwort ist falsch." in self.login.text:
            self.labelBeschreibungstext.setText("Fehler: Der Benutzername \n oder das Passwort ist falsch.")
            self.labelBeschreibungstext.setStyleSheet("color: red;")
        else:
            self.labelBeschreibungstext.setText("Sie haben sich erfolgreich eingeloggt.")
            self.labelBeschreibungstext.setStyleSheet("color: green;")
    
    
def programm():
    hologin = QApplication(sys.argv)
    
    gui = HoLoginGui()
    gui.show()
    
    sys.exit(hologin.exec())
    
    
programm()