from sqlalchemy.orm import Session
from blog import models
from fastapi import HTTPException,status


def create_blog(request,db:Session):
    blog_data = models.Blog(title=request.title,blog=request.blog,creator_id=request.creator_id)
    db.add(blog_data)
    db.commit()
    db.refresh(blog_data)
    return blog_data

def get_all_blog(db:Session):
    blog = db.query(models.Blog).all()
    return blog

def retrive_blog(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'Blog id {id} is Not Found!')
    return blog

def delete_blog(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'Blog id {id} is Not Found!')
    # db.delete(blog)
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog is deleted'