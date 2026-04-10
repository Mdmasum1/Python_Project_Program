from fastapi import FastAPI

app = FastAPI()


#Here , we are going to create new book object from class Book
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    #Create constructor
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

# Inside BOOK , create some book object and return the BOOK

BOOKS = []





#Create the first APi endpoint 
@app.get("/books")
async def read_all_books():
    return BOOKS

