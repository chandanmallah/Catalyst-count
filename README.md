# Welcome to Catalyst Media's Data Management Tool!
This application allow users to login and upload a large volume data csv (1GB) with a visual
progress of the upload.
Users are allow to filter the data using a form. 
Once the user submits the form,  the count of records is displayed based on the applied filters.

![image](https://github.com/chandanmallah/Catalyst-count/assets/45361929/5305af18-7d83-41c2-a037-2df4722da218)
login page  http://localhost:8000/login

![image](https://github.com/chandanmallah/Catalyst-count/assets/45361929/1b0da75a-ea95-4d73-a264-6b7c62cd3271)
upload csv data http://localhost:8000/dataupload

![image](https://github.com/chandanmallah/Catalyst-count/assets/45361929/9b17c9b6-04ef-4f9c-a817-3fb323cf925f)
Query builder (search for desired data) http://localhost:8000/querybuilder

![image](https://github.com/chandanmallah/Catalyst-count/assets/45361929/3ae69971-f439-4919-bcc0-6ca727dd16ac)
All users data and click on add user's to add user http://localhost:8000/users







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
