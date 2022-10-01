from demo import Demo
import random


def turn_infos(state):
    """
    returns all the text necessary for a turn

    @parameter: state - state model object of the current game. contains all
    current state informations
    """
    ret = {}

    statuses = Demo["status"]
    current_statuses = statuses[state.get_status()]

    texts = current_statuses["text"]
    ret.update({"status": random.choice(texts)})

    ret.update({"options": current_statuses["options"]})
    ret.update({"consequences": random.choice(current_statuses["consequences"])})

    return ret


def console_turn(state):
    """
    procedures that prints a turn's text when game is played in console-mode

    @parameter: state - state model object of the current game. contains all
    current state informations
    """

    turn_obj = turn_infos(state)

    print(turn_obj["status"])
    print("")
    print("Make a choice and press Return")

    for x in turn_obj["options"]:
        print(x)

    state.update_game(turn_obj["consequences"])
