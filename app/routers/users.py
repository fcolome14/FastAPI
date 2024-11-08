from fastapi import FastAPI, Response, HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
import app.models as models, app.schemas as schemas, app.utils as utils

router = APIRouter(prefix="/users", tags=['Users'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def add_users(users: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #Hash pwd
    hashed_pwd = utils.hash(users.password)
    users.password = hashed_pwd
    
    print(users.model_dump()) #-->Converts input schema to the expected format mapping for the query
    new_user = models.Users(**users.model_dump())
    db.add(new_user)
    db.commit()
    
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_users(id: int, db: Session = Depends(get_db)):
    users = db.query(models.Users).filter(models.Users.id == id).first()
    
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{str(id)} not found")
    return users