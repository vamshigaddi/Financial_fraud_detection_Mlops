# Use the official Python image from the Docker Hub
FROM python:3.9-slim

RUN apt update -y && apt install awscli -y

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first for caching dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run your Flask application
CMD ["python", "app.py"]

