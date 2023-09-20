#!/usr/bin/env python3
"""Users URI Module"""

from flask import abort, g
from api.v1.views import (
    app_views, storage, jsonify, postdata, login_required)
from models.user import User
from sqlalchemy.exc import IntegrityError
from typing import List
from models.enums import UserRole


@app_views.route('/users', methods=['GET'])
@login_required([UserRole.admin, UserRole.moderator])
def get_users():
    """Return all users in storage"""

    users: List[User] = storage.all(User).values()
    return jsonify({
        "status": "success",
        "message": "Users retrieved successfully",
        "data": {
            "users": [user.to_dict() for user in users],
            "total": len(users)
        }
    }), 200


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a User with a matching user_id"""
    user: User = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify({
        "status": "success",
        "message": "User retrieved successfully",
        "data": user.to_dict(detailed=True)
    })


@app_views.route('/users', methods=['POST'])
def create_users():
    """Create a new User
    """
    data = postdata()
    if data is None:
        abort(400)

    attrs = ['name', 'email']
    user_data: dict = {}
    for attr in attrs:
        if attr in data:
            user_data.update({attr: data.pop(attr)})
        else:
            return jsonify({
                "status": "error",
                "message": "Missing required data: " + attr,
                "data": None
            }), 400
    try:
        user = User(**user_data)
        user.save()
    except IntegrityError:
        storage.rollback()
        user = storage.match(User, email=user_data.get('email'))

    return jsonify({
        "status": "success",
        "message": "User created successfully",
        "data": user.to_dict(detailed=True)
    }), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
@login_required()
def update_user(user_id):
    """Updates user with a matching user_id"""
    data = postdata()
    if data is None:
        abort(400)
    user: User = storage.get(User, user_id)
    if user is None:
        abort(404)

    # validates g.user's access to update user data
    if g.user is not user:
        abort(401)

    # list of user attribues allowed to be updated
    user_data = {}
    attrs = ['name']
    for attr in attrs:
        if attr in data and data.get(attr, None) is not None:
            user_data.update({attr: data.get(attr)})
    try:
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
    except IntegrityError:
        storage.rollback()
        return jsonify({
            "status": "error",
            "message": "Phone number already registered with another account",
            "data": None
        })
    return jsonify({
        "status": "success",
        "message": "User data updated successfully",
        "data": user.to_dict(detailed=True)
    })


@app_views.route('/users/<user_id>', methods=['DELETE'])
@login_required([UserRole.admin])
def delete_user(user_id):
    """Delete from storage user with a matching user_id"""
    user: User = storage.get(User, user_id)
    if user is None:
        abort(404)

    storage.delete(user)
    storage.save()

    return jsonify({
        "status": "success",
        "message": "User deleted successfully",
        "data": None
    }), 200
