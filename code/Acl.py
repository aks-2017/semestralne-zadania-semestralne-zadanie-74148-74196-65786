class Acl:

    def __init__(self, ip, action, id, srcMac, dstMac,srcIp, dstIp, l4Protocol, interface, direction ):
        self.action = action
        self.id = id
        self.action = action
        self.id = id
        self.srcMac = srcMac
        self.dstMac = srcIp
        self.dstIp = dstIp
        self.l4Protocol = l4Protocol
        self.interface = interface
        self.direction = direction

    def printState(self):
        print "state"

