MP for CS 165
crimedb

=======

Technology used/required:
   - PostgreSQL 9.3
   - Python 3.3
   - Django 1.6

   (files already included)
   - JQuery 1.11
   - Bootstrap 3
   - Chartkick

=========================

To pre-populate the database:
   Create database
   1. Create a database named 'crimedb' with password 'password' and set owner as 'postgres'.

   Creat tables for database
   2. Run cmd and go to the directory of the project.
   3. Run 'python manage.py syncdb'. This should automatically create the required tables.
   4. Create your superuser

   Run script for data
   5. Still in the project directory, run 'python manage.py shell'.
   6. In the python shell, 'from crime import populatedb'
   7. Then run 'populatedb.populate()'
   8. Wait for the script to finish and your database has been pre-populated

   Generated data:
25 Locations
10 Categories
50 Agents
50 Suspects
n Reports

==========================================================================================

To access the website:
   1. Run cmd and go to the directory of the project
   2. 'python manage.py runserver'
   3. Open browser and go to 'http://127.0.0.1:8000/crime' for the homepage

==========================================================================================

Basic requirements:
   Reports
   - Min 5 categories
   - Time and date are recorded
   - Location
   - Multiple investigating agent
   - Can be solved
   - Only one suspect

   Suspects
   - Name
   - Location (does not change)

   Agents
   - Name
   - Location (may change)

   Locations
   - Min 20
   - Human-readable

=================================

Features:
   Create
   - Report
   - Agent
   - Suspect
   
   Update
   - Report
   - Agent
   - Suspect

   Delete
   - Report
   - Agent
   - Suspect
   - Confirmation & no cascade

   Read
   - Paginated reports
   - Paginated agents
   - Paginated suspects
   - Paginated criminal history
   - Paginated investigating officers
   - Search and filtering for crimes
   - Search and filtering for suspects
   - Search and filtering for agents

   Charts
   - Average crime per hour histogram
   - Histogram by location
   - Pie chart of crime categories
   - pie chart by location

