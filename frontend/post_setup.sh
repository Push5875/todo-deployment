#!/bin/bash

# Fetch the public IP of the EC2 instance
PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

# File containing the HTML code
HTML_FILE="index.html"  

# Replace the placeholder with the public IP
sed -i "s|__PUBLIC_IP__|$PUBLIC_IP|g" $HTML_FILE

echo "Public IP $PUBLIC_IP has been set in $HTML_FILE"
