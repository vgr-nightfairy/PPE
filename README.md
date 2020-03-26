This is the MVP for the PPE Tracker being built to help address COVID-19. The project is structured as follows:


    |-- PPE
        |-- app
            |-- dashapp1
                |-- callbacks.py
                |-- layout.py
            |-- templates
                |-- 404.html
                |-- base.html
                |-- index.html
                |-- login.html
                |-- masks.html
                |-- register.html
            |-- __init__.py
            |-- extensions.py
            |-- forms.py
            |-- models.py
            |-- routes.py
        |-- migrations
        |-- config.py
        |-- ppe.db
        |-- ppe.py
        |-- README.md


This is a Python application that utilizes Flask, SQLite, and Dash (to create an interative dashboard). Aside from
user registration and simple authentication, the basic end-to-end path for one PPE (N95 Masks) has been configured.
Essentially, this includes a form that gathers detailed information about current N95 Mask inventory at facilities, a
push to the database, and a real-time visualization of the aggregate count of N95 Masks per facility via the main
dashboard.

Run in virtualenv. Install dependencies as they come up (sorry, currently no requirements.txt file).
Set >> FLASK_APP=ppe.py. To get localhost link to see webapp, execute >> flask run.
When making changes to models.py, it is imperative to run >> flask db migrate    and     >> flask db upgrade
to track ongoing versions of the database. 
