# Dockerfile

# Use a lightweight Nginx base image as our foundation
FROM nginx:alpine

# Copy our custom index.html file into the default Nginx web root directory
COPY index.html /usr/share/nginx/html/index.html

# Tell Docker that the container will listen on port 80
EXPOSE 80

# The base image already has the CMD to start Nginx, so we don't need to add one.
