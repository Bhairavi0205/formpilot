import sqlite3
import os

DB_PATH = "database/formpilot.db"

def init_db():
    """Create database and users table if not exists"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dob TEXT,
            gender TEXT,
            category TEXT,
            state TEXT,
            qualification TEXT,
            phone TEXT,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized!")

def save_profile(name, dob, gender, category, state, qualification, phone, email):
    """Save or update user profile"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if profile exists
    cursor.execute("SELECT id FROM user_profile LIMIT 1")
    existing = cursor.fetchone()
    
    if existing:
        # Update
        cursor.execute("""
            UPDATE user_profile SET
                name=?, dob=?, gender=?, category=?,
                state=?, qualification=?, phone=?, email=?,
                updated_at=CURRENT_TIMESTAMP
            WHERE id=?
        """, (name, dob, gender, category, state, qualification, phone, email, existing[0]))
    else:
        # Insert new
        cursor.execute("""
            INSERT INTO user_profile 
            (name, dob, gender, category, state, qualification, phone, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, dob, gender, category, state, qualification, phone, email))
    
    conn.commit()
    conn.close()
    return True

def get_profile():
    """Get user profile from database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM user_profile LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            "id": row[0],
            "name": row[1],
            "dob": row[2],
            "gender": row[3],
            "category": row[4],
            "state": row[5],
            "qualification": row[6],
            "phone": row[7],
            "email": row[8]
        }
    return None

def delete_profile():
    """Delete user profile"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_profile")
    conn.commit()
    conn.close()
    return True