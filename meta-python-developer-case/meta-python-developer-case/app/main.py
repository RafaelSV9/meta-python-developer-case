import os
import time
import requests
from app.db import get_connection, create_users_table, insert_users

def fetch_users_from_api():
    api_url = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/users")
    resp = requests.get(api_url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    users = []
    for u in data:
        users.append({
            "id": u.get("id"),
            "name": u.get("name"),
            "username": u.get("username"),
            "email": u.get("email"),
            "city": (u.get("address") or {}).get("city")
        })
    return users

def main():
    time.sleep(5)
    conn = None
    try:
        conn = get_connection()
        create_users_table(conn)
        users = fetch_users_from_api()
        insert_users(conn, users)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
