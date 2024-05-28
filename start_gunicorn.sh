#!/bin/bash

# Change to your project directory
cd /home/ubuntu/utils_server/color_changer/

# Run Gunicorn with your configuration file
gunicorn --config gunicorn_config.py app:app
