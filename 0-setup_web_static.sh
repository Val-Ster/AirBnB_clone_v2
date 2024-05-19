#!/bin/bash

# Install Nginx if it is not already installed
if ! which nginx > /dev/null 2>&1; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu /data/

# Update Nginx configuration
nginx_config="server {
    listen 80;
    server_name localhost;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
    
    location / {
        try_files \$uri \$uri/ =404;
    }
}"

# Backup the default Nginx config file
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak

# Write the new configuration
echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo systemctl restart nginx
