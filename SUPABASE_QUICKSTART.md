# Supabase Quick Start - 3 Minutes

## 🚀 Super Fast Setup

### 1. Get Supabase Connection String (1 min)
1. Go to https://supabase.com → Create project
2. Settings → Database → Connection string (URI mode)
3. Copy: `postgresql://postgres:[PASSWORD]@db.xxx.supabase.co:5432/postgres`

### 2. Initialize Database (1 min)
```bash
# Set environment variable (replace with your actual URL)
set DATABASE_URL=postgresql://postgres:YOUR-PASSWORD@db.xxx.supabase.co:5432/postgres

# Run setup script
python setup_supabase.py
```

### 3. Test Locally (1 min)
```bash
# Run app
python app.py

# Visit http://localhost:5000
# Login: admin / admin123
```

## ✅ Done!

Your database is now in Supabase cloud!

---

## 🌐 Deploy to Render

```bash
# Commit changes
git add .
git commit -m "Use Supabase database"
git push

# In Render Dashboard → Environment:
DATABASE_URL = (your Supabase URL)
SESSION_SECRET = (random string)
GEMINI_API_KEY = (your key)

# Save → Auto-deploys
```

---

## 📋 What You Need

- ✅ Supabase account (free)
- ✅ Your Supabase connection string
- ✅ 3 minutes

## 🎯 Key Files

- `setup_supabase.py` - Run this to create tables
- `SUPABASE_SETUP.md` - Full documentation
- `.env.example` - Environment variables template

## 🆘 Quick Troubleshooting

**Can't connect?**
- Check password in connection string
- Verify Supabase project is active

**Tables not created?**
- Run `python setup_supabase.py` again
- Or use Supabase SQL Editor

**App error?**
- Check Render logs
- Verify DATABASE_URL is set
- See DEBUG_INTERNAL_ERROR.md

---

**Full guide:** See SUPABASE_SETUP.md
