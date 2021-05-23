from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas
from blog.helpers.db_helpers import get_db
from blog.helpers.user_helper import create_user_helper, get_user_helper

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post('/', response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return create_user_helper(request, db)


@router.get('/{id}', response_model=schemas.ShowUser, tags=["users"])
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_helper(id, db)
