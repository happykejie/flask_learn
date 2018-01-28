from flask import Flask
from  flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:kejie@1234@121.42.165.46:3306/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db =SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
