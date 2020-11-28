[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield2]][linkedin-url2]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h2 align="center">Rockstar G5 | w1 - Evalutaion</h2>
  <p align="center">
    This repository is the part of the evaluations at Enroute Rockstar G5
    apprenticeship program (Nov 2020). The instructor for the first week was
    Javier Zepeda a Java Developer at Enroute Systems.
    <a href="https://github.com/jubaan/RockstarG5-Evaluation-Week1"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/jubaan/RockstarG5-Evaluation-Week1/issues">Report Bug</a>
    ·
    <a href="https://github.com/jubaan/RockstarG5-Evaluation-Week1/issues">Request Feature</a>
  </p>
</p>

## Table of Contents
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Installation guide](#instalation-guide)
* [Roadmap](#roadmap)
* [Contact](#contact)
* [Acknowledgments](#acknowldgements)
<!-- ABOUT THE PROJECT -->

## About The Project

This is the first evaluation of the program, the goals were to apply the
knowledge learned during the first week of the apprenticeship.

**Project requirements**
- Create a GitHub repository
- Develop a Python app with these features
  - Reads a CSV file
  - Converts its content to JSON format
- Use **Flask** to render the JSON output in the browser on port 5050 
- Deploy the app to **Linode** Cloud VM
- Use **Docker** to convert the app into a image container
- Run de application deatach
- Allow portforwarding and make the app availible through an `http` link

### Built With

The project was developed using the following technologies:
- Python 3 
- Docker
- Linode

## Instalation Guide

### Prerequisites

To be able to run the commands and have a working copy is necesary that your 
local enviroment has already
installed:
- Docker
- Docker Compose
- Python 3

### Installation

- Clone repository
```
git clone https://github.com/jubaan/RockstarG5-Evaluation-Week1.git
```
- `cd` into the repository directory

#### Run using -docker- command

- Build the docker image
```
docker build -t csv-reader .
```
- Run the image
```
docker run --name csv-container -d -p 5050:5050 -v $(pwd)/data:/usr/src/app/data
csv-reader
```
- Open link in your preferred browser
- Stop the image and remove it
```
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
```
#### Run using -docker-compose- command

- Run the container
```
docker-compose up -d
```
- Stop the container
```
docker-compose down
```
#### Known Issues

If you have run the `docker` version first and whant to run the
`docker-compose` alternative run this command:
```
docker-compose up -d --build
```
This will eliminate the image created with `docker` and build a new one
using `docker-build`.

## Roadmap

See the [open issues](https://github.com/jubaan/RockstarG5-Evaluation-Week1/issues) for a list of proposed features (and known issues).

## Contact
<p align="center">Project Link: <a href="https://github.com/jubaan/RockstarG5-Evaluation-Week1">RockstarG5 | w1 - Evaluation</a></p>
<p align="center">GitHub: <a href="https://github.com/jubaan">Julio Añoveros</a></p>
<p align="center" style="display: flex; justify-content: center; align-items: center;">
    <a target="_blank" href="https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=julio.ab@outlook.com
">
      julio.ab@outlook.com
    </a> &nbsp; |
    <a target="_blank" href="https://github.com/jubaan?tab=repositories">
        My Repositories
    </a> &nbsp; |
    <a target="_blank" href="www.linkedin.com/in/jubaan">
      LinkedIn
    </a> &nbsp; |
    <a target="_blank" href="https://twitter.com/AnoverosJulio">
      Twitter
    </a>
</p>

## Acknowledgements
- Javier Zepeda - Java Developer
- [Enroute](http://www.enroutesystems.com)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/jubaan/RockstarG5-Evaluation-Week1.svg?style=flat-square
[contributors-url]: https://github.com/jubaan/RockstarG5-Evaluation-Week1/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jubaan/RockstarG5-Evaluation-Week1.svg?style=flat-square
[forks-url]: https://github.com/jubaan/RockstarG5-Evaluation-Week1/network/members
[stars-shield]: https://img.shields.io/github/stars/jubaan/RockstarG5-Evaluation-Week1.svg?style=flat-square
[stars-url]: https://github.com/jubaan/RockstarG5-Evaluation-Week1/stargazers
[issues-shield]: https://img.shields.io/github/issues/jubaan/RockstarG5-Evaluation-Week1.svg?style=flat-square
[issues-url]: https://github.com/jubaan/RockstarG5-Evaluation-Week1/issues
[license-shield]: https://img.shields.io/github/license/jubaan/RockstarG5-Evaluation-Week1.svg?style=flat-square
[license-url]: https://github.com/jubaan/RockstarG5-Evaluation-Week1/blob/master/LICENSE.txt
[linkedin-shield2]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url2]: https://www.linkedin.com/in/jubaan/
