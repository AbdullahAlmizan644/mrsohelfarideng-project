from flask import Flask,Blueprint
from flask_mysqldb import MySQL

db=MySQL()


def create_app():
    UPLOAD_FOLDER = '/home/ares/sohel-project/website/static/image'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    app=Flask(__name__)
    app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
    app.config['SECRET_KEY']='sohel-farid'
    app.config['MYSQL_HOST']='127.0.0.1'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']=''
    app.config['MYSQL_DB']='electric_meter'


    db.init_app(app)




    from .view import view
    from .admin import admin
    from .auth import auth


    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app