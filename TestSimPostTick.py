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
        #self.village.buildings = []
        self.village.addVillager( VillagerClass(V_Type.FARMER.value, self.sim.config["villagers"][V_Type.FARMER.value]))
        self.village.addVillager( VillagerClass(V_Type.HUNTER.value, self.sim.config["villagers"][V_Type.HUNTER.value]))
        self.village.addVillager( VillagerClass(V_Type.LUMBERJACK.value, self.sim.config["villagers"][V_Type.LUMBERJACK.value]))
        self.village.addVillager( VillagerClass(V_Type.MINER.value, self.sim.config["villagers"][V_Type.MINER.value]))
        self.village.addVillager( VillagerClass(V_Type.STONEMASON.value, self.sim.config["villagers"][V_Type.STONEMASON.value]))
        self.village.addVillager( VillagerClass(V_Type.WARRIOR.value, self.sim.config["villagers"][V_Type.WARRIOR.value]))
        self.village.addVillager( VillagerClass(V_Type.GUARD.value, self.sim.config["villagers"][V_Type.GUARD.value]))
        self.village.addVillager( VillagerClass(V_Type.MERCHANT.value, self.sim.config["villagers"][V_Type.MERCHANT.value]))
        self.village.addVillager( VillagerClass(V_Type.SCOUT.value, self.sim.config["villagers"][V_Type.SCOUT.value]))
        self.village.addVillager( VillagerClass(V_Type.RESEARCHER.value, self.sim.config["villagers"][V_Type.RESEARCHER.value]))
   

        self.village.priorities = {
            "Food": 10,
            "Wood": 10,
            "Stone": 10,
            "Ore": 10,
            "Gold": 10,
            "Attack": 10,
            "Defense": 10,
            "Research": 10,
            "Exploring": 10
        } 

        self.village.resources = {
            "Food": 200,
            "Wood": 100,
            "Stone": 100,
            "Ore": 100,
            "Gold": 100,
            "Research": 100
        }

        curentPriorities = Priority.calcPriorities(self.village)
        print(curentPriorities)
        Priority.normalizePriorities(curentPriorities)
        print(curentPriorities)   
        diff = Priority.calcDifference(curentPriorities, self.village.priorities)
        print(diff)
        diff = Priority.calcResourcesDiff(self.village)
        print(diff)



if __name__ == '__main__':
    unittest.main()