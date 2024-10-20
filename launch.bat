@echo off

:: Check if python is available, if not try py explicitly
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found, trying py...
    py --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Neither python nor py is available in PATH. Please install Python or add it to PATH.
        exit /b 1
    )
    set PYTHON_CMD=py
) else (
    set PYTHON_CMD=python
)

:: Check if the virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating a new one...
    %PYTHON_CMD% -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment. Ensure Python is installed and available in PATH.
        exit /b 1
    )
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Install required packages from requirements.txt
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    exit /b 1
)

:: Run the overarching Python script
%PYTHON_CMD% launch.py
if errorlevel 1 (
    echo Failed to run launch.py.
    exit /b 1
)

echo All tasks completed successfully!
pause
