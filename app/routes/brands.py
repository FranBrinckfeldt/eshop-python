#TODO: Error Handling
#TODO: Authentication

from flask import Blueprint, jsonify, request, abort
from ..models import BrandSchema
from ..controller import get_brand_by_id, get_all_brands, insert_brand, delete_brand, update_brand

brands_blueprint = Blueprint('brands_blueprint', __name__)

@brands_blueprint.route('/', methods=['GET'])
def get_brands():
    return jsonify(get_all_brands())

@brands_blueprint.route('/<int:id>', methods=['GET'])
def get_brand(id):
    brand = get_brand_by_id(id)
    if brand is None:
        abort(404)
    return brand

@brands_blueprint.route('/', methods=['POST'])
def post_brand():
    brand = request.get_json()
    return insert_brand(brand)

@brands_blueprint.route('/<int:id>', methods=['PUT'])
def put_brand(id):
    brand = get_brand_by_id(id)
    if brand is None:
        abort(404)
    data = request.get_json()
    brand.update(data)
    return update_brand(brand, id)

@brands_blueprint.route('/<int:id>', methods=['DELETE'])
def remove_brand(id):
    return delete_brand(id)