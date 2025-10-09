# ⚡ Quick Test Guide

## 🚀 Run the App

```powershell
python app.py
```

Open browser: **http://localhost:5000**

---

## ✅ Test Scenarios

### Scenario 1: Register as Admin
1. Click "Register"
2. Type username: **admin**
3. 👀 Watch the form change! (Department & Register Number disappear, Password appears)
4. Enter password: **admin123**
5. Click "Begin My Journey"
6. ✅ **Result:** Admin Dashboard opens

---

### Scenario 2: Register as Student
1. Click "Register"
2. Type username: **john** (or any name)
3. 👀 Form shows Register Number & Department fields
4. Enter register number: **12345**
5. Select department: **Computer Science Engineering**
6. Click "Begin My Journey"
7. ✅ **Result:** Student Dashboard opens

---

### Scenario 3: Login as Admin
1. Click "Login"
2. Click **"Admin Login"** tab
3. Username: **admin**
4. Password: **admin123**
5. Click "Admin Login"
6. ✅ **Result:** Admin Dashboard opens

---

### Scenario 4: Login as Student
1. Click "Login"
2. Stay on **"Student Login"** tab (default)
3. Register Number: **12345**
4. Click "Continue Learning"
5. ✅ **Result:** Student Dashboard opens

---

## 🎯 Key Features

✅ **Smart Registration Form**
- Detects "admin" username automatically
- Shows/hides fields dynamically
- No page reload needed

✅ **Unified Login Page**
- Two tabs: Student & Admin
- Same page, different forms
- Clear visual separation

✅ **Automatic Routing**
- Admin → Admin Dashboard
- Student → Student Dashboard
- No manual selection needed

---

## 📝 Summary of Changes

| Feature | Before | After |
|---------|--------|-------|
| Admin Login | Separate page `/admin/login` | Same page with tabs |
| Registration | Always asks for department | Hides department for admin |
| Admin Password | During registration | Shows field when username = "admin" |
| Routing | Manual navigation | Automatic based on user type |

---

**All set!** Just run `python app.py` and test it out! 🎉
