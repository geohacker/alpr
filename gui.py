# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alpr.ui'
#
# Created: Sat Jul  3 21:56:16 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
from main import main
files=range(1,21)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Automatic License Plate Recognition")
        MainWindow.resize(605, 560)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_number = QtGui.QLineEdit(self.centralwidget)
        self.text_number.setGeometry(QtCore.QRect(10, 450, 221, 41))
        self.text_number.setObjectName("text_number")
        self.button_load = QtGui.QPushButton(self.centralwidget)
        self.button_load.setGeometry(QtCore.QRect(330, 460, 121, 31))
        self.button_load.setObjectName("button_load")
        self.label_image = QtGui.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 20, 551, 421))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
	self.label_image
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 581, 431))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_exit = QtGui.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(460, 460, 121, 31))
        self.button_exit.setObjectName("button_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_load, self.button_exit)
        MainWindow.setTabOrder(self.button_exit, self.text_number)
	QtCore.QObject.connect(self.button_load,QtCore.SIGNAL("clicked()"), self.load)
#	QtCore.QObject.connect(self.button_exit,QtCore.SIGNAL("clicked()"), self.#)
	

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("Automatic License Plate Recognition", "Automatic License Plate Recognition", None, QtGui.QApplication.UnicodeUTF8))
        self.button_load.setText(QtGui.QApplication.translate("MainWindow", "Load Image", None, QtGui.QApplication.UnicodeUTF8))
        self.button_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
		

	for item in files:
		print "Loading image...."
		image = QtGui.QPixmap(os.getcwd() + "/images/" + str(item) + ".jpg")
		self.label_image.setPixmap(image)
		print "Extracting information... "
		license_number = main(item)
		print "Done"
		self.text_number.setText(license_number)
		files.remove(item)		
		break
    

class Main(QtGui.QMainWindow):
     def __init__(self):
         QtGui.QMainWindow.__init__(self)

         # This is always the same
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)


def main_gui():
     # Again, this is boilerplate, it's going to be the same on
     # almost every app you write
     app = QtGui.QApplication(sys.argv)
     window=Main()
     window.show()
     # It's exec_ because exec is a reserved word in Python
     sys.exit(app.exec_())
     

if __name__ == "__main__":
     main_gui()
