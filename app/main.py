from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import crud, models, schemas, authentication
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Username")
    if not authentication.Hash.verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")

    access_token = authentication.create_access_token(
        data={"username": user.username, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/create_todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.create_todo(db, todo=todo, user_id=current_user.id)


@app.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


@app.get('/get-user/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)
