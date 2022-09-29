#!/usr/bin/env bash
# This script sets up your web servers for the deployment of "web_static"

apt-get update -y
apt-get install nginx -y
ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
    <head>
        <title>davidkyalo</title>
    </head>
    <body>
        <h1>Success! Web server working</h1>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
chmod -R 755 /data
line="\\\tlocation \/hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}"
sed -i "30i $line" /etc/nginx/sites-available/default
service nginx restart
