@echo off
echo 🚀 Starting AI Browser Agent...

:: Ensure pip is upgraded
python -m pip install --upgrade pip

:: Install dependencies
pip install -r requirements.txt

:: Install Playwright Chromium
python -m playwright install chromium

:: Set Python path
set PYTHONPATH=%cd%

:: Start FastAPI server
start /B python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

:: Start Gradio UI
python frontend\web_ui.py
