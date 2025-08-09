@echo off
chcp 65001 >nul 2>&1
echo Starting AI Novel Writing Assistant...
echo.

:: Change to script directory
cd /d "%~dp0"

:: Create and activate virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo ERROR: Failed to create virtual environment!
        pause
        exit /b 1
    )
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)

:: Start application
echo.
echo Starting Flask application...
echo Access URL: http://localhost:60001/bingte
echo Press Ctrl+C to stop the server
echo.
python app.py

pause
