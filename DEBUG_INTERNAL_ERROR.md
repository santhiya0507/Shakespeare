# Debugging Internal Server Error on Render

## Common Causes & Solutions

### 1. Check Render Logs (Most Important!)

**Go to Render Dashboard:**
1. Click on your web service
2. Click "Logs" tab
3. Look for the actual error message

**Common errors you'll see:**
- Database connection failed
- Missing environment variable
- Import error
- SQL syntax error

### 2. Database Connection Issues

**Problem:** `DATABASE_URL` not set or incorrect
**Solution:**
```bash
# In Render Dashboard → Environment
# Verify these are set:
DATABASE_URL=postgresql://...  (from your PostgreSQL service)
SESSION_SECRET=your-secret-key
GEMINI_API_KEY=your-api-key
```

### 3. PostgreSQL Query Compatibility

**Problem:** Using `?` placeholders with PostgreSQL
**Solution:** Already fixed in app.py, but verify queries use:
- SQLite: `?` placeholders
- PostgreSQL: `%s` placeholders

### 4. Database Not Initialized

**Problem:** Tables don't exist yet
**Solution:** The app calls `init_db()` on startup, but check if it succeeded

### 5. Missing gemini.py File

**Problem:** `from gemini import ...` fails
**Solution:** Ensure `gemini.py` is in your repository

## Quick Diagnostic Steps

### Step 1: Check Render Logs
```
Render Dashboard → Your Service → Logs
```

Look for lines like:
```
Error: ...
Traceback: ...
ModuleNotFoundError: ...
psycopg2.OperationalError: ...
```

### Step 2: Verify Environment Variables
```
Render Dashboard → Your Service → Environment
```

Required:
- ✅ `DATABASE_URL`
- ✅ `SESSION_SECRET`
- ✅ `GEMINI_API_KEY`

### Step 3: Test Database Connection

Add this to check if DB is accessible:
```python
# At the end of app.py, before if __name__ == '__main__':
print(f"USE_POSTGRES: {USE_POSTGRES}")
print(f"DATABASE_URL exists: {bool(DATABASE_URL)}")
```

### Step 4: Check Build Logs
```
Render Dashboard → Your Service → Events → View Build
```

Ensure all packages installed successfully.

## Specific Error Solutions

### Error: "relation does not exist"
**Cause:** Database tables not created
**Solution:**
1. Check if `init_db()` ran successfully
2. Manually run initialization (see below)

### Error: "syntax error at or near"
**Cause:** SQL syntax incompatibility
**Solution:** Check query placeholders (`?` vs `%s`)

### Error: "could not connect to server"
**Cause:** Database URL incorrect or database not running
**Solution:**
1. Verify `DATABASE_URL` in environment variables
2. Check PostgreSQL service is running
3. Use Internal Database URL (not External)

### Error: "No module named 'gemini'"
**Cause:** `gemini.py` not in repository
**Solution:**
```bash
git add gemini.py
git commit -m "Add gemini.py"
git push
```

### Error: "No module named 'psycopg2'"
**Cause:** Missing in requirements.txt
**Solution:** Already in requirements.txt, rebuild

## Manual Database Initialization

If `init_db()` didn't run automatically:

**Option 1: Render Shell**
1. Render Dashboard → Your Service → Shell
2. Run:
   ```bash
   python
   >>> from app import init_db
   >>> init_db()
   >>> exit()
   ```

**Option 2: Local Script**
```python
# init_remote.py
import os
import psycopg2

DATABASE_URL = "your-render-database-url"
# Copy all CREATE TABLE statements from app.py init_db()
# Run them manually
```

## Enable Debug Mode Temporarily

**⚠️ Only for debugging, remove after fixing!**

In Render Environment, add:
```
FLASK_DEBUG=1
```

This will show detailed error pages.

**Remember to remove after debugging!**

## Common PostgreSQL vs SQLite Issues

### Issue 1: AUTOINCREMENT
```python
# SQLite
id INTEGER PRIMARY KEY AUTOINCREMENT

# PostgreSQL
id SERIAL PRIMARY KEY
```
**Status:** ✅ Already fixed in app.py

### Issue 2: Placeholders
```python
# SQLite
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# PostgreSQL
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```
**Status:** ✅ Already fixed in app.py

### Issue 3: Boolean Values
```python
# SQLite: 0/1
# PostgreSQL: TRUE/FALSE
```
**Status:** ✅ Compatible

### Issue 4: PRAGMA (SQLite only)
```python
# This won't work on PostgreSQL:
cursor.execute('PRAGMA table_info(tasks)')
```
**Status:** ✅ Already fixed with conditional check

## Check These Files Exist

```bash
# Verify in your repository:
✅ app.py
✅ gemini.py
✅ requirements.txt
✅ runtime.txt
✅ Procfile
✅ templates/ (folder with HTML files)
✅ static/ (folder with CSS/JS)
```

## Test Locally with PostgreSQL

To replicate the Render environment:

```bash
# Install PostgreSQL locally
# Create database
createdb shakespeare_club

# Set environment variable
set DATABASE_URL=postgresql://localhost/shakespeare_club

# Run app
python app.py
```

## Render-Specific Issues

### Issue: Static files not loading
**Solution:** Render serves static files automatically, but check paths

### Issue: App keeps restarting
**Solution:** Check logs for crash reason

### Issue: Slow first load
**Solution:** Normal on free tier (cold start)

## Get Detailed Error Info

Add this at the top of app.py (temporarily):

```python
import traceback
import sys

@app.errorhandler(500)
def internal_error(error):
    print("="*50, file=sys.stderr)
    print("INTERNAL SERVER ERROR:", file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
    print("="*50, file=sys.stderr)
    return "Internal Server Error - Check Logs", 500
```

This will print full error details to Render logs.

## Most Likely Causes (Ranked)

1. **🔴 DATABASE_URL not set** (90% of cases)
   - Solution: Add in Render Environment

2. **🟡 Database tables not created** (5% of cases)
   - Solution: Run init_db() manually

3. **🟡 gemini.py missing** (3% of cases)
   - Solution: git add gemini.py

4. **🟢 Other import errors** (2% of cases)
   - Solution: Check requirements.txt

## Next Steps

1. **Check Render Logs** - This will tell you the exact error
2. **Verify Environment Variables** - Especially DATABASE_URL
3. **Share the error message** - So I can provide specific fix

## Quick Checklist

Before asking for help, verify:

- [ ] Checked Render logs for actual error
- [ ] DATABASE_URL is set in environment
- [ ] SESSION_SECRET is set
- [ ] GEMINI_API_KEY is set
- [ ] Build completed successfully
- [ ] All files committed to Git
- [ ] Python 3.11.9 is being used (check build logs)

---

**Most Important:** Check the Render logs! They contain the exact error message that will tell us what's wrong.

Share the error from the logs and I can provide a specific fix.
