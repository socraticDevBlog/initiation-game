from demo import Demo
import random


def turn_infos(state):
    ret = {}

    statuses = Demo["status"]
    current_statuses = statuses[state.get_status()]

    texts = current_statuses["text"]
    ret.update({"status": random.choice(texts)})

    ret.update({"options": current_statuses["options"]})
    ret.update({"consequences": random.choice(current_statuses["consequences"])})

    return ret


def console_turn(state):
    turn_obj = turn_infos(state)

    print(turn_obj["status"])
    print("")
    print("Make a choice and press Return")

    for x in turn_obj["options"]:
        print(x)

    state.update_game(turn_obj["consequences"])
