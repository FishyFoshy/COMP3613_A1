from .user import create_user
from .admin import createAdmin, scheduleShift
from .staff import createStaff, timeIn, timeOut
from App.database import db
from datetime import datetime

def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    createStaff('Kevin', 'kevinpass')
    createStaff('Luffy', 'luffypass')
    createAdmin('Nishant', 'nishantpass')
    createAdmin('Daniel', 'danielpass')
    createStaff("Dominic", "dompass")

    # Kevin’s shifts, handled by admin Nishant.
    shift1 = scheduleShift(1, 1, "29/09/2025 08:00", "29/09/2025 09:30")
    shift2 = scheduleShift(1, 1, "30/09/2025 10:00", "30/09/2025 12:00")
    shift3 = scheduleShift(1, 1, "2/10/2025 14:00", "2/10/2025 15:00")
    shift4 = scheduleShift(1, 1, "3/10/2025 18:00", "3/10/2025 19:00")
    
    # Luffy’s shifts, handled by admin Daniel.
    shift5 = scheduleShift(2, 2, "29/09/2025 11:00", "29/09/2025 12:00")
    shift6 = scheduleShift(2, 2, "30/09/2025 16:00", "30/09/2025 17:00")
    shift7 = scheduleShift(2, 2, "1/10/2025 17:00", "1/10/2025 18:30")
    shift8 = scheduleShift(2, 2, "3/10/2025 20:00", "3/10/2025 21:00")
    
    # Kevin clock-ins/outs.
    timeIn(1, datetime.strptime("29/09/2025 08:05", "%d/%m/%Y %H:%M"))
    timeOut(1, datetime.strptime("29/09/2025 09:25", "%d/%m/%Y %H:%M"))
    
    timeIn(2, datetime.strptime("30/09/2025 10:10", "%d/%m/%Y %H:%M"))
    timeOut(2, datetime.strptime("30/09/2025 11:55", "%d/%m/%Y %H:%M"))
    
    timeIn(3, datetime.strptime("2/10/2025 14:02", "%d/%m/%Y %H:%M"))
    timeOut(3, datetime.strptime("2/10/2025 14:58", "%d/%m/%Y %H:%M"))
    
    timeIn(4, datetime.strptime("3/10/2025 18:03", "%d/%m/%Y %H:%M"))
    timeOut(4, datetime.strptime("3/10/2025 18:55", "%d/%m/%Y %H:%M"))    
    
    # Luffy clock-ins/outs.
    timeIn(5, datetime.strptime("29/09/2025 11:05", "%d/%m/%Y %H:%M"))
    timeOut(5, datetime.strptime("29/09/2025 11:59", "%d/%m/%Y %H:%M"))
    
    timeIn(6, datetime.strptime("30/09/2025 16:10", "%d/%m/%Y %H:%M"))
    timeOut(6, datetime.strptime("30/09/2025 16:55", "%d/%m/%Y %H:%M"))
    
    timeIn(7, datetime.strptime("1/10/2025 17:01", "%d/%m/%Y %H:%M"))
    timeOut(7, datetime.strptime("1/10/2025 18:20", "%d/%m/%Y %H:%M"))
    
    timeIn(8, datetime.strptime("3/10/2025 20:15", "%d/%m/%Y %H:%M"))
    timeOut(8, datetime.strptime("3/10/2025 20:58", "%d/%m/%Y %H:%M"))