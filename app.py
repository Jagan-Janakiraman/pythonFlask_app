#First we imported the Flask class.
from flask import Flask,request    


"""
Next we create an instance of this class. 
The first argument is the name of the application’s module or package.
__name__ is a convenient shortcut for this that is appropriate for most cases. 
This is needed so that Flask knows where to look for resources such as templates and static files.
"""
app = Flask(__name__)  

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


