#!/usr/bin/env bash
# SET UP WEB SERVERS FOR THE DEPOLYMENT OF web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
FILE="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
echo "$FILE" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current && ln -s /data/web_static/releases/test/ /data/web_static/current
NGINX_CONFIG="
server {
       listen 80;
       listen [::]:80;
       server_name 100.26.20.18;
       location /hbnb_static {
       alias /data/web_static/current/;
       }
}
"
echo "$NGINX_CONFIG" | sudo tee /etc/nginx/sites-enabled/default > /dev/null
sudo service nginx restart
