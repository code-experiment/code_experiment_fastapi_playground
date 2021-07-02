from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, authentication
from app.database import get_db

router = APIRouter(tags=["Users"])


@router.post("/create-user", response_model=schemas.Token)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user=user)
    access_token = authentication.create_access_token(
        data={"username": new_user.username, "id": new_user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/get-user/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)


@router.delete('/delete-user', response_model=schemas.UserDelete)
def delete_user(db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.delete_user(db, user_id=current_user.id)
