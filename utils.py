from enum import Enum

class GameState(Enum):
    PRE_FLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
 
class Action(Enum):
    FOLD = -1
    CHECK = 0
    BET = 1
    
