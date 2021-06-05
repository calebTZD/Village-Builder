import random
from SimData import SimData
from Defaults import Defaults

class SimulationClass:
    def __init__(self, name):
        self.villagerlist = []
        self.world = SimData.getSimByName(name)


    def getVillagers(self):
        for village in self.world.villages:
            for villager in village:
                self.villagerlist += villager
        
        random.shuffle(self.villagerlist)


Simulation = SimulationClass(Defaults.simulation.name)

if __name__ == '__main__':
    tick = 0
    tickMax = 10

    while tick < tickMax:
        Simulation.getVillagers()

        for villager in Simulation.villagerlist:
            if villager.status == "gathering":
                villager.currentLoad[villager.gatheringType] += villager.producionSpeed

            elif villager.status == "traveling to village":
                villager.distance -= 1

            elif villager.status == "attacking":
                pass 

            elif villager.status == "searching":
                pass