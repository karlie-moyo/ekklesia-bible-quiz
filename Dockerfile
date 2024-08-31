# Use the official Python image as the base image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN apt-get update && apt-get install -y wkhtmltopdf
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the container port
EXPOSE 5000

# Start the application
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
