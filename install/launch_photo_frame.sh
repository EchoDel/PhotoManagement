#!/bin/bash
cd /home/pi/PhotoManagement
/home/pi/.local/bin/poetry install --with photo_frame
/home/pi/.local/bin/poetry run launch_photo_frame
