from flask import Flask, request
from flask_restful import Resource, Api





app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


class TestCaseServer(Resource):
    def get(self):

        if "id" in request.args:
            for i in app.config["testcase"] :
                if i["id"] == int(request.args["id"]):
                    return  i
        else:

            return  app.config["testcase"]

    def post(self):
        if "id" not in request.json:
            return {"result":"error","errcode":"404","errmessage":"need testcase id"}
        app.config["testcase"].append(request.json)

        return {"result":"ok","errcode":"0"}


@app.route('/',methods=['post'])
def hello():
    return 'Hello, World!'


# @app.route('/app')
# def hello_2():
#     return 'Hello, app!'

api.add_resource(TestCaseServer, '/testcase')
if __name__ == '__main__':
    app.run(debug=True,)