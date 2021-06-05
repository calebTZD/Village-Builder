from Defaults import Defaults
from random import shuffle

class PriorityClass:
    def __init__(self):
        self.rotationPriorities = {}

    def getRandomPriority(self, village):
        priorityList = list(village.priorities.keys())
        shuffle(priorityList)
        return priorityList

    def getRotationPriority(self, village):
        if not village.name in self.rotationPriorities:
            tempPriorities = dict(village.priorities)
            tempPriorities = {k: v for k, v in sorted(tempPriorities.items(), key=lambda item: item[1], reverse=True)}
            self.rotationPriorities[village.name] = list(tempPriorities.keys())            
        else:
            self.rotationPriorities[village.name].append(self.rotationPriorities[village.name].pop(0))
        return self.rotationPriorities[village.name] 

if __name__ == '__main__':
    from pprint import pprint 
    from Village import VillageClass  
    P = PriorityClass()
    villageSettings = Defaults.simulation["villages"][0]
    village = VillageClass(villageSettings)
    print(village.priorities)
    print(P.getRandomPriority(village))
    print(P.getRandomPriority(village))
    print(P.getRotationPriority(village))
    print(P.getRotationPriority(village))
    print(P.getRotationPriority(village))
    print(P.getRotationPriority(village))