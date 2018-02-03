from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from flask import Flask
from flask_restful import Resource, Api
import json


def init_product_list():
    db = open('db.json', 'r')
    products = json.loads(db.read())
    db.close()

    for index, product in enumerate(products):
        product['id'] = index

    return products


app = Flask(__name__)
api = Api(app)
products = init_product_list()

#import pdb; pdb.set_trace()

class Product(Resource):
    def get(self, product_id):
        if product_id >= 0 and product_id < len(products):
            return products[product_id]
        else:
            return None, 404

class Products(Resource):
    def get(self):
        return products

api.add_resource(Product, '/products/<int:product_id>')
api.add_resource(Products, '/products')



if __name__ == '__main__':
    app.run(debug=True)

