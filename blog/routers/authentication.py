from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from blog import models
from blog.helpers.db_helpers import get_db
from blog.helpers.hashing import verify
from blog.schemas import Login

router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    if not verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    # generate jwt token
    return user
