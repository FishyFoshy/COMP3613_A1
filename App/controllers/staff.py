from App.database import db
from App.models import Staff, Shift
from datetime import datetime

def createStaff(name, password):
    newStaff = Staff(name, password)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff

def timeIn(shiftID, time=None):
    shift = Shift.query.get(shiftID)

    if not shift:
        return "Invalid Shift ID"
    
    if not time:
        time = datetime.now()

    if not shift.timedIn:
        shift.timedIn = time
    else:
        return "Already Timed In"
    
    db.session.add(shift)
    db.session.commit()
    return f'Timed in at {time.strftime("%d/%m/%Y %H:%M")}'

def timeOut(shiftID, time=None):
    shift = Shift.query.get(shiftID)

    if not shift:
        return "Invalid Shift ID"
    
    if not time:
        time = datetime.now()

    if not shift.timedIn:
        shift.timedOut = time
    else:
        return "Already Timed Out"
    
    db.session.add(shift)
    db.session.commit()
    return f'Timed out at {time.strftime("%d/%m/%Y %H:%M")}'

def getAllStaff():
    allStaff = Staff.query.all()
    str = ""
    for staff in allStaff:
        str += f'ID: {staff.id}, Name: {staff.name}\n'
    return str

def getStaff(id):
    return db.session.get(Staff, id)

def deleteStaff(id):
    staff = staff.query.get(id)
    if not staff:
        return None
    db.session.delete(staff)
    db.session.commit()