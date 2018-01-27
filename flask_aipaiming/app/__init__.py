from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:kejie@1234@121.42.165.46:3306/db_aipaimingTest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db =SQLAlchemy(app)

app.config['JSON_AS_ASCII'] = False


from app import views
