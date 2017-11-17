class Acl:

    def __init__(self, ip, action):
        self.ip = ip
        self.action = action

    def printState(self):
        print "IP: "+self.ip+" Action:"+self.action

