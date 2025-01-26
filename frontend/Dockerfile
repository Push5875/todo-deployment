FROM ubuntu:22.04

# Update and install Apache2
RUN apt-get update && apt-get install -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your website files to the Apache2 web directory
COPY index.html /var/www/html/

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Apache2 in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
