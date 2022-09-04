import db
from game_constants import Status


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

    def get_score(self):
        return db.get_score_by(self.token)

    def increment_score(self, val):
        return db.increment_score(self.token, val)

    def update_game(self, consequence_idx):
        return db.update_game(self.token, consequence_idx)

    def is_game_over(self):
        status = db.get_status_by(self.token)
        print(status)

        return status == Status.CATASTROPHE
