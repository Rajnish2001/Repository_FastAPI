from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from blog.schemas import Blog,ShowBlog
from blog.database import SessionLocal,get_db
from blog import models
from blog.repository.blog import create_blog,get_all_blog,retrive_blog,delete_blog


router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def blog(request:Blog,db:SessionLocal=Depends(get_db)):
    return create_blog(request,db)


@router.get('/',response_model=List[ShowBlog],status_code=status.HTTP_200_OK)
def all_blog(db:SessionLocal=Depends(get_db)):
    return get_all_blog(db)

@router.get('/{id}',response_model=ShowBlog,status_code=status.HTTP_200_OK)
def blog(id,db:SessionLocal=Depends(get_db)):
    return retrive_blog(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db:SessionLocal=Depends(get_db)):
    return delete_blog(id,db)