import sqlite3
import functools
from datetime import datetime  # ✅ Required for timestamp logging

# ✅ Decorator to log SQL queries with timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the SQL query
        if args:
            query = args[0]
        else:
            query = kwargs.get('query', '')
        
        # Log with timestamp
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Executing SQL Query: {query}")
        
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# ✅ Test the function
users = fetch_all_users(query="SELECT * FROM users")
print(users)
