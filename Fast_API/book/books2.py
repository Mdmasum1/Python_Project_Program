from fastapi import FastAPI

app = FastAPI()

BOOKS = []


#Create the first APi endpoint 
@app.get("/books")
async def read_all_books():
    return BOOKS

