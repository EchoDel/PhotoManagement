#!/bin/bash
# Check for updates
cd /home/pi/PhotoManagement/
git fetch
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse @{u})
if [ $LOCAL != $REMOTE ]; then
echo "Repository is outdated. Updating…"
# git pull
# Download updates
# git checkout master
git pull
# Stop the service
sudo systemctl stop PhotoFrame.service
# Build and update the requirements and package
poetry install
poetry build
# Restart the application
sudo systemctl start PhotoFrame.service
else
echo "Repository is up to date."
fi
