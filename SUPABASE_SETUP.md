# BardSpeak with Supabase Database

Complete guide to set up BardSpeak with Supabase PostgreSQL database.

## 🎯 Why Supabase?

- ✅ Free tier: 500MB database, unlimited API requests
- ✅ No expiration (unlike Render free PostgreSQL)
- ✅ Built-in dashboard for database management
- ✅ Automatic backups
- ✅ Fast and reliable
- ✅ Works with Render, Vercel, or any platform

## 📋 Step-by-Step Setup

### Step 1: Create Supabase Project

1. Go to https://supabase.com
2. Sign up / Log in
3. Click **"New Project"**
4. Fill in:
   - **Name**: `bardspeak`
   - **Database Password**: Choose a strong password (save it!)
   - **Region**: Choose closest to your users
   - **Pricing Plan**: Free
5. Click **"Create new project"**
6. Wait 2-3 minutes for setup

### Step 2: Get Database Connection String

1. In your Supabase project dashboard
2. Go to **Settings** (gear icon) → **Database**
3. Scroll to **Connection string** section
4. Select **URI** tab (not Session mode)
5. Copy the connection string:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxx.supabase.co:5432/postgres
   ```
6. Replace `[YOUR-PASSWORD]` with your actual database password

**Example:**
```
postgresql://postgres:MySecurePass123@db.abcdefghijk.supabase.co:5432/postgres
```

### Step 3: Initialize Database

**Option A: Using setup_supabase.py (Recommended)**

```bash
# Set environment variable
set DATABASE_URL=postgresql://postgres:YOUR-PASSWORD@db.xxx.supabase.co:5432/postgres

# Run setup script
python setup_supabase.py
```

**Option B: Using Supabase SQL Editor**

1. In Supabase dashboard, go to **SQL Editor**
2. Click **"New query"**
3. Copy all CREATE TABLE statements from `setup_supabase.py`
4. Click **"Run"**

**Option C: Let app.py initialize automatically**

The app will call `init_db()` on first run, which creates all tables.

### Step 4: Configure Local Development

Create `.env` file (don't commit this!):

```bash
# .env
DATABASE_URL=postgresql://postgres:YOUR-PASSWORD@db.xxx.supabase.co:5432/postgres
SESSION_SECRET=your-random-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
```

Install python-dotenv if not already:
```bash
pip install python-dotenv
```

Add to top of `app.py` (if not already there):
```python
from dotenv import load_dotenv
load_dotenv()  # Load .env file
```

### Step 5: Test Locally

```bash
# Run the app
python app.py

# Visit http://localhost:5000
# Try logging in with: admin / admin123
```

### Step 6: Deploy to Render

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Configure Supabase database"
   git push
   ```

2. **In Render Dashboard:**
   - Go to your web service
   - Click **Environment** tab
   - Add/Update environment variables:
     - `DATABASE_URL` = (your Supabase connection string)
     - `SESSION_SECRET` = (random string)
     - `GEMINI_API_KEY` = (your API key)
   - Click **"Save Changes"**
   - Render will auto-redeploy

3. **Verify deployment:**
   - Visit your Render URL
   - Login with admin credentials
   - Test all features

## 🔍 Verify Database Setup

### Check Tables in Supabase

1. Go to Supabase dashboard
2. Click **Table Editor**
3. You should see all tables:
   - users
   - admins
   - biographies
   - daily_quotes
   - listening_content
   - observation_content
   - writing_topics
   - tasks
   - user_completions
   - user_streaks
   - speaking_attempts

### Check Sample Data

1. Click on **admins** table
2. You should see one row: `admin` user
3. Click on **biographies** table
4. You should see 2 sample biographies

## 🎨 Supabase Dashboard Features

### SQL Editor
Run custom queries:
```sql
-- Check all users
SELECT * FROM users;

-- Check total points leaderboard
SELECT username, department, total_points 
FROM users 
ORDER BY total_points DESC 
LIMIT 10;

-- Check admin
SELECT * FROM admins;
```

### Table Editor
- View/edit data visually
- Add/delete rows
- Filter and search

### Database Backups
- Go to **Settings** → **Database**
- Scroll to **Backups**
- Free tier: Daily backups (7-day retention)
- Paid tier: Point-in-time recovery

### API
Supabase provides REST API for your database (optional, not needed for this app)

## 🔐 Security Best Practices

### 1. Change Admin Password
After first login:
```sql
-- In Supabase SQL Editor
UPDATE admins 
SET password_hash = 'new-hashed-password' 
WHERE username = 'admin';
```

Or login as admin and change via app interface.

### 2. Secure Connection String
- Never commit DATABASE_URL to Git
- Use environment variables
- Rotate password periodically

### 3. Enable Row Level Security (Optional)
For extra security, enable RLS in Supabase:
1. Go to **Authentication** → **Policies**
2. Enable RLS for sensitive tables
3. Create policies for access control

## 📊 Monitoring

### Check Database Usage
1. Supabase dashboard → **Settings** → **Usage**
2. Monitor:
   - Database size (500MB free tier limit)
   - API requests
   - Bandwidth

### Check Logs
1. Supabase dashboard → **Logs**
2. View database queries and errors

## 🆘 Troubleshooting

### Error: "Connection refused"
**Cause:** Wrong connection string or network issue
**Solution:**
1. Verify DATABASE_URL is correct
2. Check Supabase project is active
3. Try connection pooler URL (see below)

### Error: "Password authentication failed"
**Cause:** Wrong password in connection string
**Solution:**
1. Reset database password in Supabase Settings
2. Update DATABASE_URL with new password

### Error: "Too many connections"
**Cause:** Connection pool exhausted
**Solution:** Use Supabase connection pooler:
```
postgresql://postgres:[PASSWORD]@db.xxx.supabase.co:6543/postgres?pgbouncer=true
```
Note: Port 6543 (not 5432) and add `?pgbouncer=true`

### Error: "SSL required"
**Cause:** Supabase requires SSL
**Solution:** App already handles this, but if needed:
```python
DATABASE_URL += "?sslmode=require"
```

### Slow Queries
**Solution:**
1. Add indexes in Supabase SQL Editor:
   ```sql
   CREATE INDEX idx_users_register ON users(register_number);
   CREATE INDEX idx_completions_user ON user_completions(user_id);
   ```

## 💰 Supabase Pricing

### Free Tier (Current)
- ✅ 500MB database
- ✅ Unlimited API requests
- ✅ 2GB bandwidth
- ✅ 50MB file storage
- ✅ Daily backups (7 days)
- ✅ Community support

### Pro Tier ($25/month)
- 8GB database
- 250GB bandwidth
- 100GB file storage
- Point-in-time recovery
- Email support

**For BardSpeak:** Free tier is sufficient for 100-500 users

## 🔄 Migration from SQLite

If you have existing SQLite data:

### Option 1: Export/Import
```bash
# Export from SQLite
sqlite3 shakespeare_club_gamified.db .dump > backup.sql

# Manually convert and import to Supabase
# (requires SQL syntax adjustments)
```

### Option 2: Use pgloader
```bash
pgloader sqlite://shakespeare_club_gamified.db postgresql://postgres:pass@db.xxx.supabase.co:5432/postgres
```

### Option 3: Start Fresh
Just run `setup_supabase.py` to create new database with sample data.

## 📚 Useful Supabase SQL Queries

### Reset Database (DANGER!)
```sql
-- Drop all tables (careful!)
DROP TABLE IF EXISTS speaking_attempts CASCADE;
DROP TABLE IF EXISTS user_streaks CASCADE;
DROP TABLE IF EXISTS user_completions CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS writing_topics CASCADE;
DROP TABLE IF EXISTS observation_content CASCADE;
DROP TABLE IF EXISTS listening_content CASCADE;
DROP TABLE IF EXISTS daily_quotes CASCADE;
DROP TABLE IF EXISTS biographies CASCADE;
DROP TABLE IF EXISTS admins CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Then run setup_supabase.py again
```

### Check Database Size
```sql
SELECT 
    pg_size_pretty(pg_database_size('postgres')) as database_size;
```

### List All Tables
```sql
SELECT tablename 
FROM pg_tables 
WHERE schemaname = 'public';
```

### Count Records
```sql
SELECT 
    'users' as table_name, COUNT(*) as count FROM users
UNION ALL
SELECT 'admins', COUNT(*) FROM admins
UNION ALL
SELECT 'biographies', COUNT(*) FROM biographies
UNION ALL
SELECT 'user_completions', COUNT(*) FROM user_completions;
```

## ✅ Checklist

Before deploying:

- [ ] Supabase project created
- [ ] Database connection string obtained
- [ ] `setup_supabase.py` run successfully
- [ ] Tables visible in Supabase Table Editor
- [ ] Admin user exists (username: admin)
- [ ] Sample data inserted
- [ ] Local testing successful
- [ ] Environment variables set in Render
- [ ] Deployed and tested on Render

## 🎉 You're Done!

Your BardSpeak app is now using Supabase PostgreSQL database!

**Benefits:**
- ✅ Data persists across deployments
- ✅ No 90-day expiration
- ✅ Easy database management
- ✅ Automatic backups
- ✅ Scalable and reliable

**Next Steps:**
1. Change admin password
2. Add more content (biographies, topics, etc.)
3. Invite students to register
4. Monitor usage in Supabase dashboard

---

**Need Help?**
- Supabase Docs: https://supabase.com/docs
- Supabase Discord: https://discord.supabase.com
- BardSpeak Issues: Check DEBUG_INTERNAL_ERROR.md
