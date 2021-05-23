from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models
from blog.helpers.hashing import bcrypt


def create_user_helper(request, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_helper(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    return user
