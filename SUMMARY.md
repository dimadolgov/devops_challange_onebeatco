# Development Process Summary

## 1. Flask Application (user_data.py)

### Overview:
- Created a simple Flask application with two routes: `/users` and `/health`.
- The `/users` route fetches user data from the JSONPlaceholder API, extracts name and email, and publishes it to a specified endpoint.
- The `/health` route returns a JSON response indicating the health status of the application.

### Development Steps:
1. Set up a Flask application with two routes (`/users` and `/health`).
2. Implemented the logic to fetch user data from the JSONPlaceholder API, extract name and email, and publish it to an endpoint.
3. Created a health check endpoint to return a predefined JSON response.

## 2. Dockerfile

### Overview:
- Defined a Dockerfile to containerize the Flask application.
- Used a Python 3 base image, set the working directory, and installed the required dependencies.
- Copied the application files into the container and specified the command to run the application.

### Development Steps:
1. Defined a Dockerfile with the necessary instructions.
2. Used the `python` base image and set the working directory.
3. Installed the required dependencies from the `requirements.txt` file.
4. Copied the application files into the container.
5. Specified the command to run the Flask application.

## 3. Docker Compose (docker-compose.yml)

### Overview:
- Created a Docker Compose file to manage the services.
- Defined a service named `onebeatco` using the Dockerfile in the current directory.
- Mapped port 5000 on the host to port 5000 in the container.

### Development Steps:
1. Created a `docker-compose.yml` file.
2. Defined a service named `onebeatco` using the local Dockerfile.
3. Mapped port 5000 on the host to port 5000 in the container.

