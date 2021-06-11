import unittest
import initDB
from SimRunner2 import SimRunnerClass
from Villager import VillagerClass
from pprint import pprint
from util import *
from Priority import Priority

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
            "Exploring": 10
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

        print(self.village.priorities)
        diff = Priority.calcPriorities(self.village)
        print(diff)
        vType = Priority.whichVillagerToCreate(self.village)
        print(vType)
        (topValue, topType, bottomType) = Priority.whichVillagerToSwitch(self.village)
        print("Replace " + bottomType + " with " + topType + " Because it is "+ str(topValue))
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

        vType = Priority.whichVillagerToCreate(self.village)
        self.assertEqual(vType, V_Type.LUMBERJACK.value)
        
        (topValue, topType, bottomType) = Priority.whichVillagerToSwitch(self.village)
        self.assertEqual(topType, V_Type.LUMBERJACK.value)
        self.assertEqual(bottomType, V_Type.FARMER.value)

if __name__ == '__main__':
    unittest.main()