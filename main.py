from flask import Flask
from flask import render_template,request


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
    return render_template("services.html")
@app.route("/savethisdata",methods=["post"])
def savethisdata():
    if request.method =="POST":
        mytitle=request.form.get("title")
        message=request.form.get("msg")

        print(mytitle,message)
    return "your data is suceessfully............."

if __name__=="__main__":
    app.run(debug=True)
