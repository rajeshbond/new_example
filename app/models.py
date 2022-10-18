
from enum import unique    # added 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey #added 
from sqlalchemy.sql.sqltypes import TIMESTAMP # added 
from sqlalchemy.orm import relationship # added 
from sqlalchemy.sql.expression import text  #added 
from .database import Base #added


class Post(Base):
    __tablename__ = "posts1"
    id = Column(Integer, primary_key=True, nullable = False)
    title = Column(String,nullable = False)
    content = Column(String,nullable = False)
    publish = Column(Boolean, server_default = "True", nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False,
                        server_default = text('now()') )     # need to import text for SQL express 
    owner_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"),nullable = False)
    owner = relationship("User")
    
       
class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True, nullable = False)
    email = Column(String,nullable = False, unique = True)
    password = Column(String,nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False,
                        server_default = text('now()') ) 
    phone = Column(String)
    # need to import text for SQL express 
    
 
class Votes(Base):
    __tablename__ = "votes"
    post_id = Column(Integer,
                     ForeignKey("posts1.id",ondelete="CASCADE"),
                     primary_key = True)
    user_id = Column(Integer,
                     ForeignKey("users.id",ondelete="CASCADE"),
                     primary_key = True)
    
