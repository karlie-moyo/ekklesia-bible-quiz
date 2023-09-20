#!/usr/bin/env python3
"""Authentication Wrapper"""
from api.v1.config import AppConfig
from flask import g, abort
from functools import wraps


def login_required(authorized_roles=None):
    """Wrapper method for all protected routes"""

    # check if USER_ROLES exists on AppConfig
    if not hasattr(AppConfig, 'USER_ROLES'):
        raise Exception('Missing USER_ROLES attribute on AppConfig')
    elif type(AppConfig.USER_ROLES) is not list:
        raise Exception('AppConfig.USER_ROLES is not a list')
    elif len(AppConfig.USER_ROLES) == 0:
        raise Exception('AppConfig.USER_ROLES cannot be empty')

    authorized_roles = AppConfig.USER_ROLES if authorized_roles is None else authorized_roles

    def login_wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            def denied():
                abort(401)

            if g.user is None:
                return denied()
            if g.user.role not in authorized_roles:
                return denied()
            return f(*args, **kwargs)
        return decorated_function
    return login_wrapper
