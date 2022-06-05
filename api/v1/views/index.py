#!/usr/bin/python3
""" Index """
from models.user import User
from models.Comment import Comment
from models.follow import Follow
from models.like import Like
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [User, Like, Comment, Follow, Post]
    names = ["users", "likes", "comments", "follows", "posts"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
