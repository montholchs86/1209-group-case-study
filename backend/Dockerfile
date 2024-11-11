# Use Python official image as a base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install necessary dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files to the container
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]