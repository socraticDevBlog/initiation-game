import db


class State_model:
    def __init__(self, token=""):
        if token != "":
            self.token = token
        else:
            self.token = db.new_game_token()

    def get_status(self):
        return db.get_status_by(self.token)

    def get_consequence(self):
        return db.get_consequence_by(self.token)
