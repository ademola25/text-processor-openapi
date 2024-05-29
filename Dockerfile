# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies required for general compatibility
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
# ENV OPENAI_API_KEY=your-api-key

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]