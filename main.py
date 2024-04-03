from flask import Flask
from flask import render_template,request,redirect
# from flask _sqlalchemy import SQLAlchemy
import mysql.connector 
conn = mysql.connector.connect(host="localhost",username="root",password="12345",database="flaskdata")
cuser=conn.cursor()

app=Flask(__name__)

@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")
@app.route("/contactus")
def contactus():
    return render_template("contactus.html")
@app.route("/services")
def services():
    cuser.execute("select * from flasksave")
    data=cuser.fetchall()
    return render_template("services.html",mydata=data)
@app.route("/savethisdata",methods=["post"])
def savethisdata():
    if request.method =="POST":
        mytitle=request.form.get("title")
        message=request.form.get("msg")
        cuser.execute(f"insert into flasksave values('{mytitle}','{message}')")
        conn.commit()
        return redirect("/contactus")
    return "your data is suceessfully............."
@app.route("/deletethisdata/<x>",methods=["POST"])
def deletethisdata(x):
    cuser.execute(f"delete from flasksave where title='{x}'")
    return"data deleteeeeeeeeeeeeeeeeee"

if __name__=="__main__":
    app.run(debug=True)

# orm:sqlalchemy