#!/bin/bash
rm ./instance/app.db

FLASK_ENV=development DATABASE_URI=sqlite:///app.db python manage.py
FLASK_ENV=development DATABASE_URI=sqlite:///app.db pytest
