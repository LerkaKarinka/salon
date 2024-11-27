from flask import Flask, render_template, request, Response
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
    db = Database()
    pr = db.get_price()    
    return render_template("price.jinja", pr=pr) 

@app.route("/registration", methods=['GET', 'POST'])
def registration(): 
    db = Database()  
    if request.method == "POST":
        db = Database()
        name = request.form["name"]
        telephone = request.form["telephone"]
        type = request.form["type"] 
        db.add_registration(name,telephone,type)
    ser = db.get_services()
    return render_template("registration.jinja", ser=ser)
    
@app.route("/img")
def get_image():
    if not "dir" in request.args:
        return Response("dir is not defined!", 418)
    if not "id" in request.args:
        return Response("id is not defined!", 418)
    file = open(f"files/{request.args['dir']}/{request.args['id']}.jpg", "rb")
    return Response(file, 200)

def main():
    app.run("0.0.0.0", 8000,True)


if __name__ == "__main__":
    app.run(debug=True)