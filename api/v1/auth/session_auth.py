#!/usr/bin/env python3
"""Session Auth using Redis key, value store"""
from api.v1.auth import Auth
from uuid import uuid4
from flask import request
from models import storage
from models.user import User
from os import getenv

token_name = getenv('AUTH_TOKEN_NAME_ON_HEADER')
REDIS_URL = getenv('REDIS_URL')
AUTH_TTL = getenv('AUTH_TTL', 259200)


class SessionAuth(Auth):
    """Session Auth Class"""

    key = 'flask_session_auth_tokens:{}'

    def __init__(self, redis) -> None:
        """Intializes Session Auth instance"""
        self.redis = redis
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """Creates a session for user_id"""
        if user_id is None:
            raise ValueError('Missing user_id')

        token = str(uuid4())
        self.redis.set(self.key.format(token), user_id)
        self.redis.expire(self.key.format(token), int(AUTH_TTL))
        return token

    def get_user_id(self, token: str = None) -> str:
        """Returns value: user_id of a matching Token"""
        if token is None:
            raise ValueError(
                'Missing {token_name}'.format(token_name=token_name))

        user_id: bytes = self.redis.get(self.key.format(token))
        if user_id is None:
            return None
        return user_id.decode('utf-8')

    def get_token_from_headers(self, request=request) -> str:
        """Returns a token from request.headers"""
        token = request.headers.get(token_name)
        if token is None:
            raise ValueError(
                'Missing {token_name}'.format(token_name=token_name))
        return token

    def current_user(self, request=request) -> User:
        """Overloads and get the current active user"""
        user_id = self.get_user_id(
            token=self.get_token_from_headers(request=request)
        )
        if user_id is None:
            raise ValueError('user_id not found')
        return storage.get(User, user_id)

    def destroy_session(self):
        """Destroys session if exists"""
        token = self.get_token_from_headers()
        if token is None:
            raise ValueError(
                'Missing {token_name}'.format(token_name=token_name))
        resp = self.redis.delete(self.key.format(token))
        if not resp:
            raise ValueError(
                'Invalid {token_name}'.format(token_name=token_name))
        return None
