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

import db


def entry_point():
    print("enter your game token to resume a game")
    print("for a new game, just press Return")
    r = input("")

    if r != "":
        handler(r)
    else:
        token = new_game()
        handler(token)


def handler(token):
    print("The game is getting activated.")
    print(f"Always keep this token handy. Copy it to your clipboard: \n")
    print(token)


def new_game():
    print("omg! you want to play a new game of the initiation_game 2022!")
    print("Hope you will enjoy the experience")
    return db.new_game_token()


def main():
    print(title)
    r = input("Want to play Initiation_game?: y/n \n")

    if r == "y":
        entry_point()
    elif r == "n":
        print("see you later!!")
    else:
        print("invalid input. Enter letter 'y' to start a new game. Bye!")


if __name__ == "__main__":
    main()
else:
    print("not main...")
