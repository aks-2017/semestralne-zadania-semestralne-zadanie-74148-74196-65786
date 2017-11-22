import string
import requests
import json
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


print ("udene klobasy")


def addNewRuleToAcl():
    # add New Rule to ACL from GUI text fields
    global ui
    print "Add new rule to acl"
    action = str(ui.guiCbAction.currentText())
    id = len(selectedFw.acl)+1
    srcMac = ui.guiLeSrcMac.text()
    dstMac = ui.guiLeDstMac.text()
    srcIp = ui.guiLeSrcIp.text()
    dstIp = ui.guiLeDstIp.text()
    srcPrefix = ui.guiLeSrcPrefix.text()
    dstPrefix =  ui.guiLeDstPrefix.text()
    l4Protocol = str(ui.guiCbL4Protocol.currentText())
    interface = str(ui.guiCbInterface.currentText())
    direction = str(ui.guiCbDirection.currentText())
    srcPortNumber = ui.guiLeSrcPortNumber.text()
    dstPortNumber = ui.guiLeDstPortNumber.text()

    selectedFw.addRuleToAcl(
        AclClass(action, id, srcMac, dstMac, srcIp, dstIp, srcPrefix, dstPrefix, l4Protocol,
                 interface, direction, srcPortNumber, dstPortNumber))
    loadSelectedForwarderToGuiTblFirewallRules()

def loadForwarders(list):
    global selectedFw
    fw1 = Forwarder(1, "Alfa")
    fw2 = Forwarder(2, "Gama")
    fw3 = Forwarder(3, "Delta")
    list.append(fw1)
    list.append(fw2)
    list.append(fw3)
    if selectedFw is None:
        selectedFw = list[0]

def testFunctionForFW():
    selectedFw.addRuleToAcl( AclClass("permit", 1, "aa:aa:aa:bb:bb:bb", "cc:cc:cc:dd:dd:dd", "192.168.5.2", "192.168.3.5", 20, 25, "UDP","s0/0/0", "IN",123,456))
    selectedFw.addRuleToAcl(
        AclClass("deny", 2, "aa:aa:aa:bb:bb:bb", "cc:cc:cc:dd:dd:dd", "192.168.5.2", "192.168.3.5", 20, 25, "TCP",
                 "s0/0/0", "IN",321,654))
    selectedFw.printAclRules()


def loadSelectedForwarder(forwarderName):
    global fwList, selectedFw
    print "Searching Forwarder in fwList: "+forwarderName+" to GUI"
    for i in fwList:
        if i.name == forwarderName:
            print "I found forwarder: "+i.name+"i will load it to Table"
            selectedFw = i
    loadSelectedForwarderToGuiTblFirewallRules()

def loadSelectedForwarderToGuiTblFirewallRules():
    global selectedFw, ui
    ui.guiTblFirewallRules.setRowCount(0)
    index = 0
    ui.guiTblFirewallRules.setRowCount(len(selectedFw.acl))
    for i in selectedFw.acl:
        print "I will ad this rule"
        ui.guiTblFirewallRules.setItem(index,0, QtGui.QTableWidgetItem(str(i.id)))
        ui.guiTblFirewallRules.setItem(index, 1, QtGui.QTableWidgetItem(i.action))
        ui.guiTblFirewallRules.setItem(index, 2, QtGui.QTableWidgetItem(i.srcMac))
        ui.guiTblFirewallRules.setItem(index, 3, QtGui.QTableWidgetItem(i.dstMac))
        ui.guiTblFirewallRules.setItem(index, 4, QtGui.QTableWidgetItem(i.srcIp+"/"+str(i.srcPrefix)))
        ui.guiTblFirewallRules.setItem(index, 5, QtGui.QTableWidgetItem(i.dstIp+"/"+str(i.dstPrefix)))
        ui.guiTblFirewallRules.setItem(index, 6, QtGui.QTableWidgetItem(i.l4Protocol+" ("+str(i.srcPortNumber)+"/"+str(i.dstPortNumber)+")"))
        ui.guiTblFirewallRules.setItem(index, 7, QtGui.QTableWidgetItem(i.interface))
        ui.guiTblFirewallRules.setItem(index, 8, QtGui.QTableWidgetItem(i.direction))
        index += 1
    header = ui.guiTblFirewallRules.horizontalHeader()
    for x in range(0, 9):
        header.setResizeMode(x, QtGui.QHeaderView.ResizeToContents)

def actionPerformedGuiChbEnableFirewall():
    global ui
    if ui.guiChbEnableFirewall.isChecked():
        print "Firewall is activated"
    else:
        print "Firewall is deactivated"

def loadForwardersToGuiCbForwarder():
    global fwList
    global ui, selectedFw
    print "Loading Fw to Gui: "
    for i in fwList:
        print "Fw list: " + i.name
        ui.guiCbForwarder.addItem(i.name)

def actionPerformedGuiBtnDelete():
    global ui
    print "actionPerformedGuiBtnDelete"

    #FIRST ENTRY FOR GOTO
    #mec = {"type":"GOTO_TABLE", "table_id": 1, }
    #data = {"dpid": "1", "table_id": "0", "priority": "65535", "actions": [mec]}
    #r2 = requests.post('http://localhost:8080/stats/flowentry/add', data=json.dumps(data))
    #r2.status_code

    #GET FOR NUMBER OF FORWARDERS
    #r = requests.get('http://localhost:8080/stats/switches')
    #r.status_code



    #POST FOR DELETION OF ENRTY
    #mec = {"type":"GOTO_TABLE", "table_id": 1}
    #data = {"dpid": "1", "table_id": "0", "priority": "22222", "actions": [mec]}
    #r2 = requests.post('http://localhost:8080/stats/flowentry/delete', data=json.dumps(data))
    #r2.status_code



def actionPerformedGuiBtnEdit():
    global ui
    print "actionPerformedGuiBtnEdit"


def actionPerformedGuiBtnCreate():
    global ui
    print "actionPerformedGuiBtnCreate"

    # POST FOR SPECIFIC ENTRY

    data2 = {}
    data2['nw_src'] = str(ui.guiLeSrcIp.text())

    data2['nw_dst'] = str(ui.guiLeDstIp.text())

    data = {"dpid": "1", "priority": "22222", "table_id": "0", "match":
            dict(data2, **{'nw_proto': '1', 'dl_type': '2048'})}

    r = requests.post('http://localhost:8080/stats/flowentry/add', data=json.dumps(data))
    r.status_code

    #addNewRuleToAcl()

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

class GuiManager(Ui_MainWindow):

    def __init__(self):
        Ui_MainWindow.__init__(self)

    def start(self):
        # add action performed functions
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
    loadForwardersToGuiCbForwarder()
    testFunctionForFW()
    loadSelectedForwarder(ui.guiCbForwarder.currentText())

    sys.exit(app.exec_())



