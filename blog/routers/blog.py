from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas
from blog.helpers.blog_helper import get_all, create, destroy_helper, update_helper, show
from blog.helpers.db_helpers import get_db

router = APIRouter(
    prefix="/items",
    tags=["blogs"]
)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_posts(db: Session = Depends(get_db)):
    return get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create_blog_post(request: schemas.Blog, db: Session = Depends(get_db)):
    return create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def destroy(id, db: Session = Depends(get_db)):
    return destroy_helper(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return update_helper(id, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
def get_single_id(id, db: Session = Depends(get_db)):
    return show(id, db)
