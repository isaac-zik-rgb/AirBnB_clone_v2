#!/usr/bin/env bash
# SET UP WEB SERVERS FOR THE DEPLOYMENT OF web_static

# Update package list and install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Allow HTTP traffic through UFW
sudo ufw allow 'Nginx HTTP'

# Create directory structure and index.html
HTML_CONTENT="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

WEB_STATIC_DIR="/data/web_static"
sudo mkdir -p "$WEB_STATIC_DIR"/{releases/test,shared}
echo "$HTML_CONTENT" | sudo tee "$WEB_STATIC_DIR"/releases/test/index.html > /dev/null

# Delete the existing symbolic link if it exists
sudo rm -f "$WEB_STATIC_DIR"/current

# Create a new symbolic link to current
sudo ln -s "$WEB_STATIC_DIR"/releases/test/ "$WEB_STATIC_DIR"/current

# Ensure that the sites-enabled directory exists
sudo mkdir -p /etc/nginx/sites-enabled/

# Change ownership to ubuntu user
sudo chown -R ubuntu:ubuntu "$WEB_STATIC_DIR"

# Configure Nginx
NGINX_CONFIG="
server {
    listen 80;
    listen [::]:80;
    server_name 100.26.20.18;

    location /hbnb_static/ {
        alias $WEB_STATIC_DIR/current/;
    }

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
    }
}
"

echo "$NGINX_CONFIG" | sudo tee /etc/nginx/sites-available/hbnb_static > /dev/null
sudo ln -sf /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo service nginx restart
