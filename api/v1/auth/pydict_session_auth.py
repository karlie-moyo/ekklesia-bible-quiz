#!/usr/bin/env python3
"""Session Auth using Python Dict"""
from api.v1.auth import Auth
from uuid import uuid4
from flask import request
from models import storage
from models.user import User
import os

token_name = os.getenv('AUTH_TOKEN_NAME_ON_HEADER')


class SessionAuth(Auth):
    """Session Auth Class"""

    session_dict = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session for user_id"""
        if user_id is None:
            raise ValueError('Missing user_id')

        token = str(uuid4())
        self.session_dict.update({token: user_id})
        return token

    def get_user_id(self, token: str = None) -> str:
        """Returns value: user_id of a matching Token"""
        if token is None:
            raise ValueError(
                'Missing {token_name}'.format(token_name=token_name))

        return self.session_dict.get(token, None)

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
        data = self.session_dict.pop(token, None)
        if data is None:
            raise ValueError(
                'Invalid {token_name}'.format(token_name=token_name))
        return None
