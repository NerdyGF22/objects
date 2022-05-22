#1/usr/bin/python3
"""
views
"""
from flask import jsonify
from api.v1.views import app_views
from models.user import User

@app_views.route('/status')
def status():
    """ status route"""
    return jsonify({'status': 'ok'})

@pp_views.route('/stats')
def stats():
    from models import storage
    stats = dict()
    for k, c in classes.items():
        stats.update({k:storage.count(c)})
    return jsonify(stats)