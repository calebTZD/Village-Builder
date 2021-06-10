import unittest
import initDB
from SimRunner import SimRunnerClass
from Villager import VillagerClass
from pprint import pprint
from util import *

class TestTakeAction(unittest.TestCase):
    def setUp(self):
        initDB.initSimulationsCollection()
        initDB.initVillagesCollection()
        initDB.addSampleData()
        self.simRunner = SimRunnerClass("The Myst")
        self.sim = self.simRunner.sim
        self.village = self.simRunner.sim.world.villages[0]
        self.villager = self.simRunner.sim.world.villages[0].villagers[0]

    def test_Unassigned(self):
        pprint(self.villager.status)
        self.assertEqual(self.villager.status, V_Status.UNASSIGNED)
        self.simRunner.takeAction(self.villager)
        self.assertEqual(self.villager.status, V_Status.TO_LOCATION)
        self.assertIsNotNone(self.villager.assignedBuilding)
        pprint(self.villager.status)

    def test_UnassignedBuild(self):
        pass

    def test_testy(self):
        self.village
        for x in range(20):
            self.village.addVillager( VillagerClass("Warrior", self.sim.config["villagers"]["Warrior"]))
        pprint(self.village.villagers)



if __name__ == '__main__':
    unittest.main()