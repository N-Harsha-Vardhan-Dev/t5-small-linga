from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.services.t5_service import t5_correct
from app.services.google_service import google_correct
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload["sub"]   

@router.post("/correct")
def grammar_api(text: str, 
                engine: str = "t5",
                user=Depends(get_current_user)):
    try : 
        if engine == "t5":
            corrected = t5_correct(text)

        elif engine == "google":
            corrected = google_correct(text)

        else:
            raise HTTPException(status_code=400, detail="Invalid engine")
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"engine": engine, "user": user, "corrected_text": corrected}