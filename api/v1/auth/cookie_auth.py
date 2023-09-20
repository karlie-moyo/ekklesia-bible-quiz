#!/usr/bin/env python3
"""Session Auth using Python Dict"""
from api.v1.auth import Auth
from models import storage
from models.user import User
from flask import session


class CookieAuth(Auth):
    """Cookie Auth Class"""

    def create_session(self, user_id: str = None) -> str:
        """Creates a session for user_id"""
        if user_id is None:
            raise ValueError('Missing user_id')
        session['id'] = user_id
        return ''

    def get_user_id(self, session=session) -> str:
        """Returns value: user_id of a matching Token"""
        return session.get('id')

    def current_user(self) -> User:
        """Overloads and get the current active user"""
        user_id = self.get_user_id()
        if user_id is None:
            raise ValueError('user_id not found')
        return storage.get(User, user_id)

    def destroy_session(self, session=session):
        """Destroys session if exists"""
        session.clear()
