#!/usr/bin/env python3
"""User authentication module"""
from sqlalchemy import Column, String
import bcrypt
from uuid import uuid4
from base64 import b64encode, b64decode


class UserAuth:

    reset_token = Column(String(255), nullable=True)
    _password = Column(String(255), nullable=True)

    @property
    def password(self) -> str:
        """User password getter"""
        return self._password

    @password.setter
    def password(self, value: str):
        """
        User password setter: hash with bcrypt before
        storing in the database.
        """
        if value is None or value == '':
            raise ValueError('User password cannot be null or empty string')
        self._password = bcrypt.hashpw(
            value.encode('utf-8'), bcrypt.gensalt(4)
        )

    def is_valid_password(self, password: str) -> bool:
        """Validate if password is a valid user password"""
        user_password = self.password
        if isinstance(user_password, str):
            user_password = user_password.encode('utf-8')
        return bcrypt.checkpw(
            password.encode('utf-8'), user_password
        )

    def is_valid_reset_token(self, reset_token: str) -> bool:
        """Validate if token is a valid user reset token"""
        return self.reset_token == reset_token

    def generate_reset_token(self) -> str:
        """Generates new user reset_token and return"""
        token = str(uuid4())
        self.reset_token = token
        return b64encode(token.encode('utf-8')).decode('utf-8')

    @staticmethod
    def decode_reset_token(encoded_token: str) -> str:
        """A static method for decoding base64 encoded token"""
        import binascii
        try:
            result = b64decode(
                encoded_token.encode('utf-8')
            ).decode('utf-8')
        except binascii.Error as exc:
            raise ValueError(str(exc))
        return result

    @staticmethod
    def update_user_password(encoded_token, new_password):
        """Update password for User with a matching token"""
        from models import storage
        from models.user import User

        user: User = storage.match(
            User, reset_token=User.decode_reset_token(encoded_token)
        )
        if user is None:
            raise ValueError('Invalid or expired token')
        setattr(user, 'password', new_password)
        setattr(user, 'reset_token', None)
        return user
