# Use a lightweight Python image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Install dependencies (Flask and requests)
RUN pip install flask requests

# Copy the application code
COPY app.py .

# Command to run the application
CMD ["python", "app.py"]
