from flask import Flask, escape, request
from face_detect import detectFaces

app = Flask(__name__)

@app.route('/detectFaces/<path:url>')
def detectFacesEndpoint(url):
    return detectFaces(url)