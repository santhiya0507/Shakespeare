@echo off
echo ========================================
echo Push to Your NEW GitHub Repository
echo ========================================
echo.

REM Change to script directory
cd /d "%~dp0"

echo Current folder: %CD%
echo.

echo ========================================
echo IMPORTANT: Enter your repository details
echo ========================================
echo.
set /p REPO_URL="Enter your GitHub repository URL (e.g., https://github.com/santhiya0507/bardspeak.git): "
echo.

echo Step 1: Initializing Git...
if exist .git (
    echo Removing old Git configuration...
    rmdir /s /q .git
)

git init
if errorlevel 1 (
    echo ERROR: Git init failed. Run as Administrator!
    pause
    exit /b 1
)

echo.
echo Step 2: Configuring Git...
git config user.name "santhiya0507"
git config user.email "santhiyanagarajan2005@gmail.com"

echo.
echo Step 3: Adding all files...
git add .

echo.
echo Step 4: Committing...
git commit -m "BardSpeak: Mobile-friendly PWA with AI scoring"

echo.
echo Step 5: Adding remote repository...
git remote add origin %REPO_URL%

echo.
echo Step 6: Pushing to GitHub...
echo.
echo ========================================
echo You will be asked for credentials:
echo ========================================
echo Username: santhiya0507
echo Password: Use Personal Access Token
echo.
echo Get token from: https://github.com/settings/tokens
echo Click "Generate new token (classic)"
echo Check "repo" permission
echo Copy the token (starts with ghp_)
echo Use it as password
echo.
pause

git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo Push failed!
    echo ========================================
    echo.
    echo Try GitHub Desktop instead:
    echo 1. Download: https://desktop.github.com
    echo 2. File -^> Add local repository
    echo 3. Select this folder
    echo 4. Publish repository
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Code is on GitHub!
echo ========================================
echo.
echo Your repository: %REPO_URL%
echo.
echo ========================================
echo NEXT: Deploy to Render
echo ========================================
echo.
echo 1. Go to: https://dashboard.render.com
echo 2. Sign up / Login
echo.
echo 3. Create PostgreSQL Database:
echo    - Click "New +" -^> "PostgreSQL"
echo    - Name: bardspeak-db
echo    - Click "Create Database"
echo    - COPY the "Internal Database URL"
echo.
echo 4. Create Web Service:
echo    - Click "New +" -^> "Web Service"
echo    - Connect your GitHub repository
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: gunicorn app:app
echo.
echo 5. Add Environment Variables:
echo    - DATABASE_URL = (paste database URL from step 3)
echo    - SESSION_SECRET = my-secret-key-12345
echo    - GEMINI_API_KEY = AIzaSyB32kRLOKH9QaJtv-Obg0TXIO1lRZD3UoE
echo.
echo 6. Click "Create Web Service"
echo.
echo 7. Wait 5-10 minutes
echo.
echo 8. YOUR LINK: https://bardspeak.onrender.com
echo    (or whatever name you chose)
echo.
echo ========================================
echo Share your link with students!
echo ========================================
echo.
pause
