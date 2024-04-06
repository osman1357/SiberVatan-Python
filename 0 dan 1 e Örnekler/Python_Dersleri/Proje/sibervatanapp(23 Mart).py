import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QIcon

def windows():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    win.setWindowTitle("Siber Vatan")         #dosya adını belirler
    
    win.setGeometry(700,500,400,300)          #dosyanın boyutlarını belirler
    
    win.setWindowIcon(QIcon('favicon.png'))   #sayfanın resmini günceller(istediğimiz resmi koyabiliriz)
    
    win.show()
    sys.exit(app.exec())          #çarpı işaretine basıldığında kapanmasını sağlar

windows()


#Qt kütüphaneini araştır.