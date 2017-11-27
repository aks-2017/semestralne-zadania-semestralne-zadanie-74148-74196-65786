import string
import requests
import json
from APP_GUI.gui import *
from AclRule import Acl as AclClass
from PyQt4 import QtCore, QtGui
from Forwarder import *
from netaddr import IPAddress

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
    global selectedFw, ui

    # GET FOR NUMBER OF FORWARDERS
    r = requests.get('http://localhost:8080/stats/switches')
    result = r.content.translate(None, '[] ')

    # LAST ENTRY TAB #0 FOR IMPLICIT PERMIT
    actions = {"type": "GOTO_TABLE", "table_id": 1 }
    #actions1 = {"type": "GOTO_TABLE", "table_id": 2 }
    #match = {"nw_src": "10.0.0.1/24", "nw_proto": "1" }

    mn_position = 0
    for x in result.split(','):
        list.append(Forwarder(mn_position, "Forwarder s"+x))
        mn_position+=1

        #Check whether any ACL entires exist in FlowTable0 befor initalizing app
        #and if any, add to GUI and app structures
        r = requests.get('http://localhost:8080/stats/flow/'+x, data=json.dumps({'table_id': '0'}))
        print r.content

        #TODO add entries to GUI and internal structures, if returned any

        # LAST ENTRY TAB #0 FOR IMPLICIT PERMIT
        data = {"dpid": x, "table_id": "0", "priority": "65535", "actions": [actions]}
        #print data
        r2 = requests.post('http://localhost:8080/stats/flowentry/add', data=json.dumps(data))
        r2.status_code

    if mn_position == 0:
        list.append(Forwarder(mn_position, "No Forwarder connected"))

    if selectedFw is None:
        selectedFw = list[0]

    #data = {"dpid": 1, "table_id": "0", "priority": "1", "match": [match], "actions": [actions1]}
    #r2 = requests.post('http://localhost:8080/stats/flowentry/add', data=json.dumps(data))
    #r2.status_code

def loadForwardersFlowTableAction(x):
    pom = 1
    for i in fwList:
        if i.name == x:
            break
        pom += 1
    pom = str(pom)
    requestik = requests.get('http://localhost:8080/stats/flow/'+pom, data=json.dumps({'table_id': '0'}))
    #print r.content
    jasonData = json.loads(requestik.content)
    try:
       loadFromForwardersFlowTable(jasonData, pom)
    except AttributeError:
       print "Nepodarilo sa najst zvoleny forwarder"

# nacita z jasonData z GET obsah flow table0
def loadFromForwardersFlowTable(jasonData, pom):

    mojeData = jasonData[pom]
    aclID = 0
    for iter1 in mojeData:
        srcMac = "0"
        dstMac = "0"
        srcIP = "0"
        dstIP = "0"
        srcPrefix = "0"
        dstPrefix = "0"
        srcPort = "0"
        dstPort = "0"
        protocol = "0"
        print "Pokusam sa hladat"
        for iter2 in iter1.iteritems():
            # if ("priority" in iter2):  ked Kubo doda priority bunku
            #    print iter2[1]
            if ("match" in iter2):
                for tupleiter in iter2:
                    if "nw_src" in tupleiter:
                        IP, prefix = tupleiter["nw_src"].split('/')
                        srcPrefix = IPAddress(prefix).netmask_bits()
                        srcIP = IP
                    if "nw_dst" in tupleiter:
                        IP, prefix = tupleiter["nw_dst"].split('/')
                        dstPrefix = IPAddress(prefix).netmask_bits()
                        dstIP = IP
                    if "dl_src" in tupleiter:
                        srcMac = tupleiter["dl_src"]
                    if "dl_dst" in tupleiter:
                        dstMac = tupleiter["dl_dst"]
                    if "nw_proto" in tupleiter:
                        protocol = translateProtocol(tupleiter["nw_proto"])
                    if "tp_src" in tupleiter:
                        srcPort = tupleiter["tp_src"]
                    if "tp_dst" in tupleiter:
                        dstPort = tupleiter["tp_dst"]
            if ("actions" in iter2):
                if "GOTO_TABLE:1" in iter2[1]:
                    actionGui = "permit"
                else:
                    actionGui = "deny"
            if ("priority" in iter2):
                aclID = iter2[1]
        testFunctionForFW(actionGui, aclID, srcMac, srcPrefix, dstMac, dstPrefix, srcIP, dstIP, protocol, "", "", srcPort, dstPort)
        #aclID -= 100

def translateProtocol(numberOfProtocol):
    if numberOfProtocol == 1:
        return "ICMP"
    elif numberOfProtocol == 6:
        return "TCP"
    elif numberOfProtocol == 17:
        return "UDP"

# akciu, id, src MAC, dst MAC, src IP, dst IP, protokol, interface, smer, src port, dst port
def testFunctionForFW(actionGui, id, srcMac, srcPrefix, dstMac, dstPrefix, srcIP, dstIP, protocol, inter, direct, srcPort, dstPort):
    selectedFw.addRuleToAcl(
        AclClass(actionGui, id, srcMac, dstMac, srcIP, dstIP, srcPrefix, dstPrefix, protocol,
                 inter, direct,srcPort,dstPort))
    #selectedFw.printAclRules()

def loadSelectedForwarder(forwarderName):
    global fwList, selectedFw
    print "Searching Forwarder in fwList: "+forwarderName+" to GUI"
    for i in fwList:
        if i.name == forwarderName:
            print "I found forwarder: "+i.name+" will load it to Table"
            selectedFw = i
            #print "ahoj ahoj ahoj"+str(selectedFw.acl)
    loadSelectedForwarderToGuiTblFirewallRules()

def loadSelectedForwarderToGuiTblFirewallRules():
    global selectedFw, ui
    ui.guiTblFirewallRules.setRowCount(0)
    index = 0

    #selectedFw.acl = none
    del selectedFw.acl[:]
    loadForwardersFlowTableAction(ui.guiCbForwarder.currentText())
    ui.guiTblFirewallRules.setRowCount(len(selectedFw.acl))
    #while (ui.guiTblFirewallRules.rowCount() > 0):
    #        ui.guiTblFirewallRules.removeRow(0)

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

        #TODO Possible implementation as ACL statement w/ priority of 65535 and actions "GOTO_TABLE table_id = 1"

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

    #TODO load variables (as separate function, used also in EDIT) from GUI to JSON attributes

    ACL_result = {}
    #pomPerm = ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),1)
    #pomPerm = str(pomPerm.text())
    if str(ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),1).text()) == 'permit':
        ACL_result = {"type": "GOTO_TABLE", "table_id": 1}
    else:
        ACL_result = {"type": "DROP"}

    pom = 1
    for i in fwList:
        if i.name == ui.guiCbForwarder.currentText():
            break
        pom += 1
    pom = str(pom)

    P = ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),0).text()
    P = int(P)
    data = {"dpid": pom, "priority": str(P), "table_id": "0", "match":
        dict(loadSelectedRowData(), **{'dl_type': '2048'}), "actions": [ACL_result]}

    r = requests.post('http://localhost:8080/stats/flowentry/delete_strict', data=json.dumps(data))
    r.status_code

    #POST FOR DELETION OF ENRTY
    #mec = {"type":"GOTO_TABLE", "table_id": 1}
    #data = {"dpid": "1", "table_id": "0", "priority": "22222", "actions": [mec]}
    #r2 = requests.post('http://localhost:8080/stats/flowentry/delete_strict', data=json.dumps(data))
    #r2.status_code

    loadSelectedForwarder(ui.guiCbForwarder.currentText())

def actionPerformedGuiBtnEdit():
    global ui
    print "actionPerformedGuiBtnEdit"
    #/stats/flowentry/modify_strict
    ACL_result = {}
    if ui.guiCbAction.currentText() == 'Permit':
        ACL_result = {"type": "GOTO_TABLE", "table_id": 1}
    else:
        ACL_result = {"type": "DROP"}

    pom = 1
    for i in fwList:
        if i.name == ui.guiCbForwarder.currentText():
            break
        pom += 1
    pom = str(pom)

    data = {"dpid": pom, "priority": str(ui.guiLePriority.text()), "table_id": "0", "match":
            dict(loadUserData(), **{'dl_type': '2048'}), "actions": [ACL_result]}

    r = requests.post('http://localhost:8080/stats/flowentry/modify_strict', data=json.dumps(data))
    r.status_code
    loadSelectedForwarder(ui.guiCbForwarder.currentText())

def loadUserData():     #Loading from TextFields
    ACL_match_data = {}

    if ui.guiLeSrcIp.text():
        ACL_match_data['nw_src'] = str(ui.guiLeSrcIp.text()) + '/' + str(ui.guiLeSrcPrefix.text())

    if ui.guiLeDstIp.text():
        ACL_match_data['nw_dst'] = str(ui.guiLeDstIp.text()) + "/" + str(ui.guiLeDstPrefix.text())

    if ui.guiLeSrcMac.text():
        ACL_match_data['dl_src'] = str(ui.guiLeSrcMac.text())

    if ui.guiLeDstMac.text():
        ACL_match_data['dl_dst'] = str(ui.guiLeDstMac.text())

    if ui.guiLeDstPortNumber.text():
        ACL_match_data['tp_dst'] = str(ui.guiLeDstPortNumber.text())

    if ui.guiLeSrcPortNumber.text():
        ACL_match_data['tp_src'] = str(ui.guiLeSrcPortNumber.text())

    if str(ui.guiCbL4Protocol.currentText()) == 'TCP':
        ACL_match_data['nw_proto'] = 6
    elif str(ui.guiCbL4Protocol.currentText()) == 'UDP':
        ACL_match_data['nw_proto'] = 17
    elif str(ui.guiCbL4Protocol.currentText()) == 'ICMP':
        ACL_match_data['nw_proto'] = 1

    return ACL_match_data

def loadSelectedRowData():     #Loading from TextFields
    ACL_match_data = {}

    #P = ui.guiTblFirewallRules.selectionModel().selectedRows()
    #P = ui.guiTblFirewallRules.itemFromIndex(P[0]).text()

    if ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),4).text():
        ACL_match_data['nw_src'] = str(ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),4).text())

    if ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),5).text():
        ACL_match_data['nw_dst'] = str(ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),5).text())

    if ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),2).text():
        ACL_match_data['dl_src'] = str(ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),2).text())

    if ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),3).text():
        ACL_match_data['dl_dst'] = str(ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),3).text())

    if ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),6).text():
        L4 = str(ui.guiTblFirewallRules.item(ui.guiTblFirewallRules.currentRow(),6).text())
        Protocol, Ports = L4.split(' (')
        SrcPort, DstPort = Ports.split('/')
        DstPort = DstPort.translate(None, ')')

    if SrcPort != 0:
        ACL_match_data['tp_src'] = SrcPort

    if DstPort != 0:
        ACL_match_data['tp_dst'] = DstPort

    if str(Protocol) == 'TCP':
        ACL_match_data['nw_proto'] = 6
    elif str(Protocol) == 'UDP':
        ACL_match_data['nw_proto'] = 17
    elif str(Protocol) == 'ICMP':
        ACL_match_data['nw_proto'] = 1

    return ACL_match_data

def actionPerformedGuiBtnCreate():
    global ui
    print "actionPerformedGuiBtnCreate"

    # POST FOR SPECIFIC ENTRY
    #DPID refers to (switchID + 1)

    #TODO interface and direction NOT included yet

    #interface = str(ui.guiCbInterface.currentText())
    #direction = str(ui.guiCbDirection.currentText())

    ACL_result = {}
    if ui.guiCbAction.currentText() == 'Permit':
        ACL_result = {"type": "GOTO_TABLE", "table_id": 1}
    else:
        ACL_result = {"type": "DROP"}

    pom = 1
    for i in fwList:
        if i.name == ui.guiCbForwarder.currentText():
            break
        pom += 1
    pom = str(pom)

    data = {"dpid": pom, "priority": str(ui.guiLePriority.text()), "table_id": "0", "match":
            dict(loadUserData(), **{'dl_type': '2048'}), "actions": [ACL_result]}

    r = requests.post('http://localhost:8080/stats/flowentry/add', data=json.dumps(data))
    r.status_code
    loadSelectedForwarder(ui.guiCbForwarder.currentText())

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
        self.guiBtnEdit.clicked.connect(actionPerformedGuiBtnEdit)
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
    #testFunctionForFW()
    loadSelectedForwarder(ui.guiCbForwarder.currentText())

    sys.exit(app.exec_())



