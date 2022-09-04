import sqlite3
import uuid


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def new_game_token():
    guid_token = str(uuid.uuid4())

    conn = create_connection("scripts/game_state.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO GAME_STATE(token) VALUES(?)", (guid_token,))
    conn.commit()
    conn.close()

    return guid_token
