#!/bin/sh

echo "Starting kpk server"
source /home/vladislav/virtual/bin/activate && \
python "sources/my_messenger/manage.py" runserver 0.0.0.0:8011