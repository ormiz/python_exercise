from flask import Flask, escape, request
import numpy as np
import urllib
import urllib2
import cv2
import sys

app = Flask(__name__)

# Get user supplied values
cascPath = "haarcascade_frontalface_default.xml"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	req = urllib2.Request(url)
	try: resp = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		raise Exception('The server couldn\'t fulfill the request. Error code: {0}'.format(e.code))
	except urllib2.URLError as e:
		raise Exception('Failed to reach server. Reason: {0}'.format(e.reason))
		
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	if image is None:
		raise Exception('Invalid image format')
	# return the image
	return image

def detectd_faces(imageUrl):

	# Download the image
	image = url_to_image(imageUrl)
	
	# Make it gray
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
	# Return the length of the array
	return len(faces)
	

@app.route('/detectFaces/<path:url>')
def detect_faces_endpoint(url):
	try:
		detected_faces = detectd_faces(url)
		return "Faces: {}".format(detected_faces)
	except Exception as e:
		return str(e)

port = int(sys.argv[1])		
app.run(host='0.0.0.0', port=port)