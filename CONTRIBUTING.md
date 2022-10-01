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
```

## keeping code well-documented

liberal use of docstrings is encouraged
we chose to use [https://pdoc3.github.io/pdoc/](https://pdoc3.github.io/pdoc/) to document our codebase.


### install pdoc3

```
python3 -m venv env
source env/bin/activate
pip3 install pdoc3
```

### generate fresh documentation

*at project's root
```
pdoc --pdf . |> code_documented.md
```