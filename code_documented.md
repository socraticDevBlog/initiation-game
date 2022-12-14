not main...
Table is Ready
---
description: |
    API documentation for modules: initiation-game, initiation-game.console_game, initiation-game.db, initiation-game.demo, initiation-game.game_constants, initiation-game.logic, initiation-game.scripts, initiation-game.scripts.game_state, initiation-game.state_model.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...


    
# Namespace `initiation-game` {#id}




    
## Sub-modules

* [initiation-game.console_game](#initiation-game.console_game)
* [initiation-game.db](#initiation-game.db)
* [initiation-game.demo](#initiation-game.demo)
* [initiation-game.game_constants](#initiation-game.game_constants)
* [initiation-game.logic](#initiation-game.logic)
* [initiation-game.scripts](#initiation-game.scripts)
* [initiation-game.state_model](#initiation-game.state_model)






    
# Module `initiation-game.console_game` {#id}






    
## Functions


    
### Function `clear` {#id}




>     def clear()


Clears the terminal screen and scroll back to present
the user with a nice clean, new screen. Useful for managing
menu screens in terminal applications.

    
### Function `main` {#id}




>     def main(
>         token
>     )


entry point to the game.

contains game loop

@param: token - user can provide a token referencing an existing game. this
token is a unique identifier used to fetch a specifc game record from database.




    
# Module `initiation-game.db` {#id}





    
## Variables


    
### Variable `DB_PATH` {#id}




Path to database file.
Before executing game the first time, create a new datafile by executing
scripts/game_state.py script


    
## Functions


    
### Function `get_consequence_by` {#id}




>     def get_consequence_by(
>         token
>     )


retrieve Consequence enum index from database

    
### Function `get_score_by` {#id}




>     def get_score_by(
>         token
>     )




    
### Function `get_status_by` {#id}




>     def get_status_by(
>         token
>     )


retrieve Status enum index from database

    
### Function `increment_score` {#id}




>     def increment_score(
>         token,
>         val
>     )




    
### Function `new_game_token` {#id}




>     def new_game_token()


function used to create a new game.
generate a unique game identifier and store it to database table GAME_STATE
will insert a new row in database table GAME_STATE

    
### Function `update_game` {#id}




>     def update_game(
>         token,
>         consequence
>     )







    
# Module `initiation-game.demo` {#id}









    
# Module `initiation-game.game_constants` {#id}







    
## Classes


    
### Class `Consequence` {#id}




>     class Consequence(
>         value,
>         names=None,
>         *,
>         module=None,
>         qualname=None,
>         type=None,
>         start=1
>     )


An enumeration.


    
#### Ancestors (in MRO)

* [enum.Enum](#enum.Enum)



    
#### Class variables


    
##### Variable `DIE` {#id}






    
##### Variable `NEWBORN` {#id}






    
##### Variable `SURVIVE` {#id}






    
##### Variable `THRIVE` {#id}









    
### Class `Status` {#id}




>     class Status(
>         value,
>         names=None,
>         *,
>         module=None,
>         qualname=None,
>         type=None,
>         start=1
>     )


An enumeration.


    
#### Ancestors (in MRO)

* [enum.Enum](#enum.Enum)



    
#### Class variables


    
##### Variable `CATASTROPHE` {#id}






    
##### Variable `CLIMAX` {#id}






    
##### Variable `FALL` {#id}






    
##### Variable `INTRO` {#id}






    
##### Variable `RISE` {#id}











    
# Module `initiation-game.logic` {#id}






    
## Functions


    
### Function `console_turn` {#id}




>     def console_turn(
>         state
>     )


procedures that prints a turn's text when game is played in console-mode

@parameter: state - state model object of the current game. contains all
current state informations

    
### Function `turn_infos` {#id}




>     def turn_infos(
>         state
>     )


returns all the text necessary for a turn

@parameter: state - state model object of the current game. contains all
current state informations




    
# Namespace `initiation-game.scripts` {#id}




    
## Sub-modules

* [initiation-game.scripts.game_state](#initiation-game.scripts.game_state)






    
# Module `initiation-game.scripts.game_state` {#id}









    
# Module `initiation-game.state_model` {#id}







    
## Classes


    
### Class `State_model` {#id}




>     class State_model(
>         token=''
>     )










    
#### Methods


    
##### Method `get_consequence` {#id}




>     def get_consequence(
>         self
>     )




    
##### Method `get_score` {#id}




>     def get_score(
>         self
>     )




    
##### Method `get_status` {#id}




>     def get_status(
>         self
>     )




    
##### Method `increment_score` {#id}




>     def increment_score(
>         self,
>         val
>     )




    
##### Method `is_game_over` {#id}




>     def is_game_over(
>         self
>     )




    
##### Method `update_game` {#id}




>     def update_game(
>         self,
>         consequence_idx
>     )





-----
Generated by *pdoc* 0.10.0 (<https://pdoc3.github.io>).
