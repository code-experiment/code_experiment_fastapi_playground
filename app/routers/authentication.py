from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import crud, models, authentication, schemas
from app.database import get_db

router = APIRouter(tags=["Auth"])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect username or password.")
    if not authentication.Hash.verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect username or password.")

    access_token = authentication.create_access_token(
        data={"username": user.username, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/check-login', response_model=schemas.User)
def check_login(db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.get_user(db, user_id=current_user.id)
