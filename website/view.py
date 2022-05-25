from flask import Blueprint, render_template,request,flash,session,redirect
from website.__init__ import db
from random import randint
from datetime import datetime

view=Blueprint('view', __name__)


@view.route("/")
def index():
    return render_template("view/index.html")



@view.route("/about")
def about():
    return render_template("view/about.html")


@view.route("/service")
def service():
    return render_template("view/service.html")


@view.route("/contact")
def contact():
    return render_template("view/contact.html")



def token_generator(all_token):
    global token
    token =randint(11111111,99999999)
    print(token)

    while True:
        if token in all_token:
            print(token)
            token=randint(1,9)
            print("new")
            continue
        else:
            break

    return token
    


@view.route("/token",methods=["GET","POST"])
def buy_token():
    global token
    if "user" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s",(session["user"],))
        user=cur.fetchone()

        if request.method=="POST":
            amount=request.form.get("amount")
            
            cur=db.connection.cursor()
            cur.execute("SELECT token FROM user_history")
            data=cur.fetchall()
            data=list(data)

            per_unit_cost=6
            total_unit=int(amount)/per_unit_cost

            set_token= token_generator(data)            

            cur=db.connection.cursor()
            cur.execute("INSERT INTO user_history(user_id,user,meter_number,request_amount,token,unit,date) values(%s,%s,%s,%s,%s,%s,%s)",(user[0],user[1],user[7],int(amount),set_token,total_unit,datetime.now(),))
            db.connection.commit()

            flash(f"Your token number is {set_token}",category="success")
            return redirect("/card")

        return render_template("view/buy_token.html")

    else:
        return redirect("/login")



@view.route("/meter",methods=["POST"])
def meter():
    if "user" in session:
        if request.method=="POST":
            meter_number=request.form.get("meter_number")

            cur=db.connection.cursor()
            cur.execute("SELECT * FROM users where username=%s and meter_number=%s",(session["user"],meter_number,))
            data=cur.fetchone()
            print(data)
            

        return render_template("view/meter.html",data=data)

    else:
        return redirect("/login")


@view.route("/card",methods=["GET","POST"])
def card():
    if "user" in session:
    
        if request.method=="POST":
            meter_number=request.form.get("meter_number")
            get_token=request.form.get("token")

            print(meter_number)
            print(get_token,type(get_token))

            cur=db.connection.cursor()
            cur.execute("SELECT * FROM users where username=%s and meter_number=%s",(session["user"],meter_number,))
            user_data=cur.fetchone()
            print(user_data)


            cur=db.connection.cursor()
            cur.execute("SELECT * FROM user_history where user=%s and meter_number=%s and token=%s and status=%s",(session["user"],meter_number,int(get_token),0,))
            user_history_data=cur.fetchone()
            print(user_history_data)


            if user_history_data:
                cur=db.connection.cursor()
                cur.execute("UPDATE user_history SET status=%s where sno=%s",(1,user_history_data[8],))
                db.connection.commit()

                total=user_history_data[3]+user_data[6]
                unit=user_data[9]+user_history_data[5]
                last_recharge=user_history_data[3]

                cur=db.connection.cursor()
                cur.execute("UPDATE users SET total=%s,unit=%s,last_recharge=%s where username=%s and meter_number=%s",(total,unit,last_recharge,session["user"],meter_number,))
                db.connection.commit()

                flash("your recharge successfully",category="success")
                return redirect(request.url)

            else:
                flash("Incorrect meter number or token",category="error")
                return redirect(request.url)

        return render_template("view/card.html")
    
    else:
        return redirect("/login")



@view.route("/notice")
def notice():
    return render_template("view/notice.html")


@view.route("/tips")
def tips():
    return render_template("view/tips.html")