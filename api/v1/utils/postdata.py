#!/usr/bin/env python3
"""Get post/put data from flask request"""

from flask import request
from typing import Dict


def postdata() -> Dict[str, str]:
    """Return obj of <class 'dict'> or None"""
    if request.get_json(silent=True):
        data = request.get_json(silent=True)
    elif request.form:
        data = request.form
    else:
        return None

    return data.copy()


def postjson() -> Dict[str, str]:
    """Return obj of <class 'dict'> or None"""
    return request.get_json(silent=True)


def postform() -> Dict[str, str]:
    """Return obj of <class 'dict'> or None"""
    return request.form
