from App.database import db
from datetime import datetime

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateCreated = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    roster = db.Column(db.JSON, nullable=False)
    data = db.Column(db.JSON, nullable=False)

    def __init__(self, roster, data):
        self.dateCreated = datetime.now()
        self.roster = roster
        self.data = data

    def get_json(self):
        return {
            'id': self.id,
            'dateCreated': self.dateCreated.strftime("%d/%m/%Y %H:%M"),
            'roster': self.roster,
            'data': self.data
        }