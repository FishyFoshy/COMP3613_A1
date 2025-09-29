from App.database import db
from App.models import Staff, Shift, Report
from datetime import datetime, timedelta

def formulateRoster():
    today = datetime.now().date()
    weekStart = today - timedelta(days=today.weekday())
    weekEnd = weekStart + timedelta(days=6)
    
    allStaff = Staff.query.all()
    roster = {}

    for staff in allStaff:
        shifts = Shift.query.filter(Shift.staffID == staff.id, Shift.shiftStart >= weekStart, Shift.shiftEnd <= weekEnd).all()

        roster[staff.name] = [f'{shift.shiftStart.strftime("%d/%m/%Y %H:%M")} - {shift.shiftEnd.strftime("%d/%m/%Y %H:%M")}' for shift in shifts]
    
    return roster

def formulateReportData():
    today = datetime.now().date()
    weekStart = today - timedelta(days=today.weekday())
    weekEnd = weekStart + timedelta(days=6)

    allStaff = Staff.query.all()
    data = {}

    for staff in allStaff:
        totalShifts = 0
        totalWorkedHours = 0
        shiftIDs = []

        shifts = Shift.query.filter(Shift.staffID == staff.id, Shift.shiftStart >= weekStart, Shift.shiftEnd <= weekEnd).all()

        for shift in shifts:
            shiftIDs.append(shift.id)
            totalShifts += 1
            totalWorkedHours += shift.getHoursWorked()
        
        data[staff.name] = {
            "totalShifts": totalShifts,
            "totalWorkedHours": totalWorkedHours,
            "shiftIDs": shiftIDs
        }

    return data
    
def createReport():
    roster = formulateRoster()
    data = formulateReportData()
    newReport = Report(roster, data)
    db.session.add(newReport)
    db.session.commit()
    return newReport

def listReports():
    allReports = Report.query.all()
    str = ""

    for report in allReports:
        str += f'Report ID: {report.id} | Created on: {report.dateCreated}\n'
        
    return str

def printReportInfo(report):
    str = f'''
        ReportID: {report["id"]}
        Date Created: {report["dateCreated"]}
    '''
    
    for staffName, data in report["data"].items():
        str += f'''
        ---------------------------------------------------
            Name: {staffName}
            Total Shifts: {data["totalShifts"]},
            Total Worked Hours: {data["totalWorkedHours"]:.2f},
            Shift IDs: {data["shiftIDs"]}
        ---------------------------------------------------
        '''

    return str

def getReport(id):
    return db.session.get(Report, id)

def deleteReport(id):
    report = Report.query.get(id)
    if not report:
        return print("Failed to Delete Report")
    db.session.delete(report)
    db.session.commit()
    return print("Report Deleted")