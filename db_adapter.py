"""
Database adapter to support both SQLite (local) and PostgreSQL (cloud/Render)
"""
import os
import sqlite3

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False


class DatabaseAdapter:
    """Unified database interface for SQLite and PostgreSQL"""
    
    def __init__(self, database_url=None, sqlite_path=None):
        self.database_url = database_url
        self.sqlite_path = sqlite_path
        self.use_postgres = database_url and POSTGRES_AVAILABLE
        
        # Fix Render's postgres:// to postgresql://
        if self.database_url and self.database_url.startswith('postgres://'):
            self.database_url = self.database_url.replace('postgres://', 'postgresql://', 1)
    
    def get_connection(self):
        """Get database connection (SQLite or PostgreSQL)"""
        if self.use_postgres:
            conn = psycopg2.connect(self.database_url)
            return conn
        else:
            conn = sqlite3.connect(self.sqlite_path)
            conn.row_factory = sqlite3.Row
            return conn
    
    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False, commit=False):
        """Execute a query and return results"""
        conn = self.get_connection()
        
        try:
            if self.use_postgres:
                cursor = conn.cursor(cursor_factory=RealDictCursor)
            else:
                cursor = conn.cursor()
            
            # Convert SQLite syntax to PostgreSQL if needed
            if self.use_postgres:
                query = self._convert_query_syntax(query)
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            result = None
            if fetch_one:
                result = cursor.fetchone()
            elif fetch_all:
                result = cursor.fetchall()
            
            if commit:
                conn.commit()
            
            cursor.close()
            conn.close()
            
            return result
        except Exception as e:
            conn.close()
            raise e
    
    def _convert_query_syntax(self, query):
        """Convert SQLite-specific syntax to PostgreSQL"""
        # Replace AUTOINCREMENT with SERIAL
        query = query.replace('INTEGER PRIMARY KEY AUTOINCREMENT', 'SERIAL PRIMARY KEY')
        query = query.replace('AUTOINCREMENT', '')
        
        # Replace BOOLEAN DEFAULT FALSE with proper PostgreSQL syntax
        query = query.replace('BOOLEAN DEFAULT FALSE', 'BOOLEAN DEFAULT FALSE')
        query = query.replace('BOOLEAN DEFAULT TRUE', 'BOOLEAN DEFAULT TRUE')
        
        # Replace DATE() function
        query = query.replace('DATE(', 'DATE(')
        
        # Replace ? placeholders with %s for PostgreSQL
        if self.use_postgres:
            # Count ? and replace with %s
            count = query.count('?')
            for _ in range(count):
                query = query.replace('?', '%s', 1)
        
        return query
    
    def init_database(self):
        """Initialize database schema"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Determine the right syntax based on database type
        if self.use_postgres:
            autoincrement = 'SERIAL PRIMARY KEY'
            timestamp_default = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        else:
            autoincrement = 'INTEGER PRIMARY KEY AUTOINCREMENT'
            timestamp_default = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        
        # Create tables
        tables = [
            f"""CREATE TABLE IF NOT EXISTS users (
                id {autoincrement},
                username TEXT UNIQUE NOT NULL,
                register_number TEXT UNIQUE NOT NULL,
                department TEXT NOT NULL,
                total_points INTEGER DEFAULT 0,
                current_streak INTEGER DEFAULT 0,
                best_streak INTEGER DEFAULT 0,
                badges TEXT DEFAULT '[]',
                created_at {timestamp_default}
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS admins (
                id {autoincrement},
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at {timestamp_default}
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS biographies (
                id {autoincrement},
                title TEXT NOT NULL,
                person_name TEXT NOT NULL,
                content TEXT NOT NULL,
                profession TEXT NOT NULL,
                created_by INTEGER,
                created_at {timestamp_default},
                FOREIGN KEY (created_by) REFERENCES admins (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS daily_quotes (
                id {autoincrement},
                quote TEXT NOT NULL,
                author TEXT,
                posted_by INTEGER NOT NULL,
                department TEXT NOT NULL,
                post_date DATE NOT NULL,
                is_featured BOOLEAN DEFAULT FALSE,
                created_at {timestamp_default},
                FOREIGN KEY (posted_by) REFERENCES users (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS listening_content (
                id {autoincrement},
                title TEXT NOT NULL,
                audio_file TEXT NOT NULL,
                transcript TEXT NOT NULL,
                robot_character TEXT DEFAULT 'boy',
                created_by INTEGER,
                created_at {timestamp_default},
                FOREIGN KEY (created_by) REFERENCES admins (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS observation_content (
                id {autoincrement},
                title TEXT NOT NULL,
                video_url TEXT NOT NULL,
                questions TEXT NOT NULL,
                correct_answers TEXT NOT NULL,
                created_by INTEGER,
                created_at {timestamp_default},
                FOREIGN KEY (created_by) REFERENCES admins (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS writing_topics (
                id {autoincrement},
                topic TEXT NOT NULL,
                description TEXT,
                created_by INTEGER,
                created_at {timestamp_default},
                FOREIGN KEY (created_by) REFERENCES admins (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS tasks (
                id {autoincrement},
                title TEXT NOT NULL,
                description TEXT,
                department TEXT DEFAULT 'ALL',
                due_date DATE,
                is_active BOOLEAN DEFAULT TRUE,
                created_by INTEGER,
                created_at {timestamp_default},
                module_type TEXT,
                content_id INTEGER,
                FOREIGN KEY (created_by) REFERENCES admins (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS user_completions (
                id {autoincrement},
                user_id INTEGER NOT NULL,
                module_type TEXT NOT NULL,
                content_id INTEGER NOT NULL,
                score INTEGER NOT NULL,
                points_earned INTEGER NOT NULL,
                completed_at {timestamp_default},
                FOREIGN KEY (user_id) REFERENCES users (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS user_streaks (
                id {autoincrement},
                user_id INTEGER NOT NULL,
                streak_date DATE NOT NULL,
                modules_completed INTEGER DEFAULT 0,
                points_earned INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )""",
            
            f"""CREATE TABLE IF NOT EXISTS speaking_attempts (
                id {autoincrement},
                user_id INTEGER NOT NULL,
                bio_id INTEGER NOT NULL,
                attempt_at {timestamp_default},
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (bio_id) REFERENCES biographies (id)
            )"""
        ]
        
        for table_sql in tables:
            try:
                cursor.execute(table_sql)
            except Exception as e:
                print(f"Error creating table: {e}")
        
        conn.commit()
        cursor.close()
        conn.close()
