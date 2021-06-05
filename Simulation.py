import random
from SimData import SimData
from Defaults import Defaults
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass

class SimulationClass:
    def __init__(self, name):
        self.villagerList = []
        self.world = WorldClass(SimData.getWorld(name))

    def getVillagers(self):
        self.villagerList = []
        for village in self.world.villages:
            for villager in village:
                self.villagerList += villager
        
        random.shuffle(self.villagerList)

    def doTick(self):
        self.getVillagers()

        for villager in self.villagerList:
            self.takeAction(villager)

    def takeAction(self, villager):
        if villager.status == "gathering":
            villager.currentLoad[villager.gatheringType] += villager.producionSpeed

        elif villager.status == "traveling to village":
            villager.distance -= villager.speed

        elif villager.status == "traveling to building":
            villager.distance -= villager.speed

        elif villager.status == "attacking":
            pass 

        elif villager.status == "searching":
            pass

    def postTick(self):
        for village in self.world.villages:
            pass

    def upgrade(self):
        pass #TODO

    def build(self):
        pass #TODO

    def createVillager(self):
        pass #TODO

    def reassignVillager(self):
        pass #TODO

    def sendArmy(self):
        pass #TODO

    def runSimulation(self):
        tick = 0
        while tick < self.world.days:
            self.doTick()
            self.postTick()

if __name__ == '__main__':
    pass