from .user import create_user
from .admin import createAdmin, scheduleShift
from .staff import createStaff, timeIn, timeOut
from App.database import db
from datetime import datetime

def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    createStaff('Jake', 'jakepass')
    createStaff('Finn', 'finnpass')
    createStaff("Dominic", "dompass")
    createAdmin('Brian', 'brianpass')
    createAdmin('Stephen', 'stephenpass')
    

    # Jake’s shifts, handled by admin Brian
    shift1 = scheduleShift(1, 1, "29/09/2025 09:00", "29/09/2025 15:00")
    shift2 = scheduleShift(1, 1, "30/09/2025 9:00", "30/09/2025 15:00")
    shift3 = scheduleShift(1, 1, "2/10/2025 9:00", "2/10/2025 13:30")
    shift4 = scheduleShift(1, 1, "3/10/2025 10:00", "3/10/2025 14:00")
    
    # Finn's shifts, handled by admin Stephen
    shift5 = scheduleShift(2, 2, "29/09/2025 9:00", "29/09/2025 12:00")
    shift6 = scheduleShift(2, 2, "30/09/2025 8:00", "30/09/2025 14:00")
    shift7 = scheduleShift(2, 2, "1/10/2025 8:00", "1/10/2025 14:00")
    shift8 = scheduleShift(2, 2, "3/10/2025 8:00", "3/10/2025 14:00")
    shift9 = scheduleShift(2, 2, "3/10/2025 10:00", "3/10/2025 14:00")
    
    # Jake time ins/outs
    timeIn(1, datetime.strptime("29/09/2025 09:05", "%d/%m/%Y %H:%M"))
    timeOut(1, datetime.strptime("29/09/2025 15:10", "%d/%m/%Y %H:%M"))
    
    timeIn(2, datetime.strptime("30/09/2025 08:58", "%d/%m/%Y %H:%M"))
    timeOut(2, datetime.strptime("30/09/2025 15:02", "%d/%m/%Y %H:%M"))
    
    timeIn(3, datetime.strptime("2/10/2025 9:02", "%d/%m/%Y %H:%M"))
    timeOut(3, datetime.strptime("2/10/2025 13:29", "%d/%m/%Y %H:%M"))
    
    timeIn(4, datetime.strptime("3/10/2025 10:00", "%d/%m/%Y %H:%M"))
    timeOut(4, datetime.strptime("3/10/2025 14:55", "%d/%m/%Y %H:%M"))    
    
    # Finn time ins/outs
    timeIn(5, datetime.strptime("29/09/2025 9:03", "%d/%m/%Y %H:%M"))
    timeOut(5, datetime.strptime("29/09/2025 12:01", "%d/%m/%Y %H:%M"))
    
    timeIn(6, datetime.strptime("30/09/2025 8:10", "%d/%m/%Y %H:%M"))
    timeOut(6, datetime.strptime("30/09/2025 14:32", "%d/%m/%Y %H:%M"))
    
    timeIn(7, datetime.strptime("1/10/2025 7:59", "%d/%m/%Y %H:%M"))
    timeOut(7, datetime.strptime("1/10/2025 14:04", "%d/%m/%Y %H:%M"))

    timeIn(8, datetime.strptime("2/10/2025 8:01", "%d/%m/%Y %H:%M"))
    timeOut(8, datetime.strptime("2/10/2025 14:20", "%d/%m/%Y %H:%M"))
    
    timeIn(9, datetime.strptime("3/10/2025 10:15", "%d/%m/%Y %H:%M"))
    timeOut(9, datetime.strptime("3/10/2025 14:10", "%d/%m/%Y %H:%M"))