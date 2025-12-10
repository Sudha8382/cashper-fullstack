@echo off
echo ========================================
echo   Cashper Backend Server Startup
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Virtual environment not found. Creating...
    python -m venv venv
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install/Update dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo ========================================
echo   Starting Cashper Backend API Server
echo ========================================
echo.
echo Server will be available at:
echo   - http://localhost:8000
echo   - API Docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Start the server
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000

