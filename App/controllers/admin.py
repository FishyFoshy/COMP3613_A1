from App.database import db
from App.models import Staff, Admin, Shift
from datetime import datetime

def createAdmin(name, password):
    newAdmin = Admin(name, password)
    db.session.add(newAdmin)
    db.session.commit()
    return newAdmin

def scheduleShift(staffID, adminID, start, end):
    staff = Staff.query.get(staffID)

    if not staff:
        print("Invalid Staff ID")
        return None
    
    try:
        shiftStart = datetime.strptime(start, "%d/%m/%Y %H:%M")
        shiftEnd = datetime.strptime(end, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Wrong Date Format Used. Please use DD/MM/YYY HH:MM")
        return None
    
    shift = Shift(staffID, adminID, shiftStart, shiftEnd)
    db.session.add(shift)
    db.session.commit()
    return shift

def getAllAdmins():
    allAdmins = Admin.query.all()
    str = ""
    for admin in allAdmins:
        str += f'ID: {admin.id}, Name: {admin.name}\n'
    return str

def getAdmin(id):
    return db.session.get(Admin, id)

def deleteAdmin(id):
    admin = Admin.query.get(id)
    if not admin:
        return print("Failed to delete Admin")
    db.session.delete(admin)
    db.session.commit()
    print("Admin Deleted")