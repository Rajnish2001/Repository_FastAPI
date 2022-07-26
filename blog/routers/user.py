from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from blog.schemas import User,ShowUser,UserView
from blog.database import SessionLocal,get_db
from blog import models
from ..repository.user import Create_user,get_all_user,retrive_user,delete_user

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post('/',response_model=UserView,status_code=status.HTTP_200_OK)
def user(request:User,db:SessionLocal=Depends(get_db)):
    # hash_password = pwd_context.hash(request.password)
    return Create_user(request,db)


@router.get('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
def all_user(db:SessionLocal=Depends(get_db)):
    return get_all_user(db)

@router.get('/{id}',status_code=status.HTTP_200_OK)
def user(id,db:SessionLocal=Depends(get_db)):
    return retrive_user(id,db)


@router.delete('/{id}',status_code=status.HTTP_202_ACCEPTED)
def delete_user(id,db:SessionLocal=Depends(get_db)):
    # user = db.query(models.User).filter(models.User.id==id).first()
    # if user is None:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'User id {id} is Not Found!')
    # db.delete(user)
    # db.commit()
    # return 'User is deleted'
    return delete_user(id,db)