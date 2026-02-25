from fastapi import HTTPException, Header
from jose import jwt

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def get_current_user(authorization: str = Header(...)):
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")