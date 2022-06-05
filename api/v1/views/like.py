#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.like import Like
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/likes', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_likes():
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_likes = storage.all(Like).values()
    list_likes = []
    for like in all_likes:
        list_likes.append(like.to_dict())
    return jsonify(list_likes)


@app_views.route('/likes/<post>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_postlikes(post):
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_likes = storage.all(Like).values()
    list_likes = []
    for like in all_likes:
        if(like.post == post):
            list_likes.append(like.to_dict())
    return jsonify(list_likes)

