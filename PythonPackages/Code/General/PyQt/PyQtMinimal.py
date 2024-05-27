import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
    
programm = QApplication(sys.argv)
    
fenster = QWidget()
fenster.setWindowTitle("Hello-World-Programm")
fenster.setGeometry(500, 500, 400, 200)
    
helloLabel = QLabel("Hello World", parent=fenster)
helloLabel.move(175,20)
    
fenster.show()
    
sys.exit(programm.exec())
