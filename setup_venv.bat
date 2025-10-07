@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo Virtual environment setup complete!
echo ========================================
echo.
echo To activate in future, run:
echo   venv\Scripts\activate
echo.
echo To run setup_supabase.py:
echo   python setup_supabase.py
echo.
pause
