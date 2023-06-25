#First we imported the Flask class.
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import pymysql




"""
Next we create an instance of this class. 
The first argument is the name of the application’s module or package.
__name__ is a convenient shortcut for this that is appropriate for most cases. 
This is needed so that Flask knows where to look for resources such as templates and static files.
"""
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/restaurent_monitor'
db = SQLAlchemy(app)


# Database configuration
db_config = {
    'host': 'localhost',
    'database': 'database_name_here', # add ur database name here
    'user': 'root', # mysql User name here
    'password': 'password'  # mysql Password  here
}

# to create a database connection
def create_connection():
    connection = None
    try:
        connection = pymysql.connect(**db_config)
        # print("Connected to MySQL database")
        return connection
    except pymysql.Error as e:
        print(f"Error while connecting to MySQL database: {e}")
    return connection


# to check the database connection
@app.route('/check_db_connection', methods=['GET'])
def check_db_connection():
    try:
        connection = create_connection()
        if connection is None:
            return jsonify(status="Error", message="Failed to connect to the database")

        connected_database = db_config['database']  # Retrieve the database name from the db_config dictionary
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        table_names = [table[0] for table in cursor.fetchall()] #LIST COMPRENSION TO DISPLAY THE TABLES IN THAT DATABASE
        cursor.close()
        connection.close()
        return jsonify(status="Connected", database=connected_database, tables=table_names)
    except pymysql.Error as e:
        return jsonify(status="Error", message=str(e))

"""
We then use the route() decorator to tell Flask what URL should trigger our function.
The function returns the message we want to display in the user’s browser. 
The default content type is HTML, so HTML in the string will be rendered by the browser.
"""
@app.route("/")
def hello():
    return "Basic Flask App  !!YAY "

@app.route("/firstpage")
def firstpage():
    return "This is the dashboard. WELCOME!!"


def do_the_login():
    return "LogedIaaaN"
def show_login_form():
    return "Fill the Form."




# HTTP Methods
@app.route("/logins", method=['GET'] )
def login():
   if request.method == 'GET':
       return do_the_login()
   else:
       return show_login_form()