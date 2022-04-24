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
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()

        for user in users:
            if username==user[1] and password==user[4]:
                session["user"]=username
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
        password1=request.form.get("password1")
        password2=request.form.get("password2")


        if len(username)<5:
            flash("username must be greater than 4 words",category="error")

        elif len(email)<5:
            flash("email must be greater than 4 words",category="error")

        elif len(password1)<8:
            flash("password must be greater than 8 digit",category="error")

        elif password1!=password2:
            flash("password doesn't match",category="error")

        else:
            cur=db.connection.cursor()
            cur.execute("INSERT INTO users(username,email,password,date) VALUES(%s,%s,%s,%s)",(username,email,password1,datetime.now()))
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
