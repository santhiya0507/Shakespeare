# 🔐 Admin Registration & Login Guide

## ✅ What's New?

The system now has **intelligent registration and login** that automatically detects if you're an admin or student!

---

## 📝 Registration Page

### For Students:
1. Go to registration page
2. Enter **username** (any name except "admin")
3. Enter **register number**
4. Select **department**
5. Click "Begin My Journey"
6. → You'll be taken to **Student Dashboard**

### For Admin:
1. Go to registration page
2. Type **"admin"** as username
3. **Department and Register Number fields will automatically hide!**
4. **Password field will appear!**
5. Enter your admin password
6. Click "Begin My Journey"
7. → You'll be taken to **Admin Dashboard**

---

## 🔑 Login Page

The login page has **TWO tabs** on the same page:

### Student Login Tab (Default):
- Enter your register number only
- Click "Continue Learning"
- → Goes to Student Dashboard

### Admin Login Tab:
- Click on "Admin Login" tab
- Enter username: `admin`
- Enter password: `admin123` (or your custom password)
- Click "Admin Login"
- → Goes to Admin Dashboard

---

## 🎯 How It Works

### Registration Logic:
```
IF username = "admin":
    - Show password field
    - Hide register number field
    - Hide department field
    - Create admin account
    - Redirect to Admin Dashboard
ELSE:
    - Show register number field
    - Show department field
    - Hide password field
    - Create student account
    - Redirect to Student Dashboard
```

### Login Logic:
```
IF username AND password provided:
    - Check admins table
    - Redirect to Admin Dashboard
ELSE IF register_number provided:
    - Check users table
    - Redirect to Student Dashboard
```

---

## 🚀 Testing Instructions

### Test 1: Student Registration
```
1. Go to: http://localhost:5000/register
2. Username: "john_doe"
3. Register Number: "12345"
4. Department: "Computer Science Engineering"
5. Submit
6. ✅ Should go to Student Dashboard
```

### Test 2: Admin Registration
```
1. Go to: http://localhost:5000/register
2. Username: "admin" (type this)
3. Watch: Register Number and Department fields disappear!
4. Password field appears!
5. Password: "admin123"
6. Submit
7. ✅ Should go to Admin Dashboard
```

### Test 3: Student Login
```
1. Go to: http://localhost:5000/login
2. Stay on "Student Login" tab
3. Register Number: "12345"
4. Submit
5. ✅ Should go to Student Dashboard
```

### Test 4: Admin Login
```
1. Go to: http://localhost:5000/login
2. Click "Admin Login" tab
3. Username: "admin"
4. Password: "admin123"
5. Submit
6. ✅ Should go to Admin Dashboard
```

---

## 🛡️ Security Features

✅ **Password Hashing** - Admin passwords are hashed using Werkzeug
✅ **Separate Tables** - Admins and students are in different database tables
✅ **Session Management** - Different session keys for admin and students
✅ **Auto-Detection** - System automatically knows if you're admin or student

---

## 📊 Database Structure

### Students Table: `users`
- id
- username
- register_number
- department
- points
- streak
- etc.

### Admins Table: `admins`
- id
- username
- password_hash

---

## ⚠️ Important Notes

1. **Admin username MUST be "admin"** (case-insensitive)
2. **First admin registration** creates the admin account
3. **Subsequent admin logins** use the login page
4. **Students cannot access admin dashboard** (session-based protection)
5. **Admins cannot access student dashboard** (different session keys)

---

## 🎨 User Experience

### Registration Page Magic:
- Type "admin" → Form changes automatically!
- Type anything else → Normal student form
- No page reload needed
- Smooth transitions

### Login Page:
- Clean tabs interface
- Clear separation between student and admin
- No confusion about which form to use

---

## 🔧 Default Admin Credentials

**Username:** `admin`  
**Password:** `admin123`

(You can change this after first login or during registration)

---

**Ready to test!** Run `python app.py` and try both registration and login flows! 🎉
