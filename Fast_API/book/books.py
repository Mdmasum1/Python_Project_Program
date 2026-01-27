#Create my first APi endpoints
from fastapi import FastAPI

app = FastAPI()  #Create fast api object


async def first_api():
    return {"message": "Hello Eric!"}










