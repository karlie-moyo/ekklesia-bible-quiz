#!/usr/bin/env python3
"""basemodel from which all other classes will inherit from"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, String, DateTime
)
from datetime import datetime
from uuid import uuid4
from typing import Dict

import models

Base = declarative_base()


class BaseModel:
    """BaseModel"""
    id = Column(String(60), default=lambda: str(uuid4()), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)

    def save(self):
        """Create and save `obj` to storage"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete `obj` from storgae"""
        models.storage.delete(self)
        models.storage.save()

    def to_dict(self) -> Dict[str, str]:
        """Returns a dictionary representation of an obj"""
        obj = {}
        obj.update(self.__dict__)

        # Format datetime objects
        __pstr = "%Y-%m-%d %H:%M:%S.%f"
        for attr in ['created_at', 'updated_at']:
            if obj.get(attr):
                obj.update({attr: str(obj.get(attr).strftime(__pstr))})

        # Held back attributes
        attrs = ['_sa_instance_state']
        for attr in attrs:
            if obj.get(attr):
                obj.pop(attr)
        return obj
