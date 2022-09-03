from db import create_connection, new_game_token

conn = create_connection("scripts/game_state.db")

print(conn)

token = new_game_token(conn)

print(token)

print("expect your table to have one more record with a new uuid.")
