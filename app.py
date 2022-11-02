import os
import MySQLdb
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect,admin_loginact,user_reg,user_loginact,status_act,lost_act,delete_act,admin_vp,viewfound,updateact,viewlost
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html") 

@app.route("/admin.html")
def admin():
    return render_template("admin.html")  

@app.route("/user.html")
def user():
    return render_template("user.html") 

@app.route("/lost.html")
def analyst():
    return render_template("lost.html")

@app.route("/userhome.html")
def userhome():
    return render_template("userhome.html")

  

@app.route("/adminhome.html")
def adminhome():
    return render_template("adminhome.html")    

@app.route("/register.html")
def register():
    return render_template("register.html") 


#--------------------------------------------------Login----------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

@app.route("/userlog", methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':
        status = user_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("userhome.html", m1="sucess")
        else:
            return render_template("user.html", m1="Login Failed")

#-----------------------------------------------Register------------------------------------------------
@app.route("/registeract", methods = ['GET','POST'])
def registeract():
   if request.method == 'POST':    
      id="0"
      status = user_reg(request.form['username'],request.form['password'],request.form['email'],request.form['rollno'],request.form['department'])
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("register.html",m1="failed")
   
   
@app.route("/lostact", methods = ['GET','POST'])
def lostact():
   if request.method == 'POST':    
      id="0"
      status = lost_act(request.form['username'],request.form['rollno'],request.form['phone'],request.form['product'],request.form['department'])
      if status == 1:
       return render_template("lost.html",m1="sucess")
      else:
       return render_template("lost.html",m1="failed")
   
   
@app.route("/statusact", methods = ['GET','POST'])
def statusact():
   if request.method == 'POST':    
      id="0"
      status = status_act(request.form['username'],request.form['product'],request.form['status'])
      if status == 1:
       return render_template("view.html",m1="sucess")
      else:
       return render_template("view.html",m1="failed")

#-------------------------------------------View-------------------------------------------------------
@app.route("/view.html")
def viewp():
    data = viewlost()
    print(data)
    return render_template("view.html",users = data) 

@app.route("/found.html")
def found():
    data = viewfound()
    print(data)
    return render_template("found.html",users = data) 

@app.route("/adminvp.html")
def adminv():
    data = admin_vp()
    print(data)
    return render_template("adminvp.html",users = data) 




#-------------------------------------------activate---------------------------------------------------

   
   
@app.route("/update")
def update():
    a=request.args.get('a')
    d=request.args.get('d')
    data = updateact(a,d)
    return render_template("update.html",m1="sucess",users=data)

@app.route("/delete")
def delete():
    status = delete_act(request.args.get('a'),request.args.get('d'))
    if status == 1:
       return render_template("adminvp.html",m2="sucess")
    else:
       return render_template("adminvp.html",m2="failed")



# -------------------------------------------Graph---------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
