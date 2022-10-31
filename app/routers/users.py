
import email
import re
from .. import models, schemas, utls # importing models schemase , utls  # added 
from .. import models, schemas, utls,oauth2 # importing models schemase , utls  # added
from fastapi import Response, status, HTTPException, Depends, APIRouter # added 
from sqlalchemy.orm import Session # added
from ..database import get_db #added


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
    
    already_user_query = db.query(models.User).filter(models.User.email == user.email)
    
    if already_user_query.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f" {user.email} already in use  , please chose another email") 
      
    
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
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f" {id} no user avalable ") 
    
    return user

# --------------------Search user by ID--------------------------------------------------

@router.patch("/changepwd",response_model= schemas.UserOut)
def password_rest(user:schemas.UserChangePassword, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user) ):
      
    if not utls.verify(user.password, current_user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")
       
    hased_password = utls.hash(user.password_new)
    user.password = hased_password
    current_user.password = user.password
    db.commit()
    return current_user
