# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-dev \
    build-essential \
    && apt-get clean

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Specify the default command to run the application
CMD ["python", "app0.py"]


