#!/bin/bash

echo "🚀 Starting AI Browser Agent..."

# Ensure pip is upgraded
python3 -m pip install --upgrade pip

# Install dependencies
pip3 install -r requirements.txt

# Install Playwright Chromium
python3 -m playwright install chromium

export PYTHONPATH=$(pwd)
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
python3 frontend/web_ui.py

