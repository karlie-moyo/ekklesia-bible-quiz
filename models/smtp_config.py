#!/usr/bin/env python3
"""SMTP Configurations module"""

from models.base_model import Base, BaseModel
from sqlalchemy import (
    Column, String, Integer, ForeignKey
)
from base64 import b64encode, b64decode
from typing import Dict


class SMTPConfig(BaseModel, Base):
    """Holds Users SMTP Configurations"""

    __tablename__ = 'smtp_configs'

    alias = Column(String(255), nullable=True)
    username = Column(String(255), nullable=False)
    _password = Column(String(255), nullable=False)
    server = Column(String(255), nullable=False)
    port = Column(Integer, default=587, nullable=False)
    rate = Column(Integer, default=50)  # mails/hour

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    @property
    def password(self) -> str:
        """Returns decoded SMTP password"""
        return b64decode(self._password.encode('utf-8')).decode('utf-8')

    @password.setter
    def password(self, password: str):
        """Setter for SMTP Config password"""
        self._password = b64encode(password.encode('utf-8')).decode('utf-8')

    def to_dict(self, detailed=False) -> Dict[str, str]:
        """Overrides parent's defualt"""
        obj = super().to_dict()

        # level - 1 heldback attributes
        attrs = ['_password', 'user']
        for attr in attrs:
            if attr in obj:
                obj.pop(attr)

        if detailed is True:
            obj.update({'password': self.password})
            return obj

        # level - 2 heldback attributes
        attrs = ['user_id', 'created_at', 'updated_at']
        for attr in attrs:
            if attr in obj:
                obj.pop(attr)

        return obj

    def to_json_serializable(self):
        return self.to_dict(detailed=True)

    @classmethod
    def from_json_serializable(cls, data):
        return cls(**data)
