from flask import Flask
from flask_restful import Resource, Api, request
from bson.objectid import ObjectId
import db, json

app = Flask(__name__)
api = Api(app)
movie = db.collection

class HelloWorld(Resource):

    def get(self, id):
        element = movie.find_one({"_id": ObjectId(id)})
        element["_id"] = str(element["_id"])
        return {'movie' : element }
    
    def put(self, id):
        informations =  json.loads(request.data)
        movie.update_one({ '_id': ObjectId(id) }, {'$set': informations})
        return {'id': str(id)}

    def delete(self, id):
        movie.delete_one({"_id": ObjectId(id)})
        return {'delete' :str(id)}

    def post(self):
        informations =  json.loads(request.data)
        movie.insert_one(informations)
        return {'post' : 'success'}

api.add_resource(HelloWorld, '/', '/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)