@echo off

:: Try using py with Python 3.10 explicitly
py -3.10 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo py for Python 3.10 not found, trying python...
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Neither py for Python 3.10 nor python is available in PATH. Please install Python 3.10 or add it to PATH.
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py -3.10
)

:: Check if the virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating a new one...
    %PYTHON_CMD% -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment. Ensure Python 3.10 is installed and available in PATH.
        exit /b 1
    )
)

:: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Ensure that the pip is up-to-date
python -m pip install --upgrade pip

:: Install required packages from requirements.txt
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    exit /b 1
)

:: Run the overarching Python script within the virtual environment
echo Running launch.py within the virtual environment...
python launch.py
if errorlevel 1 (
    echo Failed to run launch.py.
    exit /b 1
)

echo All tasks completed successfully!
pause
