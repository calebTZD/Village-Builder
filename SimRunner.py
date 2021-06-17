import random
from SimData import SimData
from Defaults import Defaults
from Simulation import SimulationClass
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass
from Priority import PriorityManagerClass

from util import V_Status


class SimRunnerClass:
    def __init__(self, name):
        self.villagerList = []
        self.sim = SimulationClass(name)
        self.priorityManager = PriorityManagerClass()
        self.threshholds = []

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
            building = villager.village.underAttack()
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
            self.upgrade(village)
            warriors = []
            if not village.attacking():
                for villager in village.villagers:
                    if villager.type == "Warrior":
                        warriors.append(villager)

                if len(warriors) >= 15:
                    village.status = V_Status.ATTACKING
                    self.sendArmy(warriors)

    def createVillager(self, village):
        villager = self.priorityManager.whichVillagerToCreate(village)
        if village.canCreate(self.sim.config.villagers[villager]["spawnCost"]):
            self.sim.createVillager(villager, village)
            village.create(self.sim.config.villagers[villager]["spawnCost"])
        

    def reassignVillagers(self, village):
        for x in range(3):
            (topValue, topPriority, bottomPriority) = self.priorityManager.whichVillagerToCreate(village)
            if topValue <= 10:
                return
            else:
                village.switchVillagers(topPriority, bottomPriority)


    def sendArmy(self, warriors):

        for warrior in warriors:
            warrior.status = V_Status.TO_WAR
            warrior.distance = self.sim.config.world["distanceBetweenVillages"]


    def defendVillage(self):
        pass #TODO if enemies>guards call back army and convert towns folk

    def upgrade(self, village):
        
        priotiryVillager = self.priorityManager.whichVillagerToUpgrade(village)
        if village.resources["Research"] >= self.sim.config.villagers[priotiryVillager]["enhancemntCost"]:
            village.levelMod[priotiryVillager] +=1
            village.resources["Research"] -= self.sim.config.villagers[priotiryVillager]["enhancemntCost"]

        if village.resources["ProjectX"] >= self.sim.config.villagers["MrX"]["enhancemntCost"]:
            village.levelMod["Guard"] +=1
            village.levelMod["Warrior"] +=1
            village.resources["ProjectX"] -= self.sim.config.villagers["MrX"]["enhancemntCost"]
        

    def runSimulation(self):
        tick = 0
        while tick < self.sim.world.days:
            self.doTick()
            self.postTick()
            tick += 1

if __name__ == '__main__':
    sr = SimRunnerClass("The Myst")
    sr.runSimulation()