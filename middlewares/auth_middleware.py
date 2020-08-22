from functools import wraps
from flask import request, abort, Response, jsonify, g
from utils import validate_token

def is_auth(func):
    @wraps(func)
    def _is_auth(*args, **kwargs):
        authorization = request.headers.get('Authorization')
        token_validation = validate_token(authorization)
        if token_validation[0]:
            g.token_payload = token_validation[1]
            return func(*args, **kwargs)
        else:
            abort(403)
    return _is_auth
