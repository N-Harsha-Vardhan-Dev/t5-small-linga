"""
Temporary in-memory database.
Can be replaced with MongoDB / PostgreSQL without changing API contracts.
"""

users_db: dict[str, str] = {}

def get_user(username: str):
    return users_db.get(username)

def create_user(username: str, hashed_password: str):
    users_db[username] = hashed_password

def user_exists(username: str) -> bool:
    return username in users_db
