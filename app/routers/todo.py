from fastapi import APIRouter, Depends
from fastapi.param_functions import Path
from sqlalchemy.orm import Session
from app import schemas, crud, authentication
from app.database import get_db

router = APIRouter(tags=["Todos"])


@router.post("/create-todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.create_todo(db, todo=todo, user_id=current_user.id)


@router.get("/get-todos", response_model=schemas.Todos)
def get_todos(db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.get_todos(db=db, user_id=current_user.id)


@router.patch("/toggle-complete/{todo_id}", response_model=schemas.Todo)
def toggle_complete(todo_id: int, db: Session = Depends(get_db),  current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.toggle_complete(db=db, todo_id=todo_id, current_user_id=current_user.id)


@router.delete("/delete-todo/{todo_id}", response_model=schemas.TodoDelete)
def delete_todo(todo_id: int = Path(None, description="The ID of the todo to delete"), db: Session = Depends(get_db),  current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.delete_todo(db=db, todo_id=todo_id, current_user_id=current_user.id)
