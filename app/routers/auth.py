from fastapi import FastAPI, Response, HTTPException, status, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
import app.models as models
import app.schemas as schemas
import app.utils as utils
import app.oauth2 as oauth2

router = APIRouter(prefix="/login", tags=['Authentication'])

@router.post('/', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials") 
    #Same message to avoid giving clues about the failure
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    return {'access_token' : access_token, "token_type": "bearer"}