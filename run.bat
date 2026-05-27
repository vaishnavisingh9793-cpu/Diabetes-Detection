@echo off
cd /d "%~dp0"

echo Activating virtual environment...
call .venv\Scripts\activate

echo Starting Diabetes Detection Website...
start http://127.0.0.1:8000

python app.py

pause