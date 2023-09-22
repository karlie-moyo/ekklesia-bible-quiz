#!/usr/bin/env python3
"""Answer Module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, ForeignKey, Boolean
from typing import Dict


class Answer(BaseModel, Base):
    """Answer Class"""

    __tablename__ = 'answers'

    text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    question_id = Column(
        String(60), ForeignKey('questions.id'),
        nullable=False
    )

    def to_dict(self, detailed=False) -> Dict[str, str]:
        """Overrides parent's defualt"""
        obj = super().to_dict()

        # level - 1 heldback attributes
        attrs = ['question', 'question_id', 'is_correct']
        for attr in attrs:
            if attr in obj:
                obj.pop(attr)

        if detailed is True:
            return obj

        # level - 3 heldback attributes
        attrs = ['created_at', 'updated_at']
        for attr in attrs:
            if attr in obj:
                obj.pop(attr)

        return obj
