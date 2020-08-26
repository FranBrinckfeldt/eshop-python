from flask import Blueprint, jsonify, request, abort
from ..models import CustomerSchema
from ..controller import customer_register, customer_login

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route('/register', methods=['POST'])
def post_customer():
    customer = request.get_json()
    return customer_register(customer)

@customers_blueprint.route('/login', methods=['POST'])
def login_customer():
    customer = request.get_json()
    if customer is not None and customer.get('email') is not None and customer.get('password') is not None:
        return customer_login(customer['email'], customer['password'])
    else:
        abort(400)