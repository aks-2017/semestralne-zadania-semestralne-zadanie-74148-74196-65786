import string
from APP_GUI.gui import *
from Acl import Acl as AclClass
from PyQt4 import QtCore, QtGui


print string.uppercase
myAcl = AclClass("192.168.2.1", "permit")
myAcl.printState()
ui = None

def printStuff():
    global ui
    print "JOZKo"
    ui.lineEdit.setText("Jozko nepije")

class GuiManager(Ui_MainWindow):

    def __init__(self):
        Ui_MainWindow.__init__(self)

    def start(self):
        print "JOZKo"
        self.guiBtnDelete.clicked.connect(printStuff)


if __name__ == "__main__":
    import sys
    print('Starting GUI')
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = GuiManager()
    ui.setupUi(MainWindow)
    ui.start()
    MainWindow.show()
    sys.exit(app.exec_())

