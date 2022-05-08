# Webserver for a ML Model to predict Wine class with Fast API & Docker

## System requirements
- Docker
- Python 3.7
- Fast API
- Pickle

## Setup
### Build the image
Within the root directory run 

```Dockerfile
docker build
```
To specify a tag:

```Dockerfile
docker build -t mlep:wine .
```
### Run the container
```Dockerfile
docker run --rm -p 80:80 mlep:wine
```
### Other resources
- Best practices for writing Dockerfiles https://docs.docker.com/develop/develop-images/dockerfile_best-practices/