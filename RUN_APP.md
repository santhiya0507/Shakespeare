# 🚀 How to Run BardSpeak App

## Option 1: Run Locally (Quick Start)

### Step 1: Install Dependencies
Open PowerShell in this directory and run:
```powershell
pip install -r requirements.txt
```

### Step 2: Set Environment Variables (Optional but Recommended)
Create a `.env` file in this directory with:
```
SESSION_SECRET=your-random-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
```

**Get Gemini API Key:** https://makersuite.google.com/app/apikey

### Step 3: Run the App
```powershell
python app.py
```

### Step 4: Access the App
Open your browser and go to:
```
http://localhost:5000
```

**Default Admin Login:**
- Username: `admin`
- Password: `admin123`

---

## Option 2: Get a Public Link (Deploy to Cloud)

### A. Deploy to Render (Free - Recommended)

1. **Create GitHub Repository**
   - Go to https://github.com/new
   - Create a new repository (e.g., "bardspeak")
   - Push this code:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
   git branch -M main
   git push -u origin main
   ```

2. **Create Render Account**
   - Go to https://render.com
   - Sign up (free)

3. **Create PostgreSQL Database**
   - Click "New +" → "PostgreSQL"
   - Name: `bardspeak-db`
   - Click "Create Database"
   - **Copy the Internal Database URL**

4. **Deploy Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name:** bardspeak
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
   - Add Environment Variables:
     - `DATABASE_URL` = (paste the database URL from step 3)
     - `SESSION_SECRET` = (any random string, e.g., "my-secret-key-12345")
     - `GEMINI_API_KEY` = (your Gemini API key)
   - Click "Create Web Service"

5. **Your App is Live!**
   - You'll get a URL like: `https://bardspeak.onrender.com`
   - Share this link with anyone!

**Note:** Free tier sleeps after 15 minutes of inactivity (takes 30 seconds to wake up)

---

### B. Deploy to Vercel (Alternative)

1. Install Vercel CLI:
   ```powershell
   npm install -g vercel
   ```

2. Deploy:
   ```powershell
   vercel
   ```

3. Follow the prompts and add environment variables when asked

---

### C. Use ngrok for Temporary Public Link

1. **Download ngrok:** https://ngrok.com/download

2. **Run your app locally:**
   ```powershell
   python app.py
   ```

3. **In another terminal, run ngrok:**
   ```powershell
   ngrok http 5000
   ```

4. **You'll get a public URL like:**
   ```
   https://abc123.ngrok.io
   ```
   Share this link! (Valid for 2 hours on free plan)

---

## Troubleshooting

### "Module not found" error
```powershell
pip install -r requirements.txt
```

### "Port already in use"
Change port in app.py or kill the process using port 5000

### "Database error"
The app uses SQLite by default locally (no setup needed)

### "Gemini API error"
- Get API key from: https://makersuite.google.com/app/apikey
- Set it in `.env` file or environment variables

---

## Quick Commands Reference

```powershell
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Run with specific port
python app.py --port 8000

# Check if running
curl http://localhost:5000
```

---

**Need help?** Check QUICK_START.md or DEPLOYMENT_GUIDE.md for more details!
