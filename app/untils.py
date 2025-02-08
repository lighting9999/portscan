import sqlite3
# 初始化数据库
def init_db():
    conn = sqlite3.connect('scanner_history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scan_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip TEXT,
                        port INTEGER,
                        status TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
