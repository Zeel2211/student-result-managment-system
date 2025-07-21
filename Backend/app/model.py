def create_tables():
    from app.db import cursor, conn
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password_hash VARCHAR(128),
            role VARCHAR(10)
        );
        
        CREATE TABLE IF NOT EXISTS results (
            id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES users(id),
            subject VARCHAR(100),
            marks INTEGER,
            grade VARCHAR(2)
        );
    ''')
    conn.commit()
