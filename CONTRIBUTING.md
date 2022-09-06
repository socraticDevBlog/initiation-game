# from a dev perspective


## tech stack

| function            | tech    |
| ------------------- | ------- |
| interface with game | FastAPI |
| store game state    | sqlite  |

## setup

feel free to use python virtual environment and sqlite DB Browser for SQLite to
help you keep your sanity while developing.

### generate a new game state database

```
cd scripts
python game_state.py
```
expect a new file named `game_state.db` to appear in the directory

### play the console version in your terminal
```
cd ..
python console_game.py
``
