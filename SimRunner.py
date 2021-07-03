import random
from util import LOGIT, L_Type
from SimData import SimData
from Defaults import Defaults
from Simulation import SimulationClass
from Building import BuildingClass #TODO Add build to village
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
            # print(villager.village.name + ": " + villager.type)
            self.takeAction(villager)

    def takeAction(self, villager):
        if villager.status == V_Status.UNASSIGNED:
            if villager.findBuilding():
                villager.status = V_Status.TO_LOCATION
            elif villager.village.canBuild(villager.preferredBuilding):
                villager.village.addBuilding(villager.preferredBuilding) 
                               

        elif villager.status == V_Status.HARVESTING:
            villager.harvest()
            if villager.currentLoad[villager.gatheringType] >= villager.carryCapacity:
                villager.setToVillage()

        elif villager.status == V_Status.BUILDING:
            villager.assignedBuilding.buildTimeLeft -= 1
            if villager.assignedBuilding.buildTimeLeft <= 0:
                if villager.type == "Guard" or villager.type == "Warrior":
                    villager.status = V_Status.DEFENDING
                elif villager.type == "Scout":
                    villager.status = V_Status.SEARCHING
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
                if villager.village.searchPriority == "enemy":
                    enemies = list(self.sim.world.villages)
                    random.shuffle(enemies)
                    enemy = enemies[0]
                    villager.village.addEnemy(enemy)
                elif villager.village.searchPriority == "locations":
                    villager.village.searchPriority = "enemy"
                    for lType in L_Type:
                        villager.village.addLocation(lType.value)

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
            self.sendArmy(village)
            self.defendVillage(village)             

    def createVillager(self, village):
        villagerType = self.priorityManager.whichVillagerToCreate(village)
        if village.canCreate(self.sim.config.villagers[villagerType]["spawnCost"]):
            village.addVillager(villagerType)
            LOGIT.info(village.name + " Created " + villagerType)
            village.spend(self.sim.config.villagers[villagerType]["spawnCost"])

    def reassignVillagers(self, village):
        for x in range(3):
            (topValue, topPriority, bottomPriority) = self.priorityManager.whichVillagerToSwitch(village)
            if topPriority == bottomPriority or bottomPriority == None or topValue <= 10:
                return
            else:
                LOGIT.info(village.name + " Reassign " + bottomPriority + " To " + topPriority)
                village.switchVillagers(topPriority, bottomPriority)

    def sendArmy(self, village):        
        if not village.attacking():
            warriors = village.getVillagersByType("Warrior")
            if len(warriors) >= 15:
                LOGIT.info("TO WAR")
                village.stats.timesToWar += 1
                for warrior in warriors:
                    warrior.status = V_Status.TO_WAR
                    warrior.findTarget()
                    warrior.distance = self.sim.config.world["distanceBetweenVillages"]

    def defendVillage(self, village):
        if village.attacking:
            guards = village.getVillagersByType("Guard")
            building = village.underAttack()
            if building and len(building.enemies) > len(guards):
                village.stats.timesAttacked += 1
                for warrior in village.getVillagersByType("Warrior"):
                    warrior.assignedBuilding = building
                    warrior.status = V_Status.DEFENDING

    def upgrade(self, village):        
        priotiryVillager = self.priorityManager.whichVillagerToUpgrade(village)
        if village.resources["Research"] >= self.sim.config.villagers[priotiryVillager]["enhancemntCost"]:
            village.levelMod[priotiryVillager] +=1
            village.resources["Research"] -= self.sim.config.villagers[priotiryVillager]["enhancemntCost"]
            # LOGIT.info(village.name + " upgraded " + priotiryVillager)

        if village.resources["ProjectX"] >= self.sim.config.villagers["DrX"]["enhancemntCost"]:
            village.levelMod["Guard"] +=1
            village.levelMod["Warrior"] +=1
            village.resources["ProjectX"] -= self.sim.config.villagers["DrX"]["enhancemntCost"]
            # LOGIT.info(village.name + " upgraded Guard and Warrior")

    def runSimulation(self):
        tick = 0
        while tick < self.sim.world.days * 10:
            self.doTick()
            self.postTick()
            if tick % 10 == 0:
                self.sim.stats.doTickStats()
            tick += 1
            self.sim.stats.ticks += 1
            LOGIT.info(f'Tick number: {tick}')
        SimData.saveStats(self.sim.toDict())
        return True