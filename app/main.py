 

from fastapi import FastAPI

from app.routers.vote import vote
from . import models
from .database import engine
from .routers import post, users, auth , vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from tkinter import tkinter 







# models.Base.metadata.create_all(bind=engine) # commented becase now alembic is genetatic the table for us

app = FastAPI()

##### lIST OF origins

origins = ['*']


# #  pasting CORAS CODE #################
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# # #####################################
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)




@app.get("/")
async def root():
    return{"message":"Hello world == 123 "}
