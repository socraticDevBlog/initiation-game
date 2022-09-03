import sqlite3
import uuid


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def select_state_by_token(conn, token):
    cur = conn.cursor()
    cur.execute("SELECT * FROM GAME_STATE WHERE token=?", (token,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def new_game_token(conn):
    guid_token = str(uuid.uuid4())

    cur = conn.cursor()
    cur.execute("INSERT INTO GAME_STATE(token) VALUES(?)", (guid_token,))

    conn.commit()

    return guid_token
