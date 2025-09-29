from App.database import db
from datetime import datetime

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    adminID = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    shiftStart = db.Column(db.DateTime, nullable=False)
    shiftEnd = db.Column(db.DateTime, nullable=False)
    timedIn = db.Column(db.DateTime)
    timedOut = db.Column(db.DateTime)

    def __init__(self, staffID, adminID, shiftStart, shiftEnd):
        self.staffID = staffID
        self.adminID = adminID
        self.shiftStart = shiftStart
        self.shiftEnd = shiftEnd

    def rescheduleShift(self, shiftStart, shiftEnd):
        self.shiftStart = shiftStart
        self.shiftEnd = shiftEnd
        self.timedIn = None
        self.timedOut = None

    def getHoursWorked(self):
        if not self.timedIn or not self.timedOut:
            return 0
        else:
            return (self.timedOut - self.timedIn).total_seconds() / 3600
    
    def get_json(self):
        return{
            'id': self.id,
            'staffID': self.staffID,
            'adminID': self.adminID,
            'shiftStart': self.shiftStart.strftime("%d/%m/%Y %H:%M"),
            'shiftEnd': self.shiftEnd.strftime("%d/%m/%Y %H:%M"),
            'timedIn': self.timedIn.strftime("%d/%m/%Y %H:%M") if self.timedIn else None,
            'timedOut': self.timedOut.strftime("%d/%m/%Y %H:%M") if self.timedOut else None
        }