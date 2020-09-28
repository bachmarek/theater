from common import output
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "marek": {"age": 28, "gender": "male"},
    "vendy": {"age": 26, "gender": "female"},
}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")


# dev only
if __name__ == "__main__":
    app.run(debug=True)


# print(output.output_func())
