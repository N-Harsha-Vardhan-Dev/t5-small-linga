from fastapi import FastAPI
from app.auth.auth_router import router as auth_router
from app.routes.correct import router as correct_router
from dotenv import load_dotenv
load_dotenv(override=True)

app = FastAPI(title="Linga Grammar Correction API")

app.include_router(auth_router)
app.include_router(correct_router)
