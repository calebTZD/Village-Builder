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

    def test_priorities(self):
        self.village.villagers = []
        self.sim.createVillager(V_Type.HUNTER.value, self.village)
        self.sim.createVillager(V_Type.LUMBERJACK.value, self.village)
        self.sim.createVillager(V_Type.MINER.value, self.village)
        self.sim.createVillager(V_Type.STONEMASON.value, self.village)
        self.sim.createVillager(V_Type.WARRIOR.value, self.village)
        self.sim.createVillager(V_Type.GUARD.value, self.village)
        self.sim.createVillager(V_Type.MERCHANT.value, self.village)
        self.sim.createVillager(V_Type.SCOUT.value, self.village)
        self.sim.createVillager(V_Type.RESEARCHER.value, self.village)
   
        self.village.buildings = []
        self.sim.createBuilding(B_Type.FARM.value, self.village)
        self.sim.createBuilding(B_Type.LOGGINGCAMP.value, self.village)
        self.sim.createBuilding(B_Type.MINE.value, self.village)
        self.sim.createBuilding(B_Type.QUARRY.value, self.village)
        self.sim.createBuilding(B_Type.BARRACKS.value, self.village)
        self.sim.createBuilding(B_Type.MARKET.value, self.village)
        self.sim.createBuilding(B_Type.LIBRARY.value, self.village)

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

        self.village.resources = {
            "Food": 200,
            "Wood": 100,
            "Stone": 200,
            "Ore": 100,
            "Gold": 200,
            "ProjectX": 200,
            "Research": 100
        }

        diff = Priority.calcPriorities(self.village)
        self.assertEqual(diff['Food'], -7)
        self.assertEqual(diff['Wood'], 2)
        self.assertEqual(diff['Stone'], -7)
        self.assertEqual(diff['Defense'], 9)
        self.assertEqual(diff['ProjectX'], -5)
        self.assertEqual(diff['Research'], 2)



if __name__ == '__main__':
    unittest.main()