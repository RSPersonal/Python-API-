#! Python 3
# main 
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"tim": {"age": 10, "gender": "male", "hobby": "D&D"},
        "bill": {"age": 15, "gender": "male", "hobby": "coding"}}
        
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
        
    def post(self):
        return {"data": "Posted"}
        
api.add_resource(HelloWorld, "/helloworld/<name>")


if __name__ == "__main__":
    print("\nApp succesfully started in debug mode")
    app.run(debug=True)
    