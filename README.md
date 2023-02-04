# Technical_Interview_Take-Home_Exercise--SKIMS
This repository contains a solution for the Technical Interview Take-Home Exercise for the SKIMS company. The solution is built using Flask and implements a RESTful API.
## Requirements
* Requests
* Flask
* Docker

## Usage

### Clone the repo
`https://github.com/kdp19742/Technical_Interview_Take-Home_Exercise--SKIMS.git`

### If running locally

1. Install the required packages:
`pip install -r  requirements.txt`

2. Run the Flask application:
`flask --app pokemon.py run --host 0.0.0.0`

### If using docker

1. Install docker

2. Build the docker image
`docker build -t <image-name> <path>`

3. Run the docker container
`docker run -p 5000:5000 <image-name>`

 