import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Staff, Admin, Shift, Report
from App.main import create_app
from App.controllers import (
    create_user, get_all_users_json, get_all_users, initialize,
    createStaff, timeIn, timeOut, getAllStaff, getStaff, deleteStaff,
    createAdmin, scheduleShift, getAllAdmins, getAdmin, deleteAdmin,
    getShift, printShiftInfo, rescheduleShift, deleteShift
    )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help="Staff object commands")

@staff_cli.command("create", help="Creates a staff object")
@click.argument("name", default="Jeremy")
@click.argument("password", default="jpass")
def create_staff_command(name, password):
    staff = createStaff(name, password)

    if not staff:
        print("Could not create staff object")
    else:
        print(f'Staff member {staff.name} created')

@staff_cli.command("time_in", help="Time in to a shift")
def time_in_command():
    shiftID = click.prompt(f'Enter a shift ID to time in', type=int)
    string = timeIn(shiftID)
    print(string)

@staff_cli.command("time_out", help="Time out of a shift")
def time_in_command():
    shiftID = click.prompt(f'Enter a shift ID to time out', type=int)
    string = timeOut(shiftID)
    print(string)

@staff_cli.command("list", help="Show all staff")
def list_staff_command():
    print(getAllStaff())

@staff_cli.command("find", help="Find a particular Staff Member")
def get_staff_command():
    staffID = click.prompt("Enter a staff id", type=int)
    staff = getStaff(staffID)
    
    if not staff:
        print("Invalid Staff ID")
        return
    else:
        print(f'ID: {staff.id}, Name: {staff.name}\n')

app.cli.add_command(staff_cli)

'''
Admin Commands
'''

admin_cli = AppGroup('admin', help="Admin object commands")

@admin_cli.command("create", help="Creates a admin object")
@click.argument("name", default="Bob")
@click.argument("password", default="bobpass")
def create_admin_command(name, password):
    admin = createAdmin(name, password)

    if not admin:
        print("Could not create staff object")
    else:
        print(f'Admin {admin.name} created')

@admin_cli.command("schedule_shift", help="Schedules a shift for a staff")
def schedule_admin_command():
    adminID = click.prompt("Enter ID of the Admin Scheduling the Shift", type=int)
    staffID = click.prompt("Enter ID of the Staff Shift is for", type=int)
    shiftStart = click.prompt("Enter Start of Shift in format DD/MM/YYYY HH:MM")
    shiftEnd = click.prompt("Enter End of Shift in format DD/MM/YYYY HH:MM")
    shift = scheduleShift(staffID, adminID, shiftStart, shiftEnd)

    if not shift:
        print("Error Scheduling Shift")
        return
    else:
        print(f'Shift Scheduled.\n{shift.get_json()}')

@admin_cli.command("reschedule_shift", help="Reschedules a shift for a staff")
def reschedule_admin_command():
    shiftID = click.prompt("Enter ID of the Shift being Rescheduled", type=int)
    
    shift = getShift(shiftID)

    if not shift:
        print("Invalid Shift ID")
        return
    
    shiftStart = click.prompt("Enter Start of Shift in format DD/MM/YYYY HH:MM")
    shiftEnd = click.prompt("Enter End of Shift in format DD/MM/YYYY HH:MM")
    reschdeuledShift = rescheduleShift(shiftID, shiftStart, shiftEnd)

    if not reschdeuledShift:
        print("Error Rescheduling Shift")
        return
    else:
        print(f'Shift Rescheduled.\n{shift.get_json()}')

@admin_cli.command("list", help="Show all Admins")
def list_admin_command():
    print(getAllAdmins())

@admin_cli.command("find", help="Find a particular Admin")
def get_admin_command():
    adminID = click.prompt("Enter a admin id", type=int)
    admin = getAdmin(adminID)
    
    if not admin:
        print("Invalid Admin ID")
        return
    else:
        print(f'ID: {admin.id}, Name: {admin.name}\n')

@admin_cli.command("delete_staff", help="Deletes a Staff")
def delete_staff_admin_command():
    staffID = click.prompt("Enter a staff id", type=int)
    deleteStaff(staffID)

@admin_cli.command("delete_admin", help="Deletes a Admin")
def delete_admin_admin_command():
    adminID = click.prompt("Enter a admin id", type=int)
    deleteAdmin(adminID)

@admin_cli.command("delete_shift", help="Deletes a Shift")
def delete_shift_admin_command():
    shiftID = click.prompt("Enter a shift id", type=int)
    deleteShift(shiftID)

app.cli.add_command(admin_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)