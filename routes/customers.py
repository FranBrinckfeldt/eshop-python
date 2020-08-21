from flask import Blueprint, jsonify, request, abort
from models.CustomerSchema import CustomerSchema
from controller.customers import customer_register

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route('/register', methods=['POST'])
def post_customer():
    customer = request.get_json()
    return customer_register(customer)