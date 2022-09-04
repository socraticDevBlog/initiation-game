from state_model import State_model
from game_constants import Consequence, Status


title = """
   _        _  __   _        __   _                 
  (_)___   (_)/ /_ (_)___ _ / /_ (_)___   ___       
 / // _ \ / // __// // _ `// __// // _ \ / _ \      
/_//_//_//_/ \__//_/ \_,_/ \__//_/ \___//_//_/  ___ 
  ___ _ ___ _ __ _  ___  ____ |_  |/ _ \ |_  | |_  |
 / _ `// _ `//  ' \/ -_)/___// __// // // __/ / __/ 
 \_, / \_,_//_/_/_/\__/     /____/\___//____//____/ 
/___/                                               
                    
"""


def entry_point():
    print("enter your game token to resume a game")
    print("for a new game, just press Return")
    token = input("")

    game_state = State_model(token)
    print("The game is getting activated.")
    print(f"Always keep this token handy. Copy it to your clipboard: \n")
    print(game_state.token)
    print("\n")
    print("GAME IS BEGINNING NOW!!")
    handler(game_state)


def handler(state):
    print("handler function here")
    print("This proves fetching Game status from database works:")
    print(Status(state.get_status()))
    print("This proves fetching Game consequence from database workds")
    print(Consequence(state.get_consequence()))


def main():
    print(title)
    r = input("Want to play Initiation_game?: y/n \n")

    if r.lower() == "y":
        entry_point()
    elif r.lower() == "n":
        print("see you later!!")
    else:
        print("invalid input. Enter letter 'y' to start a new game. Bye!")


if __name__ == "__main__":
    main()
else:
    print("not main...")
