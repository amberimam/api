from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

db = open('db.json', 'r')
products = json.loads(db.read())
db.close()

#import pdb; pdb.set_trace()

class Product(Resource):
    def get(self, product_id):
        return products[product_id]

class Products(Resource):
    def get(self):
        return products

api.add_resource(Product, '/products/<int:product_id>')
api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(debug=True)

