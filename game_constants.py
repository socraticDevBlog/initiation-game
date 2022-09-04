from enum import Enum
from pstats import Stats


class Status(Enum):
    INTRO = 1
    RISE = 2
    CLIMAX = 3
    FALL = 4
    CATASTROPHE = 5


class Consequence(Enum):
    NEWBORN = 0
    SURVIVE = 1
    THRIVE = 2
    DIE = 3
