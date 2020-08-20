from flask import Blueprint

http_errors = Blueprint('http_errors', __name__)

@http_errors.app_errorhandler(400)
def handle_400(err):
    return {'message': 'BAD_REQUEST'}, 400

@http_errors.app_errorhandler(403)
def handle_403(err):
    return {'message': 'FORBIDDEN'}, 403

@http_errors.app_errorhandler(404)
def handle_404(err):
    return {'message': 'NOT_FOUND'}, 404

@http_errors.app_errorhandler(405)
def handle_405(err):
    return {'message': 'METHOD_NOT_ALLOWED'}, 405

@http_errors.app_errorhandler(409)
def handle_409(err):
    return {'message': 'CONFLICT'}, 409

@http_errors.app_errorhandler(500)
def handle_500(err):
    return {'message': 'INTERNAL_SERVER_ERROR'}, 500
