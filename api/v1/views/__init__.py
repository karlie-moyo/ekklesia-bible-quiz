#!/usr/bin/env python3
"""Views Module"""

from flask import Blueprint, jsonify
from models import storage, mail
from api.v1.utils.postdata import postdata
from api.v1.views.utils.auth_wrapper import login_required

app_views = Blueprint('app_views', __name__, url_prefix='/v1/')

from api.v1.views.users import *  # noqa
from api.v1.views.authentication import *  # noqa
from api.v1.views.questions import *  # noqa
