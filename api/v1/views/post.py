#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/posts', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_posts():
    """
    Retrieves the list of all posts objects
    or a specific posts
    """
    all_posts = storage.all(Post).values()
    list_posts = []
    for post in all_posts:
        list_posts.append(post.to_dict())
    return jsonify(list_posts)

@app_views.route('/posts/<post_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_post(post_id):
    """ Retrieves an user """
    post = storage.get(Post, post_id)
    if not post:
        abort(404)

    return jsonify(post.to_dict())


@app_views.route('/post/create', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def create_post():
    """
    Creates a user
    """
    print("not working")
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)