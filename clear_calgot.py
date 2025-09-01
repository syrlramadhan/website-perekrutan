#!/usr/bin/env python3

"""
Script to clear calgot table
"""

import sqlite3
import os

def clear_calgot_table():
    db_path = 'app.db'
    
    print(f"Looking for database at: {os.path.abspath(db_path)}")
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} not found!")
        return False
    
    try:
        print("Connecting to database...")
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check current count
        cursor.execute("SELECT COUNT(*) FROM calgot")
        before_count = cursor.fetchone()[0]
        print(f"Records before deletion: {before_count}")
        
        # Delete all records from calgot table
        print("Deleting all records from calgot table...")
        cursor.execute("DELETE FROM calgot")
        
        # Reset auto-increment counter (if table exists)
        print("Resetting auto-increment counter...")
        try:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='calgot'")
            print("Auto-increment counter reset")
        except sqlite3.OperationalError:
            print("No sqlite_sequence table found (normal for tables without autoincrement)")
        
        # Commit changes
        print("Committing changes...")
        conn.commit()
        
        # Verify deletion
        cursor.execute("SELECT COUNT(*) FROM calgot")
        count = cursor.fetchone()[0]
        
        conn.close()
        
        print(f"Calgot table cleared successfully! Records remaining: {count}")
        return True
        
    except Exception as e:
        print(f"Error clearing calgot table: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    clear_calgot_table()
