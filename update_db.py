#!/usr/bin/env python3

"""
Script to update database schema by adding new columns
"""

import sqlite3
import os

def update_database():
    db_path = 'app.db'
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} not found!")
        return False
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if columns already exist
        cursor.execute("PRAGMA table_info(calgot)")
        columns = [column[1] for column in cursor.fetchall()]
        
        print("Current columns:", columns)
        
        # Add username_telegram column if it doesn't exist
        if 'username_telegram' not in columns:
            print("Adding username_telegram column...")
            cursor.execute("ALTER TABLE calgot ADD COLUMN username_telegram VARCHAR(64)")
            print("✓ username_telegram column added")
        else:
            print("✓ username_telegram column already exists")
        
        # Add pilihan_tinggal column if it doesn't exist
        if 'pilihan_tinggal' not in columns:
            print("Adding pilihan_tinggal column...")
            cursor.execute("ALTER TABLE calgot ADD COLUMN pilihan_tinggal VARCHAR(32)")
            print("✓ pilihan_tinggal column added")
        else:
            print("✓ pilihan_tinggal column already exists")
        
        # Commit changes
        conn.commit()
        
        # Verify new structure
        cursor.execute("PRAGMA table_info(calgot)")
        new_columns = [column[1] for column in cursor.fetchall()]
        print("Updated columns:", new_columns)
        
        conn.close()
        print("Database update completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error updating database: {e}")
        return False

if __name__ == "__main__":
    update_database()
