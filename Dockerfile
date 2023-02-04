# Use an official Python runtime as the parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the files to the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=pokemon.py

# Expose the default Flask port
EXPOSE 5000

# Define the command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
