from re import A
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

    # def test_Unassigned(self):
    #     pprint(self.villager.status)
    #     self.assertEqual(self.villager.status, V_Status.UNASSIGNED)
    #     self.simRunner.takeAction(self.villager)
    #     self.assertEqual(self.villager.status, V_Status.TO_LOCATION)
    #     self.assertIsNotNone(self.villager.assignedBuilding)
    #     pprint(self.villager.status)

    # def test_UnassignedBuild(self):
    #     self.village.buildings = []
    #     self.village.resources = {
    #         "Food": 500,
    #         "Wood": 500,
    #         "Stone": 500,
    #         "Ore": 500,
    #         "Gold": 500,
    #         "Research": 500
    #     }
    #     pprint(self.village.buildings)
    #     pprint(self.villager.status)
    #     self.assertEqual(self.villager.status, V_Status.UNASSIGNED)
    #     self.simRunner.takeAction(self.villager)
    #     self.assertEqual(self.villager.status, V_Status.TO_LOCATION)
    #     self.assertIsNotNone(self.villager.assignedBuilding)
    #     pprint(self.villager.status)
    #     pprint(self.village.buildings)

    # def test_Harvesting(self):
    #     self.simRunner.takeAction(self.villager)
    #     self.villager.status = V_Status.HARVESTING
    #     pprint(self.villager.currentLoad)
    #     self.simRunner.takeAction(self.villager)
    #     self.assertEqual(self.villager.currentLoad["Food"], self.villager.productionSpeed)
    #     pprint(self.villager.currentLoad)
    #     pprint(self.village.resources)

    # def test_Building(self):
    #     self.village.buildings = []
    #     self.village.resources = {
    #         "Food": 500,
    #         "Wood": 500,
    #         "Stone": 500,
    #         "Ore": 500,
    #         "Gold": 500,
    #         "Research": 500
    #     }
    #     self.assertEqual(self.villager.status, V_Status.UNASSIGNED)
    #     self.simRunner.takeAction(self.villager)
    #     self.villager.status = V_Status.BUILDING
    #     self.assertIsNotNone(self.villager.assignedBuilding)
    #     pprint(self.villager.assignedBuilding.buildTimeLeft)
    #     self.simRunner.takeAction(self.villager)
    #     pprint(self.villager.assignedBuilding.buildTimeLeft)

    # def test_toLocation(self):
    #     pprint(self.villager.status)
    #     self.simRunner.takeAction(self.villager)
    #     self.assertEqual(self.villager.status, V_Status.TO_LOCATION)
    #     pprint(self.villager.distance)
    #     self.simRunner.takeAction(self.villager)
    #     pprint(self.villager.distance)
    #     pprint(self.villager.assignedBuilding.buildTimeLeft)
    #     pprint(self.villager.status)

    # def test_toVillage(self):
    #     self.simRunner.takeAction(self.villager)
    #     self.villager.currentLoad["Food"] = 50
    #     self.villager.status = V_Status.HARVESTING
    #     self.simRunner.takeAction(self.villager)
    #     self.assertEqual(self.villager.status, V_Status.TO_VILLAGE)
    #     pprint(self.villager.distance)
    #     self.simRunner.takeAction(self.villager)
    #     self.assertEqual(self.villager.status, V_Status.TO_LOCATION)

    # def test_attacking(self):
    #     villager = VillagerClass("Warrior", self.simRunner.sim.config["villagers"]["Warrior"])
    #     self.village.addVillager(villager)
    #     villager.status = V_Status.SEARCHING
    #     villager.distance = 50
    #     self.simRunner.takeAction(villager)
    #     villager.findTarget()
    #     villager.status = V_Status.TO_WAR
    #     self.simRunner.takeAction(villager)
    #     pprint(villager.status)
    #     self.simRunner.takeAction(villager)
    #     pprint(villager.assignedBuilding.currentHealth)
    #     villager.assignedBuilding.assignVillager(self.villager)
    #     self.simRunner.takeAction(villager)
    #     for v in villager.assignedBuilding.villagers:
    #         pprint(v.currentHealth)

    # def test_toWar(self):
    #     self.village.resources = {
    #         "Food": 500,
    #         "Wood": 500,
    #         "Stone": 500,
    #         "Ore": 500,
    #         "Gold": 500,
    #         "Research": 500
    #     }
    #     villager = VillagerClass("Warrior", self.simRunner.sim.config["villagers"]["Warrior"])
    #     self.village.addVillager(villager)
    #     self.simRunner.takeAction(villager)
    #     pprint(villager.assignedBuilding)
    #     villager.status = V_Status.SEARCHING
    #     villager.distance = 50
    #     self.simRunner.takeAction(villager)
    #     villager.status = V_Status.TO_WAR
    #     self.simRunner.takeAction(villager)

    def test_defense(self):
        self.village.addVillager(V_Type.GUARD.value)
        self.village.addBuilding(B_Type.BARRACKS.value)
        for building in self.village.buildings:
            building.buildTimeLeft = 0
        villager = self.village.getVillagersByType(V_Type.GUARD.value)[0]
        self.simRunner.takeAction(villager)
        self.simRunner.takeAction(villager)
        self.assertEqual(villager.status, V_Status.DEFENDING)
        target = self.village.buildings[0]
        attackingVillage = self.simRunner.sim.world.villages[1]
        attackingVillage.addVillager(V_Type.WARRIOR.value)
        attacker = attackingVillage.getVillagersByType(V_Type.WARRIOR.value)[0]
        target.enemies.append(attacker)
        self.assertEqual(target.enemyPresent(), True)
        self.simRunner.takeAction(villager)
        self.simRunner.takeAction(villager)
        

if __name__ == '__main__':
    unittest.main()