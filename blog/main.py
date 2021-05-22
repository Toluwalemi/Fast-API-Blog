from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import schemas, models
from .database import engine
from .helpers import get_db

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
