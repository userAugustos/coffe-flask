from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
  def get(self):
    print(self)
    data = pd.read_csv('data/data/users.csv')
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
    
    # read CSV
    data = pd.read_csv('data/users.csv')
    
    if args['userId'] in list(data['userId']):
      return {
        'message': f"{args['userId']} already exists."
      }, 401
      
    new_data = pd.DataFrame({
    'userId': args['userId'],
    'name': args['name'],
    'city': args['city'],
    'locations': [[]]
    })
    
    # apply the provided values
    data = data._append(new_data, ignore_index=True)
    
    # save the CSV
    
    data.to_csv('data/users.csv', index=False)
    
    return { 'data': data.to_dict() }, 200
  
  def put(self):
    parser = reqparse.RequestParser()
    
    parser.add_argument('userId', required=True)
    parser.add_argument('location', required=True)
    
    args = parser.parse_args()
    
    data = pd.read_csv('data/users.csv')
    
    print(list(data['userId']))
    
    # so we search if the passed id existis in the csv
    if args['userId'] in list(data['userId']):
      # if it does, we transform the location csv in mutiple lists
      data['locations'] = data['locations'].apply(
        lambda x: ast.literal_eval(x)
      )
      print(type(data['locations']))
      
      # search in our csv if user passed already has that location
      for index, item in enumerate(data['userId']):
        if item == args['userId']:
          print(f"find user {item}, in {index}")
          for item in data['locations'][index]:
            if item == args['location']:
              return { 'message': f"Location {args['location']} already exists in {data['locations'][index]}" }, 404
      
      user_data = data[data['userId'] == args['userId']]
      
      # this is a panda thing to update the csv safely
      user_data.loc['locations'] = user_data.loc[:, 'locations'].values[0].append(args['location'])
      
      data.to_csv('data/users.csv', index=False)
      
      return { 'data': data.to_dict() }, 200
    
    return { 'message': f"{args['userId']} user not found" }, 404
  
  def delete(self):
    parser = reqparse.RequestParser()
    
    parser.add_argument('userId', required=True)
    
    args = parser.parse_args()
    
    data = pd.read_csv('data/users.csv')
    
    for index, item in enumerate(data['userId']):
      if data['userId'][index] == args['userId']:
        data = data.drop(index)
        # we transform the csv into a python dataFrame, then we remove the row at that index, after that, we re_write the csv
        data.to_csv('data/users.csv', index=False)
        # 
        print(f"find: {data}")
        return { 'data': data.to_dict() }, 200
    
    return { 'message': 'user not found' }, 404
    

class Locations(Resource):
  pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
  # run with debug mode, make the server restart in code changes
  app.run(debug=True)