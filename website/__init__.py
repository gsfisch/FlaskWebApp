from flask import Flask

def CreateApp():
    from .views import views
    from .auth import auth

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
