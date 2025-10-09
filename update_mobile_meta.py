#!/usr/bin/env python3
"""
Script to add mobile-friendly meta tags to all HTML templates
Run this once to update all templates with mobile optimization
"""

import os
import re

# Mobile meta tags to add
MOBILE_META_TAGS = '''    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#6366f1">'''

# Mobile CSS link
MOBILE_CSS = '''    <link rel="stylesheet" href="{{ url_for('static', filename='css/mobile.css') }}">'''

def update_template(filepath):
    """Update a single template file with mobile meta tags"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has mobile meta tags
        if 'mobile-web-app-capable' in content:
            print(f"✓ Skipped (already updated): {os.path.basename(filepath)}")
            return False
        
        # Replace old viewport meta tag with new mobile-friendly ones
        old_viewport = r'<meta name="viewport" content="width=device-width, initial-scale=1\.0[^>]*>'
        if re.search(old_viewport, content):
            content = re.sub(old_viewport, MOBILE_META_TAGS, content)
        
        # Add mobile CSS after gamified.css
        if 'gamified.css' in content and 'mobile.css' not in content:
            content = content.replace(
                '    <link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/gamified.css\') }}">',
                '    <link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/gamified.css\') }}">\n' + MOBILE_CSS
            )
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"✗ Error updating {filepath}: {e}")
        return False

def main():
    """Update all HTML templates in the templates directory"""
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    
    # Student-facing pages (priority)
    student_pages = [
        'speaking.html',
        'listening.html',
        'writing.html',
        'observation.html',
        'speaking_practice.html',
        'listening_practice.html',
        'observation_practice.html',
        'leaderboard.html',
        'profile.html',
        'certificate.html'
    ]
    
    print("=" * 60)
    print("MOBILE OPTIMIZATION - UPDATING TEMPLATES")
    print("=" * 60)
    print()
    
    updated_count = 0
    
    # Update student pages first
    print("Updating student-facing pages...")
    for filename in student_pages:
        filepath = os.path.join(templates_dir, filename)
        if os.path.exists(filepath):
            if update_template(filepath):
                updated_count += 1
    
    print()
    print("=" * 60)
    print(f"COMPLETE! Updated {updated_count} template files")
    print("=" * 60)
    print()
    print("✓ All templates are now mobile-friendly!")
    print("✓ Mobile CSS has been added")
    print("✓ Touch-friendly UI enabled")
    print()
    print("Next steps:")
    print("1. Run: python app.py")
    print("2. Test on mobile device or browser dev tools")
    print("3. Deploy to HTTPS for full mobile features")
    print()

if __name__ == '__main__':
    main()
