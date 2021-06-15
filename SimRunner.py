import random
from SimData import SimData
from Defaults import Defaults
from Simulation import SimulationClass
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass
from Priority import Priority

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
            if villager.findBuilding():
                villager.status = V_Status.TO_LOCATION
            elif villager.village.canBuild(villager.preferredBuilding):
                building = BuildingClass(villager.preferredBuilding, self.sim.config['buildings'][villager.preferredBuilding])
                villager.build(building)
                villager.status = V_Status.TO_LOCATION

        elif villager.status == V_Status.HARVESTING:
            villager.harvest()
            if villager.currentLoad[villager.gatheringType] >= villager.carryCapacity:
                villager.setToVillage()

        elif villager.status == V_Status.BUILDING:
            villager.assignedBuilding.buildTimeLeft -= 1
            if villager.assignedBuilding.buildTimeLeft <= 0:
                if villager.type == "Guard" or villager.type == "Warrior":
                    villager.status = V_Status.DEFENDING
                else:
                    villager.status = V_Status.HARVESTING

        elif villager.status == V_Status.TO_LOCATION:
            villager.toLocation()
        
        elif villager.status == V_Status.TO_VILLAGE:
            villager.toVillage()

        elif villager.status == V_Status.ATTACKING:
            villager.attacking()
            if villager.assignedBuilding.currentHealth <= 0:
                villager.status = V_Status.TO_WAR

        elif villager.status == V_Status.SEARCHING:
            if villager.search():
                villager.status = V_Status.TO_VILLAGE
                enemies = list(self.sim.world.villages)
                random.shuffle(enemies)
                enemy = enemies[0]
                villager.village.addEnemy(enemy)

        elif villager.status == V_Status.TO_WAR:
            if villager.assignedBuilding.currentHealth <= 0 and villager.assignedBuilding.type != "Barracks":
                villager.findTarget()

            villager.toWar()
            if villager.distance <= 0:
                villager.assignedBuilding.enemies.append(villager)
                villager.status = V_Status.ATTACKING

        elif villager.status == V_Status.DEFENDING:
            building = villager.underAttack()
            if building:
                if villager.assignedBuilding.type == "Barracks":
                    villager.assignedBuilding = building
                    villager.distance = building.location.distance
                else:
                    villager.defending()

    def postTick(self):
        for village in self.sim.world.villages:
            self.createVillager(village)
            self.reassignVillagers(village)
            self.createVillager(village)

    def createVillager(self):
        pass #TODO

    def reassignVillagers(self):
        pass #TODO Until worst priority < threashold, convert villagers

    def sendArmy(self):
        pass #TODO ifmilitary > minAttack create Military based on attach%

    def defendVillage(self):
        pass #TODO if enemies>guards call back army and convert towns folk

    def upgrade(self):
        pass #TODO If research or ProjectX > threashold upgrade entitites

    def runSimulation(self):
        tick = 0
        while tick < self.sim.world.days:
            self.doTick()
            self.postTick()
            tick += 1

if __name__ == '__main__':
    sr = SimRunnerClass("The Myst")
    sr.runSimulation()