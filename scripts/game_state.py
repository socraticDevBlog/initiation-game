import sqlite3

connection_obj = sqlite3.connect("game_state.db")

cursor_obj = connection_obj.cursor()

gamestate_table = """ CREATE TABLE GAME_STATE (
            id INTEGER PRIMARY KEY,
            token VARCHAR(255) NOT NULL UNIQUE,
            score INT DEFAULT 0,
            status INT DEFAULT 1, 
            consequence INT DEFAULT 0,
            creation_datetime DATETIME DEFAULT current_timestamp,
            update_datetime DATETIME current_timestamp,
            end_datetime DATETIME
        ); """

cursor_obj.execute(gamestate_table)

print("Table is Ready")

connection_obj.close()
