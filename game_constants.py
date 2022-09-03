from enum import Enum


class Status(Enum):
    INTRO = 1, "introduction"
    RISE = 2, "rising action"
    CLIMAX = 3, "climax"
    FALL = 4, "return"
    CATASTROPHE = 5, "end of game"


class Consequence(Enum):
    NEWBORN = 0, "You are pure pure like a newborn"
    SURVIVE = 1, "You survived previous action"
    THRIVE = 2, "You have conquered!"
    DIE = 3, "Basically you are dead now. Game over"
