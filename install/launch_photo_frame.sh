#!/bin/bash
export DISPLAY=:0
cd /home/raspberry/PhotoManagement
/home/raspberry/.local/bin/poetry install --with photo_frame
/home/raspberry/.local/bin/poetry run launch_photo_frame
