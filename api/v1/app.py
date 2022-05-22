#1/usr/bin/python3

from models import storage 
from api.v1.views import app_views
from flask import Blueprint,Flask, jsonify,make_response
from flask_cors import CORS
import os

app =Flask(__name__)
app.register_blueprint(app_views)
CORS(app,origin="0.0.0.0")

@pp.teardown_appcontext
def tearthatmotherfuckerdown(self):
    """ tear that shit down"""
    storage.close()
@app.errorhandler(404)
def dudewermypage(e):
    """ dude where's page my page"""
    return make_response(jsonify({"erroe":"Not found"}),404)

if __name__ == '__main__':
    ho = os.getenv("API_HOST")
    po = os.getenv("API_PORT")

    if ho is None:
        ho = '0.0.0.0'
    
    if po is None:
        po = 5000
    
    app.run(host = ho, port = po, threaded = True, debug = True)
