# Sum numbers

Sums 3 integers.

## Description

A flask application with APIS for summing up 3 intergers.

## Getting Started

### Dependencies

* python 3.9
* pip3
* Docker

### Installing

* Follow the link to install Docker in your machine (https://docs.docker.com/engine/install/)

### Hosting Flask application on the localhost.

* Run the requirements file to install all the dependencies.
```
pip3 install -r requirements.txt
```
* Once the dependencies are installed, use the following command to start the Flask application.
```
python api.py
```

### Hosting Flask application using Docker.
* After installing and starting the Docker on your local machine, ```cd``` to the directory where ```Dockerfile```
file is present.
* Run the following command to create an image of the application. This image will contain all the end to end resources and dependencies needed to run it on a container. Here ```docker_image_name``` is a custom name you can give to your docker image.
```
docker image build -t docker_image_name .
```
* To list all the images present on your system use
```
docker image ls
```
* Once the docker image is created, you can use the following command to create a container and run the application on it.
```
docker run -dti -p 5000:5000 docker_image_name
```

### Calling the APIs after hosting the application.
* Once the application is hosted either in the local machine or in Docker container, use the following curl command to call the APIs.

* Using the curl we can call the APIs deployed by the flask application. In the curl command, ```[1, 2, 3]``` are the numbers to be added. 
```
curl -H 'Content-Type: application/json' -X PUT  -d '[1,2,3]' http://localhost:5000/sum
```
* The curl command will return the follow response with HTTP status code 200.
```javascript
{
  "result": 6, 
  "status": 200
}
```

