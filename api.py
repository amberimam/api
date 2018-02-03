from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from flask import Flask
from flask_restful import abort, Resource, Api
import json
from webargs import fields
from webargs.flaskparser import use_kwargs


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

class Product(Resource):
    def get(self, product_id):
        if product_id >= 0 and product_id < len(products):
            return products[product_id]
        else:
            abort(404, message="Product {} doesn't exist".format(product_id))

class Products(Resource):
    args = {
        'category': fields.Str(required=False)
    }

    @use_kwargs(args)
    def get(self, category):
        if category:
            return [p for p in products if category in p['categories']]
        else:
            return products

api.add_resource(Product, '/products/<int:product_id>')
api.add_resource(Products, '/products')


if __name__ == '__main__':
    app.run(debug=True)

