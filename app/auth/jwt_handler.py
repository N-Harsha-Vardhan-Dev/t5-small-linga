from datetime import datetime, timedelta
import os
from jose import jwt


SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret")
# print(type(SECRET_KEY), repr(SECRET_KEY)) # Debug line to check SECRET_KEY value
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY not set")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
