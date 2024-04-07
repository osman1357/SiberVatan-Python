import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QIcon
""""
def windows():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    win.setWindowTitle("SiberVatan")
    win.setGeometry(700,500,368,498)
    win.setWindowIcon(QIcon('favicon.png'))

    label_name = QtWidgets.QLabel(win)
    label_name.setText('Adınız: ')
    label_name.move(50,30)
    
    label_surname = QtWidgets.QLabel(win)
    label_surname.setText('Soyaınız: ')
    label_surname.move(50,60)
    
    text_name = QtWidgets.QLineEdit(win)
    text_name.move(150,30)
    
    text_sname = QtWidgets.QLineEdit(win)
    text_sname.move(150,60)
    
    save = QtWidgets.QPushButton(win)
    save.setText('Kaydet')
    save.move(150,150)
    
    def clicked():
        print("Ad: "+ text_name.text() + '  ' + "Soyad: " + text_sname.text())
    save.clicked.connect(clicked)
    
    win.show()
    sys.exit(app.exec())
windows()
"""
#--------------------------------------------------------------------------------------------------------------------#

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("Siber VATAN")
        self.setGeometry(750,750,500,500)
        self.setWindowIcon(QIcon('favicon.png'))
        self.initUI()
     
    def initUI(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setText("Adınız: ")
        self.label_name.move(50,30)

        self.label_sname = QtWidgets.QLabel(self)
        self.label_sname.setText('Soyadınız: ')
        self.label_sname.move(50,60)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)

        self.txt_lname = QtWidgets.QLineEdit(self)
        self.txt_lname.move(150,70)
        
        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setText('Sonuç: ')
        self.label_result.resize(100,100)
        self.label_result.move(150,150)
        
        self.save = QtWidgets.QPushButton(self)
        self.save.setText('Kaydet')
        self.save.move(150,120)
        self.save.clicked.connect(self.clicked)

    def clicked(self):
        self.label_result.setText("Ad: " + self.txt_name.text() + "  " + "Soyad: " + self.txt_lname.text())
        
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
window()


#Class fonksiyonlara init çalış
