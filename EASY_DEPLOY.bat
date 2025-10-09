@echo off
echo ========================================
echo BardSpeak - Easy GitHub Push
echo ========================================
echo.

REM Change to the script's directory
cd /d "%~dp0"

echo Current folder: %CD%
echo.

echo Step 1: Initializing Git...
if exist .git (
    echo Git already initialized
) else (
    git init
    if errorlevel 1 (
        echo.
        echo ERROR: Could not initialize Git
        echo Please run this script as Administrator:
        echo 1. Right-click this file
        echo 2. Select "Run as administrator"
        echo.
        pause
        exit /b 1
    )
)

echo.
echo Step 2: Configuring Git...
git config user.name "santhiya0507"
git config user.email "santhiyanagarajan2005@gmail.com"

echo.
echo Step 3: Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/santhiya0507/Shakespeare_club.git

echo.
echo Step 4: Adding all files...
git add .

echo.
echo Step 5: Committing changes...
git commit -m "Updated BardSpeak: Mobile-friendly, PWA, AI scoring, unified login"

echo.
echo Step 6: Pushing to GitHub...
echo.
echo ========================================
echo IMPORTANT: You will be asked for credentials
echo ========================================
echo Username: santhiya0507
echo Password: Use your Personal Access Token (NOT your GitHub password)
echo.
echo Don't have a token? Get one here:
echo https://github.com/settings/tokens
echo Click "Generate new token (classic)"
echo Check "repo" permission
echo Copy the token and use it as password
echo.
pause

git branch -M main
git push -f origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo Push failed! Try these solutions:
    echo ========================================
    echo.
    echo EASIEST SOLUTION: Use GitHub Desktop
    echo 1. Download: https://desktop.github.com
    echo 2. Install and login
    echo 3. File -^> Add local repository
    echo 4. Select this folder
    echo 5. Publish repository
    echo.
    echo OR: Use Personal Access Token
    echo 1. Go to: https://github.com/settings/tokens
    echo 2. Generate new token (classic)
    echo 3. Check "repo" permission
    echo 4. Copy token
    echo 5. Run this script again
    echo 6. Use token as password
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Code pushed to GitHub!
echo ========================================
echo.
echo Repository: https://github.com/santhiya0507/Shakespeare_club
echo.
echo Next: Deploy to Render
echo 1. Go to: https://dashboard.render.com
echo 2. New + -^> PostgreSQL (create database)
echo 3. New + -^> Web Service (deploy app)
echo 4. Connect your GitHub repo
echo 5. Add environment variables
echo 6. Get your link!
echo.
echo See DEPLOY_TO_RENDER.md for detailed steps
echo.
pause
