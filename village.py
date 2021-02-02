class village:
    def __init__(self, villagers = 1):
        self.villagers = villagers
        self.wood = 0
        self.stone = 0
        self.food = 0

    def addVillagers(self, villagers):
        self.villagers += villagers

    def addWood(self, rp):
        self.wood += rp

    def addStone(self, rp):
        self.stone += rp

    def addFood(self, rp):
        self.food += rp