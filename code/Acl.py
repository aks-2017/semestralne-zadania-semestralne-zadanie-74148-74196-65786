class Acl:

    def __init__(self, ip, action, id, srcMac, dstMac, srcIp, dstIp, srcPrefix, dstPrefix, l4Protocol, interface, direction ):
        self.action = action
        self.id = id
        self.action = action
        self.id = id
        self.srcMac = srcMac
        self.dstMac = dstMac
        self.srcIp = srcIp
        self.dstIp = dstIp
        self.srcPrefix = srcPrefix
        self.dstPrefix = dstPrefix
        self.l4Protocol = l4Protocol
        self.interface = interface
        self.direction = direction

    def printState(self):
        print "state"

