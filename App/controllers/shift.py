from App.database import db
from App.models import Shift
from datetime import datetime

def getShift(id):
    return db.session.get(Shift, id)

def printShiftInfo(shift):
    str = f'''
        Shift ID: {shift["id"]}
        Shift Start: {shift["shiftStart"]}
        Shift End: {shift["shiftEnd"]}
        Timed in: {shift["timedIn"]}
        Timed out: {shift["timedOut"]}
    '''
    return str

def rescheduleShift(id, start, end):
    shift = getShift(id)

    if not shift:
        print("Invalid Shift ID")
        return None
    
    try:
        shiftStart = datetime.strptime(start, "%d/%m/%Y %H:%M")
        shiftEnd = datetime.strptime(end, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Wrong Date Format Used. Please use DD/MM/YYY HH:MM")
        return None
    
    try:
        shift.rescheduleShift(shiftStart, shiftEnd)
        db.session.add(shift)
        db.session.commit()
        return shift
    except:
        print("Error Rescheduling Shift")
        return None


def deleteShift(id):
    shift = Shift.query.get(id)
    if not shift:
        return print("Failed to Delete Shift")
    db.session.delete(shift)
    db.session.commit()
    print("Shift Deleted")