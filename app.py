from flask import Flask
from flask_restful import Resource, Api, request
from bson.objectid import ObjectId
import db


app = Flask(__name__)
api = Api(app)
movie = db.collection

class HelloWorld(Resource):

    def get(self, id):
        element = movie.find_one({"_id": ObjectId(id)})
        element["_id"] = str(element["_id"])
        return {'get' : element }
    
    def put(self, id, title, description, duration):
        element = movie.find_one_and_update({"_id": ObjectId(id)}, {"title": title, "description": description, "duration": duration})
        element["_id"] = str(element["_id"])
        return {'put' : element}

    def delete(self, id):
        element = movie.delete_one({"_id": ObjectId(id)})
        # element["_id"] = str(element["_id"])
        return {'delete' :str(id)}

    def post(self, title, description, duration):
        movie.insert_one( { "title" : title, "description": description, "duration": duration } )
        return {'post' :str(title)}

api.add_resource(HelloWorld, '/<string:id>')
# api.add_resource(HelloWorld, '/')

# request

if __name__ == '__main__':
    app.run(debug=True)