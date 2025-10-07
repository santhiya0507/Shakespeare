# Quick Start - Deploy to Render in 5 Minutes

## 🚀 Fast Track Deployment

### Step 1: Push to GitHub (2 min)
```bash
cd "c:\Users\new pc\Documents\BardSpeak-main[1]\BardSpeak-main"
git init
git add .
git commit -m "Deploy BardSpeak"
```
Create repo on GitHub, then:
```bash
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
git push -u origin main
```

### Step 2: Create Database on Render (1 min)
1. Go to https://dashboard.render.com
2. **New +** → **PostgreSQL**
3. Name: `bardspeak-db`, Click **Create**
4. **Copy the Internal Database URL**

### Step 3: Deploy App (2 min)
1. **New +** → **Web Service**
2. Connect your GitHub repo
3. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
4. Add Environment Variables:
   - `DATABASE_URL` = (paste URL from Step 2)
   - `SESSION_SECRET` = (any random string)
   - `GEMINI_API_KEY` = (your Gemini key)
5. Click **Create Web Service**

### Done! ✅
Your app will be live at: `https://your-app-name.onrender.com`

---

## 📝 What You Need

- ✅ GitHub account
- ✅ Render account (free)
- ✅ Gemini API key

## 🔑 Default Login
- Admin: `admin` / `admin123`

## ⚠️ Free Tier Notes
- App sleeps after 15 min (first load = 30 sec)
- Database expires in 90 days (backup data!)

## 📚 Full Guide
See `DEPLOYMENT_GUIDE.md` for detailed instructions.
