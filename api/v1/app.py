#!/usr/bin/env python3
"""Python Flask Application Module: RESTFul API"""

from flask import Flask, jsonify, g
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.config import AppConfig
from os import getenv
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_object(AppConfig)
app.register_blueprint(app_views)
CORS(app, resources={r'/v1/*': {'origins': '*'}},
     supports_credentials=True)


@app.before_request
def app_setup_context():
    """App Setup Context"""
    auth = app.config['AUTH']
    try:
        g.user = auth.current_user()
    except ValueError:
        g.user = None


@app.teardown_appcontext
def close_storage(exception=None):
    """Close any active SQLAlchemy sessions"""
    storage.close()


@app.get('/status')
def status_page():
    return jsonify({
        "status": True,
        "message": "Still up.",
        "data": None
    }), 200


@app.errorhandler(400)
def bad_request(error) -> str:
    """Bad Request Error Handler"""
    return jsonify({
        "status": "error",
        "message": "Bad Request",
        "data": None
    }), 400


@app.errorhandler(401)
def unathorized(error) -> str:
    """Unathorized Error Handler"""
    return jsonify({
        "status": "error",
        "message": "Unauthorized",
        "data": None
    }), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden Error Handler"""
    return jsonify({
        "status": "error",
        "message": "Forbidden",
        "data": None
    }), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({
        "status": "error",
        "message": "Not found",
        "data": None
    }), 404


@app.errorhandler(405)
def method_not_allowed(error) -> str:
    """Method not allowed error handler"""
    return jsonify({
        "status": "error",
        "message": "Method not allowed",
        "data": None
    }), 405


@app.errorhandler(422)
def unprocessable_entity(error) -> str:
    """Unprocessable entity handler"""
    return jsonify({
        "status": "error",
        "message": "Data integrity error",
        "data": None
    }), 422


@app.errorhandler(500)
def server_error(error) -> str:
    """Internal Server Error Handler"""
    return jsonify({
        "status": "error",
        "message": "Internal Server Error",
        "data": None
    }), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, load_dotenv=True,
            debug=getenv('DEBUG', False))
