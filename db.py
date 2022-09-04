from dataclasses import field
import sqlite3
import uuid

DB_PATH = "scripts/game_state.db"
"""
Path to database file.
Before executing game the first time, create a new datafile by executing
scripts/game_state.py script
"""


def _create_connection():
    """
    private function. do not call directly
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(e)

    return conn


def new_game_token():
    """
    function used to create a new game.
    generate a unique game identifier and store it to database table GAME_STATE
    will insert a new row in database table GAME_STATE
    """
    guid_token = str(uuid.uuid4())

    conn = _create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO GAME_STATE(token) VALUES(?)", (guid_token,))
    conn.commit()
    conn.close()

    return guid_token


def _get_value_by(token, field_name):
    """
    private function. do not call directly!
    """
    sql = f"SELECT {field_name} FROM GAME_STATE WHERE token = ?"
    var_token = (token,)

    conn = _create_connection()
    cur = conn.cursor()
    cur.execute(sql, var_token)
    idx = cur.fetchone()
    conn.close()
    return idx[0]


def get_status_by(token):
    """
    retrieve Status enum index from database
    """
    return _get_value_by(token, "status")


def get_consequence_by(token):
    """
    retrieve Consequence enum index from database
    """
    return _get_value_by(token, "consequence")
