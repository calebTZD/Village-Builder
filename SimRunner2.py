import random
from SimData import SimData
from Defaults import Defaults
from Simulation import SimulationClass
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass

from util import V_Status


class SimRunnerClass:
    def __init__(self, name):
        self.villagerList = []
        self.sim = SimulationClass(name)

    def randomizeVillagers(self):
        self.villagerList = []
        for village in self.sim.world.villages:
            self.villagerList.extend(village.villagers)
        
        random.shuffle(self.villagerList)

    def doTick(self):
        self.randomizeVillagers()

        for villager in self.villagerList:
            print(villager.village.name + ": " + villager.type)
            #self.takeAction(villager)

    def takeAction(self, villager):
        if villager.status == V_Status.UNASSIGNED:
            villager.findBuilding()
            villager.status = V_Status.TO_LOCATION
        if villager.status == V_Status.HARVESTING:
            villager.currentLoad[villager.gatheringType] += villager.producionSpeed        

        if villager.status == V_Status.BUILDING:
            pass

        elif villager.status == V_Status.TO_LOCATION:
            villager.distance -= villager.speed
            #TODO: if there change to harvesting or whatever
        
        elif villager.status == V_Status.TO_VILLAGE:
            villager.distance -= villager.speed
            #TODO: if there return resources and move to unassigned

        elif villager.status == V_Status.ATTACKING:
            pass 

        elif villager.status == V_Status.SEARCHING:
            pass

    def postTick(self):
        for village in self.sim.world.villages:
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
        while tick < self.sim.world.days:
            self.doTick()
            self.postTick()
            tick += 1

if __name__ == '__main__':
    sr = SimRunnerClass("The Myst")
    sr.runSimulation()