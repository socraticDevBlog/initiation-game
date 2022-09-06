from demo import Demo
import random


def turn(state):
    statuses = Demo["status"]
    current_statuses = statuses[state.get_status()]
    texts = current_statuses["text"]
    print(random.choice(texts))
    print("")
    print("Make a choice and press Return")
    options = current_statuses["options"]

    for x in options:
        print(x)

    consequences = current_statuses["consequences"]
    state.update_game(random.choice(consequences))
