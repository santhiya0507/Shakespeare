# BardSpeak Deployment Guide for Render

This guide will help you deploy your BardSpeak application to Render with a cloud PostgreSQL database.

## What Changed

Your app now supports **both SQLite (local) and PostgreSQL (cloud)**:
- **Local development**: Uses SQLite database file
- **Render deployment**: Automatically uses PostgreSQL from environment variable `DATABASE_URL`

## Prerequisites

1. GitHub account
2. Render account (free tier available at https://render.com)
3. Your Gemini API key

## Step-by-Step Deployment

### 1. Push Code to GitHub

```bash
cd "c:\Users\new pc\Documents\BardSpeak-main[1]\BardSpeak-main"
git init
git add .
git commit -m "Initial commit - BardSpeak app with cloud database support"
```

Create a new repository on GitHub, then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/bardspeak.git
git branch -M main
git push -u origin main
```

### 2. Create PostgreSQL Database on Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `bardspeak-db`
   - **Database**: `shakespeare_club`
   - **User**: `bardspeak`
   - **Region**: Choose closest to your users
   - **Plan**: Free (or paid for better performance)
4. Click **"Create Database"**
5. Wait for database to be created (takes ~1 minute)
6. **Copy the Internal Database URL** (starts with `postgres://`)

### 3. Deploy Web Service on Render

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `bardspeak`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid for better performance)

### 4. Add Environment Variables

In the Render web service settings, add these environment variables:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Paste the Internal Database URL from step 2 |
| `SESSION_SECRET` | Generate a random string (e.g., use https://randomkeygen.com/) |
| `GEMINI_API_KEY` | Your Google Gemini API key |

**Important**: If the `DATABASE_URL` starts with `postgres://`, Render will automatically convert it to `postgresql://` (the app handles this).

### 5. Deploy

1. Click **"Create Web Service"**
2. Render will automatically:
   - Install dependencies from `requirements.txt`
   - Start your app with gunicorn
   - Initialize the PostgreSQL database on first run

### 6. Initialize Database

After first deployment:
1. Your app will automatically run `init_db()` on startup
2. This creates all tables and inserts sample data
3. Default admin credentials:
   - Username: `admin`
   - Password: `admin123`

## Verify Deployment

1. Visit your Render URL: `https://bardspeak.onrender.com`
2. Test registration and login
3. Check that data persists after app restarts

## Important Notes

### Free Tier Limitations

**Render Free Tier**:
- Web service spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month (enough for one service)

**PostgreSQL Free Tier**:
- 1GB storage
- Expires after 90 days (backup your data!)
- Shared CPU/RAM

### Upgrading to Paid

For production use, consider:
- **Web Service**: $7/month (no spin-down, better performance)
- **PostgreSQL**: $7/month (no expiration, backups, more storage)

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | PostgreSQL connection string (auto-provided by Render) |
| `SESSION_SECRET` | Yes | Secret key for Flask sessions |
| `GEMINI_API_KEY` | Yes | Google Gemini API for AI features |
| `FFMPEG_BIN` | No | Path to ffmpeg (if using audio conversion) |
| `FFPROBE_BIN` | No | Path to ffprobe (if using audio conversion) |

## Troubleshooting

### Database Connection Errors

If you see `psycopg2` errors:
1. Check that `DATABASE_URL` is set correctly
2. Verify the database is running in Render dashboard
3. Check logs: Render Dashboard → Your Service → Logs

### App Won't Start

1. Check build logs for dependency errors
2. Verify `requirements.txt` has all packages
3. Ensure `Procfile` exists with: `web: gunicorn app:app`

### Data Not Persisting

1. Verify you're using PostgreSQL (check logs for "USE_POSTGRES: True")
2. Don't use SQLite on Render (filesystem is ephemeral)
3. Check database connection in Render dashboard

## Local Development

Your app still works locally with SQLite:

```bash
# No DATABASE_URL set = uses SQLite
python app.py
```

To test with PostgreSQL locally:

```bash
# Set DATABASE_URL to your local PostgreSQL
set DATABASE_URL=postgresql://user:pass@localhost/dbname
python app.py
```

## Backup and Migration

### Export Data from SQLite to PostgreSQL

If you have existing SQLite data:

```bash
# Install pgloader
# Then run:
pgloader sqlite://shakespeare_club_gamified.db postgresql://user:pass@host/dbname
```

### Backup PostgreSQL Data

From Render dashboard:
1. Go to your database
2. Click "Backups" tab
3. Create manual backup or schedule automatic backups (paid plans)

## Support

- **Render Docs**: https://render.com/docs
- **PostgreSQL Docs**: https://www.postgresql.org/docs/
- **Flask Docs**: https://flask.palletsprojects.com/

## Security Checklist

- [ ] Change default admin password after first login
- [ ] Use strong `SESSION_SECRET`
- [ ] Keep `GEMINI_API_KEY` secret
- [ ] Enable HTTPS (Render provides this automatically)
- [ ] Regular database backups
- [ ] Monitor logs for suspicious activity

## Next Steps

1. Configure custom domain (optional)
2. Set up monitoring and alerts
3. Configure automated backups
4. Add more admin users
5. Customize the app for your needs

---

**Your app is now running in the cloud with persistent PostgreSQL storage!** 🎉
