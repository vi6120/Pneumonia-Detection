import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
    
class HoLoginGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login fuer heise online")
    
        self.zentralesWidget = QWidget(self)
        self.setCentralWidget(self.zentralesWidget)
    
    def programm():
        hologin = QApplication(sys.argv)
    
        gui = HoLoginGui()
        gui.show()
    
        sys.exit(hologin.exec())
    
    
programm()

