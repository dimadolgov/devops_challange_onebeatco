### Instructions for Using the Repository

## Prerequisites
  Docker: Ensure that Docker is installed on your machine. If not, you can download it from 

## Clone the Repository
  gh repo clone dimadolgov/devops_challange_onebeatco
  cd devops_challange_onebeatco

## Install the required Python dependencies:
  pip install -r requirements.txt

## Build the Docker image:
  docker build -t onebeatco .

## Run the Application
  docker-compose up 
  docker run -p 5000:5000 onebeatco
  #This command will start the Flask application inside a Docker container. The application will be accessible at http://127.0.0.1:5000/users




Additional Notes
The app.py file contains the main Flask application logic.
The Dockerfile defines the Docker image for the application.
The docker-compose.yml file manages the services and their configurations.
The test_app.py file contains a simple test suite for the Flask application.

