from flask import Blueprint, render_template,session,flash,request,redirect
from website.__init__ import db,create_app
import os
from werkzeug.utils import secure_filename
from datetime import datetime

admin=Blueprint('admin', __name__)
app=create_app()

@admin.route("/dashboard")
def dashboard():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()

        cur=db.connection.cursor()
        cur.execute("SELECT count(sno) from users ")
        total_user=cur.fetchone()
        return render_template("admin/index.html",users=users,total_user=total_user)
    
    else:
        return redirect("/admin_login")

@admin.route("/admin_login",methods=["GET","POST"])
def admin_login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        if email=="admin@gmail.com" and password=="12345678":
            session["admin"]=email
            return redirect("/dashboard")
        else:
            flash("Wrong email or password.",category="error")
    return render_template("admin/login.html")



@admin.route("/admin_logout")
def admin_logout():
    session.pop("admin", None)
    flash("Admin Logged out!")
    return redirect("/")




@admin.route("/user_table")
def user_table():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()

        cur=db.connection.cursor()
        cur.execute("SELECT count(sno) from users ")
        total_user=cur.fetchone()
        return render_template("admin/user_table.html",users=users,total_user=total_user)

    else:
        return redirect("/admin_login")




@admin.route("/user_history")
def user_history():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM user_history")
        user_history=cur.fetchall()

        cur=db.connection.cursor()
        cur.execute("SELECT count(sno) from user_history")
        total_history=cur.fetchone()
        return render_template("admin/user_history.html",user_history=user_history,total_history=total_history)
    else:
        return redirect("/admin_login")



@admin.route("/write_notice",methods=["GET","POST"])
def write_notice():
    if "admin" in session:  
        if request.method=="POST":
            title=request.form.get('title')
            image = request.files['image']
            content=request.form.get('content')


            image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
            cur=db.connection.cursor()
            cur.execute("INSERT INTO notice(title,image,content,date) VALUES (%s,%s,%s,%s)",(title,image.filename,content,datetime.now(),))
            db.connection.commit()
            return redirect("/all_notice")

        return render_template("admin/write_notice.html")
    else:
        return redirect("/admin_login")
    
    
@admin.route("/all_notice",methods=["GET","POST"])
def all_notice():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM notice")
        notices=cur.fetchall()

        cur=db.connection.cursor()
        cur.execute("SELECT count(id) from notice")
        total_notice=cur.fetchone()
        return render_template("admin/all_notice.html",notices=notices,total_notice=total_notice)
    else:
        return redirect("/admin_login")
