# Rockstar 5G | Week 1 - Evaluation

This project is the evaluation of the first week in Enroute System Rockstar G5
apprenticeship.

## Prerequisite
- Docker
- Python

## Instructions
- Clone repository
```
git clone https://github.com/jubaan/w1-rockstarG5-julio-anoveros.git
```
- Build the docker image
```
docker build -t csv-reader .
```
- Run the image
```
docker run --name csv-container -d -p 5050:5050 -v $(pwd)/data:/usr/src/app/data
csv-reader
```
- Stop the image and remove it
```
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
```
- Open link in your preferred browser
