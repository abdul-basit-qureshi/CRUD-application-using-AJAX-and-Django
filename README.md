# Django Ajax CRUD Account Management Web Application

This is a Django web application that allows you to perform CRUD (Create, Read, Update, Delete) operations on user accounts using Ajax. The application allows you to manage user account details such as username, email, and password.

## Features

- Create new user accounts with username, email, and password.
- View a list of existing user accounts.
- Update user account details including username, email, and password.
- Delete user accounts.
- Real-time data updates using Ajax without requiring page reloads.
- Form validation for input fields.
- CSRF protection for Ajax requests.




## Installation
 
### Clone the repository
git clone https://github.com/abdul-basit-qureshi/CRUD-application-using-AJAX-and-Django.git


#### Create a virtual environment
python -m venv venv

#### Activate the virtual environment (macOS and Linux)
source venv/bin/activate

#### Activate the virtual environment (Windows)
venv\Scripts\activate

#### Install the required dependencies
pip install -r requirements.txt

#### Apply database migrations
python manage.py migrate

#### Start the development server
python manage.py runserver

After executing these commands, you can access the application by opening your web browser and visiting http://localhost:8000.
