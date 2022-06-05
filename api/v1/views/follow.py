#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.follow import Follow
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/follows', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_follows():
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_follows = storage.all(Follow).values()
    list_follow = []
    for follow in all_follows:
        list_follow.append(follow.to_dict())
    return jsonify(list_follow)

@app_views.route('/follows/<following>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_following(following):
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_follows = storage.all(Follow).values()
    list_follow = []
    for follow in all_follows:
        if(follow.followingId == following):
            list_follow.append(follow.to_dict())
    return jsonify(list_follow)



