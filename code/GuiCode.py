import string
from APP_GUI.gui import *
from Acl import Acl as AclClass
from PyQt4 import QtCore, QtGui

#myAcl = AclClass("192.168.2.1", "permit")
#myAcl.printState()
#print WebDev Branch test 2
ui = None

def printStuff():
    global ui
    ui.guiLeSrcMac.setText("Ahoj")
    print "ahoj"

def actionPerformedGuiBtnDelete():
    global ui
    print "actionPerformedGuiBtnDelete"

def actionPerformedGuiBtnEdit():
    global ui
    print "actionPerformedGuiBtnEdit"

def actionPerformedGuiBtnCreate():
    global ui
    print "actionPerformedGuiBtnCreate"

def actionPerformedGuiCbForwarder():
    global ui
    print "Forwarder changed to: "+ui.guiCbForwarder.currentText()
    loadSelectedForwarder(ui.guiCbForwarder.currentText())

def actionPerformedGuiCbL4Protocol():
    global ui
    print "L4 protocol changed to:"+ui.guiCbL4Protocol.currentText()

def actionPerformedGuiChbEnableFirewall():
    global ui
    if ui.guiChbEnableFirewall.isChecked():
        print "Firewall is activated"
    else:
        print "Firewall is deactivated"

def loadSelectedForwarder(forwarderName):
    print "Loading Forwarder: "+forwarderName+" to GUI"



class GuiManager(Ui_MainWindow):

    def __init__(self):
        Ui_MainWindow.__init__(self)

    def start(self):
        print "JOZKo"
        print "stuff"
        self.guiBtnDelete.clicked.connect(actionPerformedGuiBtnDelete)
        self.guiBtnCreate.clicked.connect(actionPerformedGuiBtnCreate)
        self.guiBtnEdit.clicked.connect(actionPerformedGuiBtnDelete)
        self.guiCbForwarder.currentIndexChanged.connect(actionPerformedGuiCbForwarder)
        self.guiChbEnableFirewall.stateChanged.connect(actionPerformedGuiChbEnableFirewall)
        self.guiCbL4Protocol.currentIndexChanged.connect(actionPerformedGuiCbL4Protocol)


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

