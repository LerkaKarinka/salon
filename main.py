from flask import Flask, render_template
from database import Database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.jinja")

@app.route("/employee")
def employee():    
    db = Database()
    result_raw = db.get_employee()
    result = []
    for r in result_raw:
        result.append(str(r["id"]) + ": " + r["name"] + r["post"])
    return render_template("employee.jinja") 
    
        


def main():
    app.run("0.0.0.0", 8000,True)

if __name__ == "__main__":
    app.run(debug=True)