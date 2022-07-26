from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from blog import models
from blog.hashing import Hash


def Create_user(request,db:Session):
    user = models.User(name=request.name,email=request.email,password=Hash(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_user(db:Session):
    user = db.query(models.User).all()
    return user


def retrive_user(id,db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'User id {id} is Not Found!')
    return user


def delete_user(id,db:Session):
    user = db.query(models.User).filter(models.User.id==id).delete(synchronize_session=False)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'User id {id} is Not Found!')
    # db.delete(user)
    # user.delete(synchronize_session=False)
    db.commit()
    return 'User is deleted'