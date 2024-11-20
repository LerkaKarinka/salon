from flask import Flask, render_template
from database import Database
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.jinja")

@app.route("/employee")
def employee():
    db = Database()
    emp = db.get_employee()     
    return render_template("employee.jinja", emp = emp)
@app.route("/price")
def price():    
    return render_template("price.jinja") 
@app.route("/registration")
def registration():    
    return render_template("registration.jinja")
    
def main():
    app.run("0.0.0.0", 8000,True)


if __name__ == "__main__":
    app.run(debug=True)