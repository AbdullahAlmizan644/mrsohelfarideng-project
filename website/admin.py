from flask import Blueprint, render_template,session,flash,request,redirect
from website.__init__ import db

admin=Blueprint('admin', __name__)


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
