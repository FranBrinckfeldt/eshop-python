#TODO: Error Handling
#TODO: Authentication

from flask import Blueprint, jsonify, request, abort
from models.CategorySchema import CategorySchema
from controller.categories import get_category_by_id, get_all_categories, insert_category, delete_category, update_category

categories_blueprint = Blueprint('categories_blueprint', __name__)

@categories_blueprint.route('/', methods=['GET'])
def get_categories():
    return jsonify(get_all_categories())

@categories_blueprint.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = get_category_by_id(id)
    if category is None:
        abort(404)
    return category

@categories_blueprint.route('/', methods=['POST'])
def post_category():
    category = request.get_json()
    return insert_category(category)

@categories_blueprint.route('/<int:id>', methods=['PUT'])
def put_category(id):
    category = get_category_by_id(id)
    if category is None:
        abort(404)
    data = request.get_json()
    category.update(data)
    return update_category(category, id)

@categories_blueprint.route('/<int:id>', methods=['DELETE'])
def remove_category(id):
    return delete_category(id)