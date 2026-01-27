
from fastapi import FastAPI 


app = FastAPI()  #Create fast api object


@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello Eric!"}










