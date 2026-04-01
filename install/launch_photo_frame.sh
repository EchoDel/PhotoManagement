#!/bin/bash
cd /home/raspberry/PhotoManagement
/home/raspberry/.local/bin/poetry install --with photo_frame
/home/raspberry/.local/bin/poetry run launch_photo_frame
