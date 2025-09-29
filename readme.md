# Rostering App
```
•(Admin) Schedule a staff member shifts for the week
•(Staff) View combined roster of all staff
•(Staff) Time in/Time out at the stat/end of shift
•(Admin) View shift report for the week
```

# CLI Command

Initializes the Database
```
flask init
```

# Staff Commands

Time in at the Start of Shift
```
flask staff time_in
```

Time out at the End of Shift
```
flask staff time_out
```

View the Combined Staff Roster
```
flask staff view_roster
```

# Admin Commands

Creates a new Admin
```
flask admin create_admin
```

Creates a new Staff Member
```
flask admin create_staff
```

Schedules a Shift for a Staff Member
```
flask admin schedule_shift
```

Reschedules a Shift for a Staff Member
```
flask admin reschedule_shift
```

Lists all Admin
```
flask admin list_admins
```

Shows details of an Admin
```
flask admin find_admin
```

Lists all Staff
```
flask admin list_staff
```

Shows details of a Staff Member
```
flask admin find_staff
```

Creates a Shift Report
```
flask admin create_report
```

Shows the details of a chosen Shift Report
```
flask admin view_report
```

Lists all Reports
```
flask admin list_reports
```

Deletes chosen Staff
```
flask admin delete_staff
```

Deletes chosen Admin
```
flask admin delete_admin
```

Deletes chosen Shift
```
flask admin delete_shift
```

Deletes chosen Report
```
flask admin delete_report
```