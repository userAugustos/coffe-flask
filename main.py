from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
  def get(self):
    print(self)
    data = pd.read_csv('users.csv')
    data = data.to_dict()
    return { 'data': data }, 200
  
  def post(self):
    parser = reqparse.RequestParser()
    # so the add_argument, just takes an item from the body or the query params. wherever it is
    parser.add_argument('userId', required=True)
    parser.add_argument('name', required=True)
    parser.add_argument('city', required=True)
    
    args = parser.parse_args()
    
    print(args)
    
    new_data = pd.DataFrame({
      'userId': args['userId'],
      'name': args['name'],
      'city': args['city'],
      'locations': [[]]
    })
    
    #read CSV
    data = pd.read_csv('users.csv')
    
    #app the provided values
    data = data._append(new_data, ignore_index=True)
    
    #save the CSV
    
    data.to_csv('users.csv', index=False)
    
    return { 'data': data.to_dict() }, 200

class Locations(Resource):
  pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
  # run with debug mode, make the server restart in code changes
  app.run(debug=True)