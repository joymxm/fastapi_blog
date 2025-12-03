from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.user_schema import UserCreate
from db.repository.user_repo import create_new_user
from schemas.user_schema import ShowUser

router = APIRouter()


# Response schema (excludes password)



@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user




    