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

game_over = """
                                                         
   _________    _____   ____     _______  __ ___________ 
  / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ >
 / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
 \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
/_____/     \/      \/     \/                   \/       


"""

from state_model import State_model
from game_constants import Consequence, Status
from logic import turn
import os, argparse


def clear():
    """
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    """
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")


def main(token):
    print(title)

    state = State_model(token)

    while True:
        clear()
        if state.is_game_over():
            print(game_over)
            break

        turn(state)
        _ = input("")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token",
        type=str,
        help="An optional existing game token can be given to resume an existing game",
    )
    args = parser.parse_args()
    token = args.token if args.token != None else ""
    main(token)
else:
    print("not main...")
