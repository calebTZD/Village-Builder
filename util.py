from enum import Enum
class V_Status(Enum):
    UNASSIGNED = 1
    TO_LOCATION = 2    
    BUILDING = 3
    HARVESTING = 4
    TO_VILLAGE = 5
    ATTACKING = 6
    SEARCHING = 7