import unittest
import initDB
from SimRunner import SimRunnerClass
from pprint import pprint
from util import *

class TestTakeAction(unittest.TestCase):
    def setUp(self):
        initDB.initSimulationsCollection()
        initDB.initVillagesCollection()
        initDB.addSampleData()
        self.simRunner = SimRunnerClass("The Myst")
        self.villager = self.simRunner.sim.world.villages[0].villagers[0]

    def test_Unassigned(self):
        pprint(self.villager.status)
        self.assertEqual(self.villager.status, V_Status.UNASSIGNED)
        self.simRunner.takeAction(self.villager)
        self.assertEqual(self.villager.status, V_Status.TO_LOCATION)
        self.assertIsNotNone(self.villager.assignedBuilding)
        pprint(self.villager.status)



if __name__ == '__main__':
    unittest.main()