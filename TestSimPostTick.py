import unittest
import initDB
from SimRunner import SimRunnerClass
from Villager import VillagerClass
from pprint import pprint
from util import *
from Priority import PriorityManagerClass

class TestTakeAction(unittest.TestCase):
    def setUp(self):
        initDB.initSimulationsCollection()
        initDB.initVillagesCollection()
        initDB.addSampleData()
        self.simRunner = SimRunnerClass("The Myst")
        self.sim = self.simRunner.sim
        self.village = self.simRunner.sim.world.villages[0]
        self.villager = self.simRunner.sim.world.villages[0].villagers[0]

    def init_villagers(self):
        self.village.villagers = []
        self.sim.createVillager(V_Type.FARMER.value, self.village)
        self.sim.createVillager(V_Type.LUMBERJACK.value, self.village)
        self.sim.createVillager(V_Type.MINER.value, self.village)
        self.sim.createVillager(V_Type.STONEMASON.value, self.village)
        self.sim.createVillager(V_Type.WARRIOR.value, self.village)
        self.sim.createVillager(V_Type.GUARD.value, self.village)
        self.sim.createVillager(V_Type.MERCHANT.value, self.village)
        self.sim.createVillager(V_Type.SCOUT.value, self.village)
        self.sim.createVillager(V_Type.RESEARCHER.value, self.village)
        self.sim.createVillager(V_Type.DRX.value, self.village)

    def init_buildings(self):   
        self.village.buildings = []
        self.sim.createBuilding(B_Type.FARM.value, self.village)
        self.sim.createBuilding(B_Type.LOGGINGCAMP.value, self.village)
        self.sim.createBuilding(B_Type.MINE.value, self.village)
        self.sim.createBuilding(B_Type.QUARRY.value, self.village)
        self.sim.createBuilding(B_Type.BARRACKS.value, self.village)
        self.sim.createBuilding(B_Type.MARKET.value, self.village)
        self.sim.createBuilding(B_Type.LIBRARY.value, self.village)
        self.sim.createBuilding(B_Type.BUILDINGX.value, self.village)

    def init_priorities(self):
        self.village.priorities = {
            "Food": 10,
            "Wood": 10,
            "Stone": 10,
            "Ore": 10,
            "Gold": 10,
            "Attack": 10,
            "Defense": 10,
            "Research": 10,
            "ProjectX": 10,
            "Explore": 10
        } 

    def init_resources(self):
        self.village.resources = {
            "Food": 100,
            "Wood": 100,
            "Stone": 100,
            "Ore": 100,
            "Gold": 100,
            "ProjectX": 100,
            "Research": 100
        }

    def test_priorities(self):
        self.init_villagers()
        self.init_buildings()
        self.init_priorities()
        self.init_resources()

        diff = self.simRunner.priorityManager.calcPriorities(self.village)
        vType = self.simRunner.priorityManager.whichVillagerToCreate(self.village)
        (topValue, topType, bottomType) = self.simRunner.priorityManager.whichVillagerToSwitch(self.village)
        self.assertEqual(diff['Food'], 0)
        self.assertEqual(diff['Wood'], 0)
        self.assertEqual(diff['Stone'], 0)
        self.assertEqual(diff['Ore'], 0)
        self.assertEqual(diff['Gold'], 0)
        self.assertEqual(diff['Defense'], 0)
        self.assertEqual(diff['ProjectX'], 0)
        self.assertEqual(diff['Research'], 0)

    def test_nextCreate(self):
        self.init_villagers()
        self.init_buildings()
        self.init_priorities()
        self.init_resources()
        self.village.resources["Food"] += 100
        self.village.resources["Wood"] -= 100

        vType = self.simRunner.priorityManager.whichVillagerToCreate(self.village)
        self.assertEqual(vType, V_Type.LUMBERJACK.value)
        
        (topValue, topType, bottomType) = self.simRunner.priorityManager.whichVillagerToSwitch(self.village)
        self.assertEqual(topType, V_Type.LUMBERJACK.value)
        self.assertEqual(bottomType, V_Type.FARMER.value)

    def test_nextUpgrade(self):
        self.village.levelMod = {
            "Farmer": 3,
            "Lumberjack": 2,
            "Miner": 3,
            "Stonemason": 3,
            "Merchant": 3,
            "Warrior": 4,
            "Guard": 5,
            "Scout": 3,
            "DrX": 0,
            "Researcher": 5
        }
        self.village.priorities['Food'] = 10
        pprint(self.simRunner.priorityManager.whichVillagerToUpgrade(self.village))

    def test_upgrade(self):
        self.village.levelMod = {
            "Farmer": 3,
            "Lumberjack": 2,
            "Miner": 3,
            "Stonemason": 3,
            "Merchant": 3,
            "Warrior": 5,
            "Guard": 6,
            "Scout": 3,
            "DrX": 0,
            "Researcher": 5
        }
        priotiryVillager = self.simRunner.priorityManager.whichVillagerToUpgrade(self.village)
        self.assertEqual(priotiryVillager, V_Type.LUMBERJACK.value)
        self.assertEqual(self.village.levelMod[priotiryVillager], 2)
        self.simRunner.upgrade(self.village)
        self.assertEqual(self.village.levelMod[priotiryVillager], 2)
        self.assertEqual(self.village.levelMod[V_Type.GUARD.value], 6)
        self.assertEqual(self.village.levelMod[V_Type.WARRIOR.value], 5)
        self.village.resources["Research"] = self.sim.config.villagers[priotiryVillager]["enhancemntCost"]
        self.village.resources["ProjectX"] = self.sim.config.villagers[V_Type.DRX.value]["enhancemntCost"]
        self.simRunner.upgrade(self.village)
        self.assertEqual(self.village.levelMod[priotiryVillager], 3)
        self.assertEqual(self.village.levelMod[V_Type.GUARD.value], 7)
        self.assertEqual(self.village.levelMod[V_Type.WARRIOR.value], 6)
        self.assertEqual(self.village.resources["Research"], 0)
        self.assertEqual(self.village.resources["ProjectX"], 0)

    def test_createVillager(self):
        self.init_villagers()
        self.init_buildings()
        self.init_priorities()
        self.init_resources()
        self.village.resources["Food"] += 100
        self.village.resources["Wood"] -= 100
        numLumberjacks = len(self.village.getVillagersByType(V_Type.LUMBERJACK.value))
        self.assertEqual(numLumberjacks, 1)
        self.simRunner.createVillager(self.village)
        numLumberjacks = len(self.village.getVillagersByType(V_Type.LUMBERJACK.value))  
        self.assertEqual(numLumberjacks, 2)


    def test_reassignVillager(self):
        self.init_villagers()
        self.init_buildings()
        self.init_priorities()
        self.init_resources()
        self.village.resources["Food"] += 5
        self.village.resources["Wood"] -= 5
        self.village.resources["Ore"] += 10
        self.village.resources["Gold"] -= 10
        numLumberjacks = len(self.village.getVillagersByType(V_Type.LUMBERJACK.value))
        self.assertEqual(numLumberjacks, 1)
        self.simRunner.createVillager(self.village)
        numLumberjacks = len(self.village.getVillagersByType(V_Type.LUMBERJACK.value))
        self.assertEqual(numLumberjacks, 2)

if __name__ == '__main__':
    unittest.main()