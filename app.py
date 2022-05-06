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
        return {'get' : element }
    
    def put(self, id):
        informations =  json.loads(request.data)
        movie.update_one({ '_id': ObjectId(id) }, {'$set': {'title': informations['title'], 'description': informations['description'], 'duration': informations['duration'] }})
        return {'id': str(id)}

    def delete(self, id):
        element = movie.delete_one({"_id": ObjectId(id)})
        # element["_id"] = str(element["_id"])
        return {'delete' :str(id)}

    def post(self):
        informations =  json.loads(request.data)
        movie.insert_one( {'title': informations['title'], 'description': informations['description'], 'duration': informations['duration'] } )
        return {'post' : 'sucess'}

api.add_resource(HelloWorld, '/', '/<string:id>')

# request

# get
# requests.get('http://127.0.0.1:5000/62751ef9cc83db8478d76f4c').json()

# put
# requests.put('http://127.0.0.1:5000/62751ef9cc83db8478d76f4c', json = {"title": "The Batman","description":"bijour","duration":"2h40"}).json()

# post
# requests.post('http://127.0.0.1:5000/', json = {"title": "TEST","description":"bijour","duration":"2h40"})

# delete
# requests.delete('http://127.0.0.1:5000/62751ef9cc83db8478d76f4c')


if __name__ == '__main__':
    app.run(debug=True)