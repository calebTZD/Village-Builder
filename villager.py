class villager:
    def __init__(self, tpe = None, wHr = 2):
        self.type = tpe
        self.wHr = wHr

    def getWhr(self):
        return self.wHr

    def setType(self, tpe):
        self.type = tpe