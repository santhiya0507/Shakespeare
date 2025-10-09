# 🔐 Login Guide - BardSpeak

## ✅ Changes Made

The login system has been **unified into ONE page** at `/login`

### What's New?

- **Single Login Page** with two tabs:
  - 📚 **Student Login Tab** - Enter register number only
  - 🛡️ **Admin Login Tab** - Enter username and password

### How It Works

#### For Students:
1. Go to the login page
2. Stay on the **"Student Login"** tab (default)
3. Enter your register number
4. Click "Continue Learning"

#### For Admin:
1. Go to the login page
2. Click on the **"Admin Login"** tab
3. Enter:
   - **Username:** `admin`
   - **Password:** `admin123`
4. Click "Admin Login"
5. You'll be redirected to the admin dashboard

---

## 🚀 How to Test

### Step 1: Run the App
```powershell
python app.py
```

### Step 2: Open Browser
Go to: **http://localhost:5000**

### Step 3: Test Login
- Click "Login" button on homepage
- You'll see ONE page with TWO tabs:
  - Student Login (default)
  - Admin Login

### Step 4: Test Admin Login
- Switch to "Admin Login" tab
- Enter username: `admin`
- Enter password: `admin123`
- Click "Admin Login"
- You should see the admin dashboard!

---

## 📝 Technical Details

### Backend Changes (app.py)
- Modified `/login` route to handle both student and admin login
- Checks if `username` and `password` fields exist → Admin login
- Checks if `register_number` field exists → Student login
- Old `/admin/login` route now redirects to `/login`

### Frontend Changes (login.html)
- Added Bootstrap tabs for Student/Admin login
- Two separate forms in one page
- Student form: only register number field
- Admin form: username + password fields

---

## 🎯 Benefits

✅ **Single Entry Point** - One login page for everyone
✅ **Clear Separation** - Tabs make it obvious which login to use
✅ **No Confusion** - Students don't see admin fields by default
✅ **Easy Access** - Admin can easily switch to their tab

---

## 🔧 Default Credentials

### Admin:
- **Username:** `admin`
- **Password:** `admin123`

### Students:
- Use their **register number** (created during registration)

---

**Ready to use!** Just run `python app.py` and test it out! 🎉
