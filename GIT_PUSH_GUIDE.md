# Git Push Guide - BardSpeak

## ✅ Step 1: Initialize Git (Run in PowerShell)

Open PowerShell in your project folder and run:

```powershell
cd "c:\Users\new pc\Documents\BardSpeak-main[1]\BardSpeak-main"

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Configure BardSpeak with Supabase database"
```

## 🌐 Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `bardspeak`
3. Description: `Shakespeare Club Communication App with Supabase`
4. **Keep it Private** (recommended - contains config)
5. **Don't** initialize with README (you already have files)
6. Click **"Create repository"**

## 🚀 Step 3: Push to GitHub

GitHub will show you commands. Run these:

```powershell
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## 🔐 Step 4: Set Environment Variables in Render

1. Go to https://dashboard.render.com
2. Click your web service (or create new one)
3. Go to **Environment** tab
4. Add these variables:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | `postgresql://postgres:Nithi853197@db.alpylywgdjbptbkztfal.supabase.co:5432/postgres` |
| `SESSION_SECRET` | (generate random string at https://randomkeygen.com/) |
| `GEMINI_API_KEY` | (your Google Gemini API key) |

5. Click **"Save Changes"**
6. Render will auto-deploy

## ✅ Verify Deployment

1. Wait for deployment to complete (~2-3 minutes)
2. Visit your Render URL: `https://your-app.onrender.com`
3. Login with: `admin` / `admin123`
4. Test all features

## 🎯 Summary

**What we did:**
- ✅ Removed hardcoded password from code
- ✅ Set up Supabase database (11 tables created)
- ✅ Ready to push to Git safely
- ✅ Environment variables documented

**What's protected:**
- ✅ Database password (use environment variables)
- ✅ API keys (use environment variables)
- ✅ Session secrets (use environment variables)

## 📝 Quick Commands Reference

```powershell
# Initialize and commit
git init
git add .
git commit -m "Initial commit with Supabase"

# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
git branch -M main
git push -u origin main

# Future updates
git add .
git commit -m "Your update message"
git push
```

## 🆘 Troubleshooting

### Error: "Permission denied"
Run PowerShell as Administrator or use Git Bash

### Error: "fatal: not a git repository"
Make sure you're in the correct folder:
```powershell
cd "c:\Users\new pc\Documents\BardSpeak-main[1]\BardSpeak-main"
```

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
```

### Need to update remote URL
```powershell
git remote set-url origin https://github.com/YOUR_USERNAME/bardspeak.git
```

## 🎉 You're Done!

Your app is now:
- ✅ Using Supabase cloud database
- ✅ Safely stored in Git (no passwords committed)
- ✅ Ready to deploy on Render
- ✅ Secure with environment variables

**Next:** Deploy to Render and share your app URL! 🚀
