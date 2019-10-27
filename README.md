# python_exercise

To pull docker image:
docker pull ormi2/python-exercise

I used Flask as my server framework and took part of the code from https://github.com/shantnu/FaceDetect for detection.
The main file is face_detect_server.py.

The program can get port number from outside, for example:
python face_detect_server.py 5000.

Since the program can receive the port argument, You can specify the port inside the Dockerfile in the CMD line.
To build the docker image:
docker build -t python-exercise:latest .
To run a container with port 5000 (should match the port inside the Dockerfile):
docker run -p 5000:5000 python-exercise

The main endpoint of the server is:
http://{server}:{port}/detectFaces/{encodedURL}

for example:
http://localhost:5000/detectFaces/https%3A%2F%2Fclemenssiebler.com%2Fwp-content%2Fuploads%2F2018%2F09%2Fface_api_test.jpg

This should return a string "Faces: 2"