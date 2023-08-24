# Welcome to Catalyst Media's Data Management Tool!
This application allow users to login and upload a large volume data csv (1GB) with a visual
progress of the upload.
Users are allow to filter the data using a form. 
Once the user submits the form,  the count of records is displayed based on the applied filters.

## Quick Start Guide

**Welcome to Catalyst Media's Data Management Tool!** This guide will help you set up and use our Django Web Application for efficient data handling and analysis. Follow these steps to get started:

**Prerequisites**
Before diving in, make sure you have the following software installed on your system:

- **Python** (version 3.9.x)
- **Django** (version 3.2.19)
- **PostgreSQL** (version 15.x)
- **django-environ** (django-environ==0.4.5)
- **djangorestframework** (version 3.14.0)
- **psycopg2-binary** (version 2.9.6)
- **dj-database-url** version(2.0.0)

## Installation

**1. Get the Code:** Clone this repository or download and unzip the files to a location of your choice.

**2. Navigate to the Project:** In your terminal, move into the project folder using the command:
```sh
cd catalyst-count-main

# Install Dependencies: Install the required dependencies using the following command
pip install django

# Set Up the Database: Prepare the database by applying migrations
python manage.py makemigrations
python manage.py migrate

# Configure Database Connection: Open the .env file inside the catalyst_count folder. Make sure to set SECRET_KEY and DATABASE_URL. Adjust the DATABASE_URL to match your PostgreSQL database
DATABASE_URLpostgres://catalyst_media_count_user:tI5ACqZ4r3zon1EnNF883naI5uIWNawE@dpg-cjjoo1gcfp5c738glggg-a.singapore-postgres.render.com/catalyst_media_count

# Create a Superuser: Generate a superuser by entering dummy credentials
python manage.py createsuperuser

# Usage: To launch the development server, execute the following command
python.exe .\manage.py runserver

# Command Sequence Completed
# You can now close the terminal or shell.




It seems like you're looking for a way to divide the content based on whether the shell is still open or closed. In a linear README format, you cannot add content that is contextually dependent on the user's actions in the terminal.

However, you can provide clear instructions to the user on what to do next in both cases. Here's a way to structure it:

markdown
Copy code
## Installation

**1. Get the Code:** Clone this repository or download and unzip the files to a location of your choice.

**2. Navigate to the Project:** In your terminal, move into the project folder using the command:
```sh
cd catalyst-count-main
3. Install Dependencies: Install the required dependencies using the following command:

sh
Copy code
pip install django
4. Set Up the Database: Prepare the database by applying migrations:

sh
Copy code
python manage.py makemigrations
python manage.py migrate
5. Configure Database Connection: Open the .env file inside the catalyst_count folder. Make sure to set SECRET_KEY and DATABASE_URL. Adjust the DATABASE_URL to match your PostgreSQL database:

sh
Copy code
DATABASE_URL=postgres://catalyst_media_count_user:tI5ACqZ4r3zon1EnNF883naI5uIWNawE@dpg-cjjoo1gcfp5c738glggg-a.singapore-postgres.render.com/catalyst_media_count
6. Create a Superuser: Generate a superuser by entering dummy credentials:

sh
Copy code
python manage.py createsuperuser
7. Usage: To launch the development server, execute the following command:

sh
Copy code
python.exe .\manage.py runserver
8. Command Sequence Completed: You can now close the terminal or shell.

Next Steps
Server Running
The server will start running at http://localhost:8000/. Make sure there are no errors in the command prompt.

Login
Access the login page at http://localhost:8000/login. Use the superuser credentials created during installation to explore other pages.

Data Upload
Head to http://localhost:8000/dataupload to upload large CSV files containing company data.

Query Builder
Visit http://localhost:8000/querybuilder to utilize the query builder page. Apply filters based on name, year founded, industry, and country. After applying filters, clicking "Query Data" will display the matching record count.

Users
Check out http://localhost:8000/users to access the users page. This section lists all system users, accessible only to logged-in users.

Begin your journey to simplified data management with Catalyst Media's tool. Happy exploring!









