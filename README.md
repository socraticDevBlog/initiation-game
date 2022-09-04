```
   _        _  __   _        __   _                 
  (_)___   (_)/ /_ (_)___ _ / /_ (_)___   ___       
 / // _ \ / // __// // _ `// __// // _ \ / _ \      
/_//_//_//_/ \__//_/ \_,_/ \__//_/ \___//_//_/  ___ 
  ___ _ ___ _ __ _  ___  ____ |_  |/ _ \ |_  | |_  |
 / _ `// _ `//  ' \/ -_)/___// __// // // __/ / __/ 
 \_, / \_,_//_/_/_/\__/     /____/\___//____//____/ 
/___/                                               
         
```

# initiation-game

You step into a room. Prepare to die or be reborn.

initiation-game is a one-room dungeon-style game.

### game fondamentals

#### token

A unique identifier token is generated for each new game. Game-client will have
to provide token for each API calls (except "new game").

Game uses this token to locate player's Status, Consequence to last action, and score.

#### Status

Game status is stored in database as an Integer. In game runtime it is mapped
to an enum-like datastructure.

Status is a chronological index of where the player is in the game. It has been
copied from the archetypal [narrative
structure](https://www.wikiwand.com/en/Narrative_structure).

```
class Status(Enum):
    INTRO = 1, "introduction"
    RISE = 2, "rising action"
    CLIMAX = 3, "climax"
    FALL = 4, "return"
    CATASTROPHE = 5, "end of game"
```

#### Consequence

Consequence is a finite set of consequences the player experiences now from
previous action/decision. It helps the game to feel like it has a flow.

```
class Consequence(Enum):
    NEWBORN = 0, "You are pure like a newborn"
    SURVIVE = 1, "You survived previous action"
    THRIVE = 2, "You have conquered!"
    DIE = 3, "Basically you are dead now. Game over."
```


