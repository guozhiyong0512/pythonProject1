from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:guozhiyong0512@123.56.172.18:3308/tmp_hello?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    steps = db.Column(db.String(120), unique=False, nullable=True)
    def __repr__(self):
        return '<User %r>' % self.description
# db.create_all()

db.session.add(TestCase(id=1,name="2",description="3",steps="4"))
db.session.commit()


# class HelloWorld(Resource):
#     def get(self, tmp):
#         print(tmp)
#         # db.create_all()
#         db.session.add(TestCase(id=1234, name="tmp"))
#         db.session.commit()
#         return "hello, world!"
#
#     def post(self, tmp):
#         print(request.data)
#         print(request.json)
#         print(tmp)
#         return "hello, world!"


# api.add_resource(HelloWorld, '/abc/<int:tmp>')


# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")
