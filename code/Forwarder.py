class Forwarder:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.acl = []

    def printState(self):
        print "Class state"