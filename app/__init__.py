from flask import Flask, jsonify
from .routes import products_blueprint, brands_blueprint, categories_blueprint, customers_blueprint
from .errors import http_errors

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return 'e-Shop Flask'

app.register_blueprint(products_blueprint, url_prefix = '/products')
app.register_blueprint(brands_blueprint, url_prefix = '/brands')
app.register_blueprint(categories_blueprint, url_prefix = '/categories')
app.register_blueprint(customers_blueprint, url_prefix = '/customers')

app.register_blueprint(http_errors)