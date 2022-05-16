import sqlite3

conn = sqlite3.connect('./database/database1.db')
c = conn.cursor()

# c.execute("DROP TABLE filo_users;")
# c.execute("DROP TABLE user_files;")

c.execute("""CREATE TABLE IF NOT EXISTS  filo_users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")

c.execute("""
    CREATE TABLE IF NOT EXISTS  user_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    filename TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES users (id)
)""")

c.execute("INSERT INTO filo_users (username) VALUES (?)", ('Abhinav',))
c.execute("INSERT INTO filo_users (username) VALUES (?)", ('Patel',))
c.execute("INSERT INTO filo_users (username) VALUES (?)", ('Shivhare',))

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (1, 'hello'))

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (2, 'doof')
          )

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (2, 'react')
          )

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (2, 'backend')
          )

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (2, 'mongo_db')
          )

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (3, 'Angular')
          )

c.execute("INSERT INTO user_files (file_id, filename) VALUES (?, ?)",
          (3, 'nodejs')
          )

conn.commit()

c.execute("select filename from user_files where file_id=?", (2,))
# c.execute("SELECT i.filename FROM user_files i JOIN filo_users l ON i.file_id = l.id ORDER BY l.username;")

details = c.fetchall()
print(details)
conn.close()
