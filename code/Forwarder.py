class Forwarder:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.acl = []

    def printState(self):
        print "Class state"

    def addRuleToAcl(self,rule):
        self.acl.append(rule)

    def printAclRules(self):
        for i in self.acl:
            print "aclRule: "+i.action
