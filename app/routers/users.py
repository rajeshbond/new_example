

from .. import models, schemas, utls # importing models schemase , utls 
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix= '/users',
     tags=["Users"]
)


#-------------------------------------- Fresh New User Creation code starts Here ----------------------------------

@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)

def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)): 
    
    # Hash the password - user.password 
    
    hased_password = utls.hash(user.password)
    user.password = hased_password
    new_user = models.User(**user.dict())
    db.add(new_user)  # need to add the post 
    db.commit()  
    db.refresh(new_user) # we need to retun the data base by refreshing the file 
    print(user)
    return new_user
#-------------USER CREATION ENDS HERE --------------------------------------------------
  
###########################Search user by ID ######################################

@router.get('/{id}',response_model=schemas.UserOut)
def get_user(id: int,db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"No Post avalable for ID {id}") 
    
    return user

#--------------------Search user by ID--------------------------------------------------
    