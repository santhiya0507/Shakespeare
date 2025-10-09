# Shakespeare Club Logo Setup Instructions

## ✅ What Has Been Done

All HTML templates have been updated to display the Shakespeare Club logo at the top of each page:

### Updated Pages:
1. **home.html** - Main landing page (200px logo)
2. **dashboard.html** - Student dashboard (100px logo in header)
3. **register.html** - Registration page (150px logo)
4. **login.html** - Login page (150px logo)
5. **admin_login.html** - Admin login page (150px logo)
6. **admin_dashboard.html** - Admin dashboard (80px logo in header)

## 📋 Next Steps - Save Your Logo

### Option 1: Using the Setup Script (Recommended)
1. Double-click `setup_logo.bat` in the project root
2. This will create the `static/images` directory
3. Save your logo image as: `static/images/shakespeare_logo.png`

### Option 2: Manual Setup
1. Create a new folder: `static/images/`
2. Save your Shakespeare Club logo image as: `static/images/shakespeare_logo.png`

## 📁 Required File Path
```
BardSpeak-main/
├── static/
│   ├── images/
│   │   └── shakespeare_logo.png  ← Save your logo here
│   ├── css/
│   ├── js/
│   └── audio/
```

## 🎨 Logo Specifications

- **File Name:** `shakespeare_logo.png`
- **Format:** PNG (recommended for transparency)
- **Recommended Size:** 500x500 pixels or larger (will be auto-scaled)
- **Background:** Transparent background works best

## ✨ Logo Display Sizes

The logo will automatically scale to different sizes on different pages:
- **Home Page:** 200px max width
- **Dashboard:** 100px max width  
- **Registration/Login:** 150px max width
- **Admin Pages:** 80-150px max width

## 🚀 Testing

After saving the logo:
1. Start your Flask application
2. Visit the home page at `http://localhost:5000`
3. The logo should appear at the top of the page
4. Navigate to other pages to verify the logo displays correctly

## 🔧 Troubleshooting

**Logo not showing?**
- Verify the file is named exactly: `shakespeare_logo.png`
- Check the file is in: `static/images/` folder
- Clear your browser cache (Ctrl+F5)
- Restart the Flask application

**Logo too large/small?**
- The CSS automatically scales the logo
- You can adjust sizes in the HTML templates if needed

## 📝 Notes

- All templates use Flask's `url_for()` function for proper path resolution
- The logo will work in both development and production environments
- If you want to use a different image format (JPG, SVG), update the file extension in all templates
