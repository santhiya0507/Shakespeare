@echo off
echo ========================================
echo BardSpeak Deployment Script
echo ========================================
echo.

cd /d "%~dp0"

echo Current directory: %CD%
echo.

echo Step 1: Initialize Git...
git init
if %errorlevel% neq 0 (
    echo ERROR: Git init failed
    pause
    exit /b 1
)

echo Step 2: Add all files...
git add .

echo Step 3: Commit...
git commit -m "BardSpeak app ready for deployment"

echo.
echo ========================================
echo Git setup complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create repository on GitHub: https://github.com/new
echo 2. Name it: bardspeak
echo 3. Run these commands:
echo.
echo    git remote add origin https://github.com/santhiya0507/bardspeak.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Or use GitHub Desktop (easier):
echo    Download from: https://desktop.github.com
echo.
pause
