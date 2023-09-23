#!/usr/bin/env python3
"""Flask Application Config"""
from models.enums import UserRole
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.cookie_auth import CookieAuth
from os import getenv
from models import redis


class AppConfig:
    USER_ROLES = [UserRole.admin, UserRole.contributor,
                  UserRole.customer, UserRole.editor, UserRole.member, UserRole.moderator, UserRole.user]
    AUTH = {
        'cookie': CookieAuth(),
        'token': SessionAuth(redis=redis),
    }[getenv('AUTH_TYPE')]
    SECRET_KEY = getenv('API_SECRET_KEY')
