#!/bin/bash

gunicorn -w 2 -b 0.0.0.0 --chdir /opt/src app:app
