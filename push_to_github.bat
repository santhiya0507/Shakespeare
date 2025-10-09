@echo off
echo ========================================
echo Push BardSpeak to GitHub
echo Repository: https://github.com/santhiya0507/Shakespeare_club
echo ========================================
echo.

REM Change to script directory
cd /d "%~dp0"

echo Current directory: %CD%
echo.

REM Check if .git exists
if exist .git (
    echo Git repository already initialized
) else (
    echo Initializing Git repository...
    git init
    if %errorlevel% neq 0 (
        echo ERROR: Failed to initialize Git
        echo Try running this script as Administrator
        pause
        exit /b 1
    )
)

echo.
echo Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/santhiya0507/Shakespeare_club.git

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Updated BardSpeak with mobile support and AI scoring"

echo.
echo Pushing to GitHub...
echo You may be asked for GitHub credentials...
echo.
git branch -M main
git push -f origin main

if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo ERROR: Push failed!
    echo ========================================
    echo.
    echo Possible solutions:
    echo 1. Use GitHub Desktop instead (easier)
    echo 2. Generate Personal Access Token:
    echo    - Go to: https://github.com/settings/tokens
    echo    - Generate new token
    echo    - Use as password when prompted
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Code pushed to GitHub
echo ========================================
echo.
echo Your repository: https://github.com/santhiya0507/Shakespeare_club
echo.
echo Next steps:
echo 1. Go to https://dashboard.render.com
echo 2. Create PostgreSQL database
echo 3. Create Web Service
echo 4. Connect to your GitHub repo
echo 5. Get your Render link!
echo.
pause
