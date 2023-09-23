#!/usr/bin/env python3
"""Leaderboards URI"""

from models import storage
from models.result import Result
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/leaderboards', methods=['GET'])
def get_leaderboards():
    """Return a list of the top 25 attempts"""
    results = storage.all(Result).values()

    s_results = sorted(
        results, key=lambda x: x.score, reverse=True
    )

    leaderboards = [x.to_dict() for x in s_results[:25]]

    return jsonify({
        "status": "success",
        "message": "Leaderboards retrieved successfully",
        "data": {
            "count": len(leaderboards),
            "leaderboards": leaderboards
        }
    }), 200
