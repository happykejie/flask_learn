from app import app
from app.api import  api
from app.api.admin import  admin
from app.api.weixin import  weixin

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(weixin, url_prefix='/api')
app.register_blueprint(admin, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
