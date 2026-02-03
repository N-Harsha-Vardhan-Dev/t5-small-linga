from fastapi import APIRouter, HTTPException
from app.auth.schemas import UserRegister, UserLogin, TokenResponse
from app.auth.jwt_handler import create_access_token
from app.utils.security import hash_password, verify_password
from app.db.fake_db import get_user, create_user, user_exists

router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    if user_exists(user.username):
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = hash_password(user.password)
    create_user(user.username, hashed_pw)

    return {"message": "User registered successfully"}

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    stored_password = get_user(user.username)

    if not stored_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token}
