# Use a lightweight Python image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Install dependencies (only Flask)
RUN pip install flask

# Copy the application code
COPY app.py .

# Command to run the application
CMD ["python", "app.py"]
