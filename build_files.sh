#!/bin/bash
echo "BUILDING PROJECT ON VERCEL..."
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
echo "BUILD ENDED."
