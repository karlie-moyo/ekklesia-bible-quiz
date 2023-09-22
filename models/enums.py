#!/usr/bin/env python3
"""Defines a set of Enum classes"""

from enum import Enum


class UserRole(Enum):
    """User roles for role based actions"""
    admin = "admin"
    moderator = "moderator"
    editor = "editor"
    contributor = "contributor"
    member = "member"
    user = "user"
    customer = "customer"

    def to_dict(self):
        return self.value

    @property
    def all(self):
        """Returns all available roles"""
        return list(self.__members__.values())
