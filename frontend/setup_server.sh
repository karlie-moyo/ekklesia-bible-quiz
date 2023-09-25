#!/bin/bash
# Sets up your web servers for the deployment

# Install nginx
apt update
apt -y install nginx

# Create Project directories
mkdir -p /data/mindpal/releases/test/

# create initial page for test
cat << EOF | tee /data/mindpal/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Welcome to Kamva Mindpal.
  </body>
</html>
EOF

# create a symlink to test dir
ln -sf /data/mindpal/releases/test/ /data/mindpal/current

# manage permissions
chown -R ubuntu:ubuntu /data/mindpal/
