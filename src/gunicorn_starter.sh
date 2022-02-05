#!/bin/bash
gunicorn --config /app/gunicorn_config.py app.wsgi:app