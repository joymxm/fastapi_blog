from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.blog_schema import BlogCreate, ShowBlog
from db.repository.blog_repo import create_new_blog, retrieve_blog, retrieve_all_blogs

router = APIRouter()


@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
 
    new_blog = create_new_blog(blog=blog, db=db)
    return new_blog


@router.get("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def get_blog(id: int, db: Session = Depends(get_db)):
 
    blog = retrieve_blog(id=id, db=db)

    if not blog:
        raise HTTPException(detail=f'blog with {id} does not exist', status_code=HTTP_404_NOT_FOUND)
    return blog


@router.get("", response_model=List[ShowBlog])
def get_all_blogs( db: Session = Depends(get_db)): 
    blogs = retrieve_all_blogs(db=db)
    return blogs