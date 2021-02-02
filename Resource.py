class resource:
    def __init__(self, type, rp = 500):
        self.type = type
        self.rPoints = rp

    def reduceRP(self, amount):
        self.rPoints -= amount
        