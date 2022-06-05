#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from soupsieve import comments
from models.Comment import Comment
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/comments', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_comment():
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_comments = storage.all(Comment).values()
    list_comments = []
    for comment in all_comments:
        list_comments.append(comment.to_dict())
    return jsonify(list_comments)


@app_views.route('/comments/<post>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_postcomments(post):
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_comments = storage.all(Comment).values()
    list_comments = []
    for comment in all_comments:
        if(comment.post == post):
            list_comments.append(comment.to_dict())
    return jsonify(list_comments)




