import  MySQLdb
from app import  db
from datetime import datetime
from flask_sqlalchemy.wtf import

class Apm_Users(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    user_login =db.Column(db.String(60))
    user_pass =db.Column(db.String(255))
    user_nicename =db.Column(db.String(50))
    user_email =db.Column(db.String(100))
    user_url =db.Column(db.String(1000))
    user_registered =db.Column(db.DateTime)
    user_activation_key =db.Column(db.String(255))
    user_status =db.Column(db.INTEGER)
    display_name =db.Column(db.VARCHAR(250))

    def __init__(self, ID,user_login, user_pass, user_nicename, user_email,user_url
                 ,user_activation_key,user_status,display_name,user_registered=None):
        self.ID =ID
        self.user_login = user_login
        self.user_pass = user_pass
        self.user_nicename = user_nicename
        self.user_email = user_email
        self.user_url = user_url
        self.user_activation_key = user_activation_key
        self.display_name = display_name
        if user_registered is None:
            pub_date = datetime.utcnow()




    def __repr__(self):
        return '<Apm_Users %r>' % self.user_login

    TodoForm = model_form(Todo)