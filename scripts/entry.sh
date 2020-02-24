#!/usr/bin/env bash

exec gunicorn wsgi:application --bind 0.0.0.0:5000
