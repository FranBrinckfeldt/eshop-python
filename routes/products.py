from flask import Blueprint, jsonify, request, abort, g
from models.ProductSchema import ProductSchema
from controller.products import get_product_by_id, get_all_products, insert_product, delete_product, update_product
from middlewares import is_auth

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route('/', methods=['GET'])
def get_products():
    return jsonify(get_all_products())

@products_blueprint.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = get_product_by_id(id)
    if product is None:
        abort(404)
    return product

@products_blueprint.route('/', methods=['POST'])
@is_auth
def post_product():
    product = request.get_json()
    try:
        ProductSchema().load(product)
    except:
        abort(400)
    return insert_product(product)

@products_blueprint.route('/<int:id>', methods=['PUT'])
@is_auth
def put_product(id):
    product = get_product_by_id(id)
    if product is None:
        abort(404)
    data = request.get_json()
    try:
        ProductSchema().load(data)
    except:
        abort(400)
    product.update(data)
    return update_product(product, id)

@products_blueprint.route('/<int:id>', methods=['DELETE'])
@is_auth
def remove_product(id):
    return delete_product(id)