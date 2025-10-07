# BardSpeak - Shakespeare Club Communication App

A gamified English communication learning platform with AI-powered feedback, designed for students to practice speaking, listening, writing, and observation skills.

## 🌟 Features

### For Students
- **Speaking Module**: Practice reading biographies with speech recognition and AI feedback
- **Listening Module**: Interactive audio lessons with robot characters
- **Writing Module**: Daily quotes and essay topics with sentiment analysis
- **Observation Module**: Video-based learning with comprehension questions
- **Gamification**: Points, streaks, badges, and leaderboards
- **Certificates**: Earn certificates upon completing all modules

### For Admins
- **Content Management**: Add/edit biographies, topics, videos, and audio
- **Task Assignment**: Create department-specific tasks with deadlines
- **Student Monitoring**: Track progress, points, and completions
- **Analytics Dashboard**: View student performance and engagement

### AI Features (Powered by Google Gemini)
- Sentiment analysis of student responses
- Communication practice feedback
- Writing quality assessment

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit http://localhost:5000
```

**Default Admin Login:**
- Username: `admin`
- Password: `admin123`

### Cloud Deployment (Render)
See **[QUICK_START.md](QUICK_START.md)** for 5-minute deployment guide.

See **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** for detailed instructions.

## 📋 Requirements

- Python 3.11+
- Flask 3.0+
- SQLite (local) or PostgreSQL (cloud)
- Google Gemini API key
- FFmpeg (optional, for audio conversion)

## 🗄️ Database

**Automatic Detection:**
- **Local**: Uses SQLite (`shakespeare_club_gamified.db`)
- **Cloud**: Uses PostgreSQL (via `DATABASE_URL` environment variable)

**Tables:**
- `users` - Student accounts and stats
- `admins` - Admin accounts
- `biographies` - Speaking practice content
- `daily_quotes` - Student-submitted quotes
- `listening_content` - Audio lessons
- `observation_content` - Video lessons
- `writing_topics` - Essay prompts
- `tasks` - Admin-assigned tasks
- `user_completions` - Activity tracking
- `user_streaks` - Daily engagement
- `speaking_attempts` - Rate limiting

## 🎮 How It Works

### Student Flow
1. **Register** with username, register number, and department
2. **Login** to access dashboard
3. **Complete modules** to earn points:
   - Speaking: 10-15 points
   - Listening: 10 points
   - Writing: 10-15 points
   - Observation: 10 points
4. **Build streaks** by practicing daily
5. **Earn badges** for milestones:
   - Century Scorer (100+ points)
   - Week Warrior (7-day streak)
   - Monthly Master (30-day streak)
   - Practice Champion (10+ completions)
   - Communication Expert (50+ completions)
6. **Download certificate** after completing all modules

### Admin Flow
1. **Login** with admin credentials
2. **Manage content** (add/edit/delete)
3. **Assign tasks** to departments
4. **Monitor progress** via dashboard
5. **View analytics** and leaderboards

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite / PostgreSQL
- **AI**: Google Gemini API
- **Speech**: SpeechRecognition, gTTS
- **Audio**: pydub, FFmpeg
- **PDF**: ReportLab
- **Server**: Gunicorn (production)
- **Hosting**: Render (recommended)

## 📁 Project Structure

```
BardSpeak-main/
├── app.py                  # Main Flask application
├── gemini.py              # AI integration (Gemini API)
├── db_adapter.py          # Database abstraction layer
├── requirements.txt       # Python dependencies
├── Procfile              # Render start command
├── render.yaml           # Render deployment config
├── .gitignore            # Git exclusions
├── templates/            # HTML templates
│   ├── home.html
│   ├── dashboard.html
│   ├── speaking.html
│   ├── writing.html
│   └── ...
├── static/               # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── audio/
└── docs/
    ├── README.md
    ├── QUICK_START.md
    ├── DEPLOYMENT_GUIDE.md
    └── CHANGES.md
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Cloud only | PostgreSQL connection string |
| `SESSION_SECRET` | Yes | Flask session secret key |
| `GEMINI_API_KEY` | Yes | Google Gemini API key |
| `FFMPEG_BIN` | No | Path to ffmpeg executable |
| `FFPROBE_BIN` | No | Path to ffprobe executable |

### Local Setup (.env file)
```bash
SESSION_SECRET=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key
```

### Render Setup
Add environment variables in Render dashboard under "Environment".

## 🎯 Key Features Explained

### Speaking Practice
- Students read biographies aloud
- Speech-to-text transcription
- AI analyzes pronunciation and fluency
- Similarity score vs. original text
- 3 attempts per biography per day

### Daily Quotes
- Students submit inspirational quotes
- First submission per department gets bonus points
- Quotes displayed on dashboard
- Encourages daily engagement

### Streaks & Gamification
- Daily activity tracking
- Consecutive day streaks
- Best streak recorded
- Motivates consistent practice

### Certificates
- Requires completion in all 4 modules
- PDF generation with student details
- Downloadable from dashboard
- Professional design

## 🔒 Security

- Password hashing with Werkzeug
- Session-based authentication
- CSRF protection (Flask built-in)
- Environment variable secrets
- SQL injection prevention (parameterized queries)

## 🐛 Troubleshooting

### "Unable to open database file"
✅ **Fixed!** App now uses absolute path for SQLite.

### "Couldn't find ffmpeg or avconv"
- Install FFmpeg: https://www.gyan.dev/ffmpeg/builds/
- Or set `FFMPEG_BIN` environment variable
- Or ensure client uploads WAV format

### "psycopg2 not found"
```bash
pip install psycopg2-binary
```

### "Gemini API error"
- Check `GEMINI_API_KEY` is set correctly
- Verify API key is active
- Check API quota/limits

## 📊 Database Schema

See `app.py` `init_db()` function for complete schema.

**Key relationships:**
- Users → Completions (one-to-many)
- Users → Streaks (one-to-many)
- Admins → Content (one-to-many)
- Tasks → Departments (filtered)

## 🚢 Deployment Options

### Option 1: Render (Recommended)
- Free tier available
- Auto-scaling
- PostgreSQL included
- See DEPLOYMENT_GUIDE.md

### Option 2: Heroku
- Similar to Render
- PostgreSQL add-on
- Requires Procfile

### Option 3: PythonAnywhere
- Free tier available
- SQLite supported
- Manual setup required

### Option 4: Self-hosted
- VPS (DigitalOcean, Linode, etc.)
- Nginx + Gunicorn
- PostgreSQL or SQLite
- Full control

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Google Gemini for AI capabilities
- Flask community for excellent framework
- Render for easy deployment
- Students and educators for feedback

## 📧 Support

For issues and questions:
1. Check DEPLOYMENT_GUIDE.md
2. Review CHANGES.md
3. Check Render logs
4. Open GitHub issue

---

**Built with ❤️ for English communication learners**

## 🎓 Educational Use

This app is designed for:
- English language learners
- Communication skills development
- Classroom engagement
- Self-paced learning
- Progress tracking

Perfect for:
- Schools and colleges
- Language institutes
- Corporate training
- Self-study programs

---

## Version History

### v2.0 (Current) - Cloud Ready
- ✅ PostgreSQL support
- ✅ Render deployment ready
- ✅ Fixed database path issues
- ✅ Production server (Gunicorn)
- ✅ Environment variable configuration

### v1.0 - Initial Release
- Basic Flask app
- SQLite database
- Core modules (speaking, listening, writing, observation)
- Gamification features
- Admin panel

---

**Ready to deploy? Start with [QUICK_START.md](QUICK_START.md)!** 🚀
