@echo off
echo ========================================
echo Git Setup and Push for BardSpeak
echo ========================================
echo.

cd /d "%~dp0"

echo Initializing Git repository...
git init
if errorlevel 1 (
    echo Error: Failed to initialize Git
    pause
    exit /b 1
)

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Configure BardSpeak with Supabase database"

echo.
echo ========================================
echo Git repository initialized!
echo ========================================
echo.
echo Next steps:
echo 1. Create a repository on GitHub
echo 2. Run these commands:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
echo    git branch -M main
echo    git push -u origin main
echo.
pause
