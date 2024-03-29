# Base image
FROM python:3.9-slim-buster

# Create a directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the main.py file
CMD python ./index.py