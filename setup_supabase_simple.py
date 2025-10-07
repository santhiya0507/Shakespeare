"""
Initialize Supabase Database for BardSpeak - Simple Version
This version checks dependencies first
"""
import sys
import os

# Check if psycopg2 is installed
try:
    import psycopg2
except ImportError:
    print("❌ Error: psycopg2 is not installed")
    print("\nPlease install it first:")
    print("  pip install psycopg2-binary")
    print("\nOr run:")
    print("  python -m pip install psycopg2-binary werkzeug")
    sys.exit(1)

# Check if werkzeug is installed
try:
    from werkzeug.security import generate_password_hash
except ImportError:
    print("❌ Error: werkzeug is not installed")
    print("\nPlease install it first:")
    print("  pip install werkzeug")
    sys.exit(1)

print("✅ All dependencies found!")
print()

# Get Supabase connection string
DATABASE_URL = os.environ.get('DATABASE_URL')

if not DATABASE_URL:
    print("DATABASE_URL not found in environment variables.")
    print()
    DATABASE_URL = input("Enter your Supabase DATABASE_URL: ").strip()
    
    if not DATABASE_URL:
        print("❌ Error: DATABASE_URL is required")
        sys.exit(1)

print("\nConnecting to Supabase...")
print(f"Host: {DATABASE_URL.split('@')[1].split('/')[0] if '@' in DATABASE_URL else 'unknown'}")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("✅ Connected successfully!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\nTroubleshooting:")
    print("1. Check your DATABASE_URL is correct")
    print("2. Verify your Supabase project is active")
    print("3. Check your database password")
    print("4. Format: postgresql://postgres:PASSWORD@db.xxx.supabase.co:5432/postgres")
    sys.exit(1)

print("\n" + "="*60)
print("Creating tables...")
print("="*60)

tables_created = 0

# Users table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        register_number TEXT UNIQUE NOT NULL,
        department TEXT NOT NULL,
        total_points INTEGER DEFAULT 0,
        current_streak INTEGER DEFAULT 0,
        best_streak INTEGER DEFAULT 0,
        badges TEXT DEFAULT '[]',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    tables_created += 1
    print("✅ 1/11 Users table")
except Exception as e:
    print(f"❌ Users table failed: {e}")

# Admins table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    tables_created += 1
    print("✅ 2/11 Admins table")
except Exception as e:
    print(f"❌ Admins table failed: {e}")

# Biographies table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS biographies (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        person_name TEXT NOT NULL,
        content TEXT NOT NULL,
        profession TEXT NOT NULL,
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (created_by) REFERENCES admins (id)
    )''')
    tables_created += 1
    print("✅ 3/11 Biographies table")
except Exception as e:
    print(f"❌ Biographies table failed: {e}")

# Daily quotes table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_quotes (
        id SERIAL PRIMARY KEY,
        quote TEXT NOT NULL,
        author TEXT,
        posted_by INTEGER NOT NULL,
        department TEXT NOT NULL,
        post_date DATE NOT NULL,
        is_featured BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (posted_by) REFERENCES users (id)
    )''')
    tables_created += 1
    print("✅ 4/11 Daily quotes table")
except Exception as e:
    print(f"❌ Daily quotes table failed: {e}")

# Listening content table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS listening_content (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        audio_file TEXT NOT NULL,
        transcript TEXT NOT NULL,
        robot_character TEXT DEFAULT 'boy',
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (created_by) REFERENCES admins (id)
    )''')
    tables_created += 1
    print("✅ 5/11 Listening content table")
except Exception as e:
    print(f"❌ Listening content table failed: {e}")

# Observation content table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS observation_content (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        video_url TEXT NOT NULL,
        questions TEXT NOT NULL,
        correct_answers TEXT NOT NULL,
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (created_by) REFERENCES admins (id)
    )''')
    tables_created += 1
    print("✅ 6/11 Observation content table")
except Exception as e:
    print(f"❌ Observation content table failed: {e}")

# Writing topics table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS writing_topics (
        id SERIAL PRIMARY KEY,
        topic TEXT NOT NULL,
        description TEXT,
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (created_by) REFERENCES admins (id)
    )''')
    tables_created += 1
    print("✅ 7/11 Writing topics table")
except Exception as e:
    print(f"❌ Writing topics table failed: {e}")

# Tasks table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        department TEXT DEFAULT 'ALL',
        due_date DATE,
        is_active BOOLEAN DEFAULT TRUE,
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        module_type TEXT,
        content_id INTEGER,
        FOREIGN KEY (created_by) REFERENCES admins (id)
    )''')
    tables_created += 1
    print("✅ 8/11 Tasks table")
except Exception as e:
    print(f"❌ Tasks table failed: {e}")

# User completions table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_completions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        module_type TEXT NOT NULL,
        content_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        points_earned INTEGER NOT NULL,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    tables_created += 1
    print("✅ 9/11 User completions table")
except Exception as e:
    print(f"❌ User completions table failed: {e}")

# User streaks table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_streaks (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        streak_date DATE NOT NULL,
        modules_completed INTEGER DEFAULT 0,
        points_earned INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    tables_created += 1
    print("✅ 10/11 User streaks table")
except Exception as e:
    print(f"❌ User streaks table failed: {e}")

# Speaking attempts table
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS speaking_attempts (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        bio_id INTEGER NOT NULL,
        attempt_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (bio_id) REFERENCES biographies (id)
    )''')
    tables_created += 1
    print("✅ 11/11 Speaking attempts table")
except Exception as e:
    print(f"❌ Speaking attempts table failed: {e}")

conn.commit()

print("\n" + "="*60)
print(f"Tables created: {tables_created}/11")
print("="*60)

if tables_created < 11:
    print("\n⚠️  Warning: Some tables failed to create")
    print("Check the errors above and try again")
else:
    print("\n✅ All tables created successfully!")

# Insert sample data
print("\n" + "="*60)
print("Inserting sample data...")
print("="*60)

try:
    cursor.execute("SELECT * FROM admins WHERE username = 'admin'")
    if not cursor.fetchone():
        # Insert default admin
        admin_password_hash = generate_password_hash('admin123')
        cursor.execute("INSERT INTO admins (username, password_hash) VALUES (%s, %s) RETURNING id", 
                       ('admin', admin_password_hash))
        admin_id = cursor.fetchone()[0]
        print("✅ Admin user created")
        print("   Username: admin")
        print("   Password: admin123")
        
        # Insert sample biographies
        sample_biographies = [
            ("MS Dhoni - The Captain Cool", "Mahendra Singh Dhoni", 
             "Mahendra Singh Dhoni, known as Captain Cool, is one of the greatest cricket captains in history. Born on July 7, 1981, in Ranchi, Jharkhand, Dhoni rose from a small town to lead India to victory in the 2007 T20 World Cup, 2011 Cricket World Cup, and 2013 Champions Trophy. His calm demeanor under pressure and lightning-fast wicket-keeping skills made him a legend. Dhoni's leadership style was unique - he led by example, never panicked, and always believed in his team. Even in the most challenging situations, he maintained his composure and made strategic decisions that turned matches around.", 
             "Cricketer", admin_id),
            ("Dr. APJ Abdul Kalam - The Missile Man", "Dr. APJ Abdul Kalam",
             "Dr. Avul Pakir Jainulabdeen Abdul Kalam, known as the Missile Man of India, was born on October 15, 1931, in Rameswaram, Tamil Nadu. From humble beginnings selling newspapers to becoming India's 11th President, Dr. Kalam's journey is truly inspiring. He played a pivotal role in India's space and missile programs, leading projects like Agni and Prithvi missiles. His vision for India as a developed nation by 2020 motivated millions. Dr. Kalam was not just a scientist but also a teacher who loved interacting with students. His simplicity, dedication to education, and unwavering belief in the power of dreams made him the People's President.",
             "Scientist", admin_id)
        ]
        
        for title, name, content, profession, created_by in sample_biographies:
            cursor.execute("INSERT INTO biographies (title, person_name, content, profession, created_by) VALUES (%s, %s, %s, %s, %s)",
                           (title, name, content, profession, created_by))
        print("✅ Sample biographies inserted (2)")
        
        # Insert sample listening content
        sample_listening = [
            ("Robot Greeting", "audio_greeting.mp3", 
             "Hello there! Welcome to the Shakespeare Club Communication App. I am your friendly learning companion. Today we will practice listening skills together. Are you ready to begin this exciting journey of improving your English communication? Let's start with something fun and educational!",
             "boy", admin_id),
            ("Daily Motivation", "audio_motivation.mp3",
             "Good morning, dear students! Every day is a new opportunity to learn something amazing. Remember, communication is not just about speaking - it's about connecting with others, sharing ideas, and building relationships. Practice makes perfect, so keep working on your skills. You are capable of achieving great things!",
             "girl", admin_id)
        ]
        
        for title, audio_file, transcript, robot_character, created_by in sample_listening:
            cursor.execute("INSERT INTO listening_content (title, audio_file, transcript, robot_character, created_by) VALUES (%s, %s, %s, %s, %s)",
                           (title, audio_file, transcript, robot_character, created_by))
        print("✅ Sample listening content inserted (2)")
        
        # Insert sample observation content
        sample_observation = [
            ("Success Mindset", "https://www.youtube.com/watch?v=motivational1",
             "What are the key points mentioned about achieving success? List three important qualities discussed in the video.",
             "Hard work, Perseverance, Positive attitude", admin_id),
            ("Communication Skills", "https://www.youtube.com/watch?v=communication1",
             "According to the video, what makes effective communication? Name two important elements.",
             "Active listening, Clear expression", admin_id)
        ]
        
        for title, video_url, questions, answers, created_by in sample_observation:
            cursor.execute("INSERT INTO observation_content (title, video_url, questions, correct_answers, created_by) VALUES (%s, %s, %s, %s, %s)",
                           (title, video_url, questions, answers, created_by))
        print("✅ Sample observation content inserted (2)")
        
        # Insert sample writing topics
        sample_topics = [
            ("My Dreams and Aspirations", "Write about your future goals and how you plan to achieve them.", admin_id),
            ("The Importance of Communication", "Explain why good communication skills are essential in today's world.", admin_id),
            ("A Person Who Inspires Me", "Describe someone who motivates you and explain why they are your inspiration.", admin_id)
        ]
        
        for topic, description, created_by in sample_topics:
            cursor.execute("INSERT INTO writing_topics (topic, description, created_by) VALUES (%s, %s, %s)",
                           (topic, description, created_by))
        print("✅ Sample writing topics inserted (3)")
        
        conn.commit()
        print("\n✅ All sample data inserted successfully!")
    else:
        print("ℹ️  Admin user already exists")
        print("   Sample data was already inserted")
        print("   Skipping data insertion")
        
except Exception as e:
    print(f"❌ Error inserting sample data: {e}")
    conn.rollback()

conn.close()

print("\n" + "="*60)
print("🎉 Supabase database setup complete!")
print("="*60)
print("\nDefault Admin Credentials:")
print("  Username: admin")
print("  Password: admin123")
print("\n⚠️  Remember to change the admin password after first login!")
print("\nYou can now run your app with:")
print("  python app.py")
print("\nOr deploy to Render with DATABASE_URL environment variable set.")
print("\n" + "="*60)
