# from server.__init__ import app
from flask_migrate import Migrate
from flask_restx import Api, fields, Namespace, Resource
# from server.models import db,app

from models import db, app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'bb8f7de46cd4426ebf5ca7df06d43665'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

ns =Namespace("api")


api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
