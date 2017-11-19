import string
from APP_GUI.gui import *
from AclRule import Acl as AclClass
from PyQt4 import QtCore, QtGui
from Forwarder import *

#myAcl = AclClass("192.168.2.1", "permit")
#myAcl.printState()
#print WebDev Branch test 2
ui = None
fwList = []
selectedFw = None

def loadForwarders(list):
    global selectedFw
    fw1 = Forwarder(1, "Janko")
    fw2 = Forwarder(2, "Samko")
    fw3 = Forwarder(3, "Danko")
    list.append(fw1)
    list.append(fw2)
    list.append(fw3)
    if selectedFw is None:
        selectedFw = list[0]


def loadForwardersToGui():
    global fwList
    global ui
    print "Loading Fw to Gui: "
    for i in fwList:
        print "Fw list: "+i.name
        ui.guiCbForwarder.addItem(i.name)




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
    l4proto = ui.guiCbL4Protocol.currentText()
    print "L4 protocol changed to:"+l4proto
    if l4proto != "TCP" and l4proto != "UDP":
        print "Block Src/Dst port number lineEdit"
        ui.guiLeSrcPortNumber.setDisabled(True)
        ui.guiLeDstPortNumber.setDisabled(True)
    else:
        print "Unblock Src/Dst port number lineEdit"
        ui.guiLeSrcPortNumber.setDisabled(False)
        ui.guiLeDstPortNumber.setDisabled(False)


def actionPerformedGuiChbEnableFirewall():
    global ui
    if ui.guiChbEnableFirewall.isChecked():
        print "Firewall is activated"
    else:
        print "Firewall is deactivated"

def loadSelectedForwarder(forwarderName):
    global fwList, selectedFw
    print "Searching Forwarder in fwList: "+forwarderName+" to GUI"
    for i in fwList:
        if i.name == forwarderName:
            print "I found forwarder: "+i.name+"i will load it to Table"
            selectedFw = i

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

    loadForwarders(fwList)
    loadForwardersToGui()

    sys.exit(app.exec_())



