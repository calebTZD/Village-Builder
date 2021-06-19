import initDB
from SimRunner import SimRunnerClass
from SimData import SimData
if __name__ == '__main__':
    from pprint import pprint
    initDB.initSimulationsCollection()
    initDB.initVillagesCollection()
    initDB.addSampleData()
    simRunner = SimRunnerClass("The Myst")
    sim = simRunner.sim
    #pprint(sim.__dict__)
    pprint(sim.toDict())
    # stats = VillagerStatsClass(sim.world.villages[0].villagers[0])
    # pprint(stats.statDict())
    pprint(SimData.getStatsByName("The Myst"))