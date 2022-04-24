from flask import Blueprint, render_template
from website.__init__ import db

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


@view.route("/meter")
def meter():
    return render_template("view/meter.html")


@view.route("/card")
def card():
    return render_template("view/addCard.html")



@view.route("/notice")
def notice():
    return render_template("view/notice.html")


@view.route("/tips")
def tips():
    return render_template("view/tips.html")