"""
WSGI entry point for Vercel deployment
"""
from app import app

# Vercel expects 'app' or 'application' variable
application = app

if __name__ == "__main__":
    app.run()
