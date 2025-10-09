# 🚀 Deploy BardSpeak to Render - Get Your Link!

## Step-by-Step Guide to Get Your Render Link

---

## 📋 Prerequisites

1. ✅ GitHub account (create at https://github.com/signup)
2. ✅ Render account (create at https://render.com/signup)
3. ✅ Gemini API key (get at https://makersuite.google.com/app/apikey)

---

## 🔧 Step 1: Initialize Git and Push to GitHub

### 1.1 Initialize Git Repository

Open PowerShell in your project folder and run:

```powershell
cd "c:\Users\new pc\Documents\BardSpeak-main[1]\BardSpeak-main"

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - BardSpeak app ready for deployment"
```

### 1.2 Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `bardspeak` (or any name)
3. **Don't** check "Initialize with README"
4. Click "Create repository"

### 1.3 Push to GitHub

Copy the commands from GitHub (they look like this):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username!**

---

## 🗄️ Step 2: Create Database on Render

### 2.1 Go to Render Dashboard
- Open https://dashboard.render.com
- Login with your account

### 2.2 Create PostgreSQL Database
1. Click **"New +"** button (top right)
2. Select **"PostgreSQL"**
3. Fill in:
   - **Name:** `bardspeak-db`
   - **Database:** `bardspeak`
   - **User:** `bardspeak`
   - **Region:** Choose closest to you
   - **Plan:** Free
4. Click **"Create Database"**

### 2.3 Copy Database URL
1. Wait for database to be created (1-2 minutes)
2. Scroll down to **"Connections"** section
3. Find **"Internal Database URL"**
4. Click **"Copy"** button
5. **Save this URL** - you'll need it in Step 3!

Example URL:
```
postgresql://bardspeak:xxxxx@dpg-xxxxx.oregon-postgres.render.com/bardspeak
```

---

## 🌐 Step 3: Deploy Web Service

### 3.1 Create Web Service
1. Click **"New +"** button
2. Select **"Web Service"**
3. Click **"Connect a repository"**
4. **Connect your GitHub** account (if first time)
5. Select your **`bardspeak`** repository
6. Click **"Connect"**

### 3.2 Configure Service
Fill in these settings:

**Basic Settings:**
- **Name:** `bardspeak` (or your preferred name)
- **Region:** Same as database
- **Branch:** `main`
- **Root Directory:** (leave empty)
- **Runtime:** `Python 3`

**Build Settings:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Plan:**
- Select **"Free"**

### 3.3 Add Environment Variables

Scroll down to **"Environment Variables"** section and add these:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Paste the Internal Database URL from Step 2.3 |
| `SESSION_SECRET` | Any random string (e.g., `my-secret-key-12345`) |
| `GEMINI_API_KEY` | Your Gemini API key |

**To add each variable:**
1. Click **"Add Environment Variable"**
2. Enter **Key** and **Value**
3. Repeat for all 3 variables

### 3.4 Deploy!
1. Click **"Create Web Service"** button at bottom
2. Wait for deployment (5-10 minutes)
3. Watch the logs for progress

---

## 🎉 Step 4: Get Your Link!

### 4.1 Find Your URL
Once deployed, you'll see at the top:
```
https://bardspeak.onrender.com
```
Or whatever name you chose!

### 4.2 Test Your App
1. Click the URL
2. Your app opens in browser!
3. Test login/registration
4. Share the link with students!

---

## 📱 Step 5: Install as Mobile App

### On Android:
1. Open your Render URL in Chrome
2. Tap **"Install App"** button (appears automatically)
3. Or tap menu (⋮) → "Add to Home Screen"
4. App installs on home screen!

### On iPhone:
1. Open your Render URL in Safari
2. Tap **Share** button
3. Tap **"Add to Home Screen"**
4. App installs on home screen!

---

## 🔧 Troubleshooting

### Problem: "Build failed"
**Solution:**
- Check build logs in Render
- Verify `requirements.txt` has no errors
- Make sure all files are pushed to GitHub

### Problem: "Application failed to start"
**Solution:**
- Check start command: `gunicorn app:app`
- Verify environment variables are set
- Check logs for specific error

### Problem: "Database connection error"
**Solution:**
- Verify `DATABASE_URL` is correct
- Make sure database is created and running
- Check if URL starts with `postgresql://` (not `postgres://`)

### Problem: "Gemini API error"
**Solution:**
- Verify `GEMINI_API_KEY` is set correctly
- Get new key from https://makersuite.google.com/app/apikey
- Check API quota/limits

---

## 📊 Your Render URLs

After deployment, you'll have:

1. **App URL:** `https://bardspeak.onrender.com`
   - Share this with students!
   - Works on mobile and desktop
   - HTTPS enabled (required for microphone)

2. **Database URL:** `postgresql://...`
   - Internal use only
   - Already configured in environment variables

---

## 💰 Render Free Tier

### What You Get:
- ✅ **750 hours/month** free
- ✅ **Automatic HTTPS**
- ✅ **PostgreSQL database** (90 days free)
- ✅ **Auto-deploy** from GitHub
- ✅ **Custom domain** support

### Limitations:
- ⏰ App sleeps after 15 min inactivity
- ⏰ First load takes 30 seconds (wakes up)
- 💾 Database expires in 90 days (backup data!)

---

## 🔄 Updating Your App

### After making changes:

```powershell
# Commit changes
git add .
git commit -m "Updated features"

# Push to GitHub
git push

# Render auto-deploys! (2-5 minutes)
```

---

## 📝 Quick Commands Summary

```powershell
# Step 1: Git Setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
git branch -M main
git push -u origin main

# Step 2: Go to Render Dashboard
# Create PostgreSQL database
# Copy Internal Database URL

# Step 3: Create Web Service
# Connect GitHub repo
# Add environment variables:
#   - DATABASE_URL
#   - SESSION_SECRET
#   - GEMINI_API_KEY
# Deploy!

# Step 4: Get your link!
# https://bardspeak.onrender.com
```

---

## 🎯 Final Checklist

- [ ] Git initialized
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] PostgreSQL database created
- [ ] Database URL copied
- [ ] Web service created
- [ ] Environment variables added
- [ ] Deployment successful
- [ ] App URL received
- [ ] Tested on browser
- [ ] Tested on mobile
- [ ] Shared with students!

---

**Follow these steps and you'll have your Render link in 15 minutes!** 🚀

Your app will be live at: `https://bardspeak.onrender.com` (or your chosen name)
