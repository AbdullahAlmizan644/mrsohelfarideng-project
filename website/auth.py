from flask import Blueprint, render_template,request,flash,redirect,session
from website.__init__ import db,create_app
from datetime import datetime
import os
from werkzeug.utils import secure_filename

auth=Blueprint('auth', __name__)


app=create_app()

@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where username=%s and password=%s",(username,password,))
        user=cur.fetchone()


        if user:
            session["user"]=username
            session["meter"]=user[7]
            flash("Logged in successFully!",category="success")
            return redirect("/profile")
        else:
            flash("wrong username or password",category="error")

    return render_template('auth/login.html')


@auth.route("/user_logout")
def user_logout():
    session.pop("user",None)
    return redirect("/")



@auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        meter_number=request.form.get("meter_number")
        password1=request.form.get("password1")
        password2=request.form.get("password2")

        print(type(meter_number))
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where username=%s",(username,))
        user=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where meter_number=%s",(meter_number,))
        m=cur.fetchone()


        if user:
            flash("Username already exist",category="error")

        elif len(username)<5:
            flash("Username must be greater than 4 words",category="error")

        elif len(email)<5:
            flash("Email must be greater than 4 words",category="error")

        elif m:
            flash("Meter number already exist",category="error")

        elif "bs-" != meter_number[0:3]:
            flash("Your prefix should be bs-",category="error")

        elif len(meter_number)<8:
            flash("Meter number must be greater than 8 digit",category="error")

        elif len(password1)<8:
            flash("Password must be greater than 8 digit",category="error")

        elif password1!=password2:
            flash("Password doesn't match",category="error")

        else:
            cur=db.connection.cursor()
            cur.execute("INSERT INTO users(username,email,password,date,meter_number) VALUES(%s,%s,%s,%s,%s)",(username,email,password1,datetime.now(),meter_number,))
            db.connection.commit()
            cur.close()
            flash("Account created successfully!",category="success")
            return redirect("/login")
    return render_template("auth/signup.html")


@auth.route("/profile",methods=["GET","POST"])
def profile():
    if "user" in session:
        if request.method=="POST":
            image=request.files["image"]

            if image.filename=="":
                flash("No file selected", category="error")
                return redirect(request.url)

            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
                cur=db.connection.cursor() 
                cur.execute("UPDATE users set image=%s WHERE username=%s ",(image.filename,session["user"]))
                db.connection.commit()
                flash("Image upload successfully",category="success")
                return redirect(request.url)
        
        cur=db.connection.cursor() 
        cur.execute("select * from users where username=%s",(session["user"],))
        user=cur.fetchone()
        return render_template("auth/profile.html",user=user)
    else:
        return redirect("/login")
