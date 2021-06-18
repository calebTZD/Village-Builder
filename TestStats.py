import initDB
from SimRunner import SimRunnerClass
if __name__ == '__main__':
    from pprint import pprint
    initDB.initSimulationsCollection()
    initDB.initVillagesCollection()
    initDB.addSampleData()
    simRunner = SimRunnerClass("The Myst")
    sim = simRunner.sim
    #pprint(sim.__dict__)
    pprint(sim.world.villages[0].toDict())
    # stats = VillagerStatsClass(sim.world.villages[0].villagers[0])
    # pprint(stats.statDict())