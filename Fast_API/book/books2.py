from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

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
        self.description = description
        self.author = author
        self.rating = rating

#pydantic/BaseModel for more and more data validation
class BookRequest(BaseModel):

    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt = 0, lt=6)

    #To pre-populate something very specufic , we can do this by using model_config
    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title" : "A new book",
                "author": "MD",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    }



# Inside BOOK , create some book object and return the BOOK
#list of book

BOOKS = [

    Book(1, "Computer Science Pro", "Codingwihtmd", 'A very nice book!', 5),
    Book(2, "Be Fast with FasAPI", "Codingwihtmd", 'A great book!', 5),
    Book(3, "Master Endpoints", "Codingwihtmd", 'A awesome book!', 5),
    Book(4, "Hp1", "Author 1", 'Book Description', 2),
    Book(5, "Hp2", "Author 2", 'Book Description', 3),
    Book(6, "Hp3", "Author 3", 'Book Description', 1)


]




#Create the first APi endpoint 
@app.get("/books")
async def read_all_books():
    return BOOKS

#Create post api endpoint
@app.post("/create_book")
async def creat_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump()) #You can also use dict() instead but it is old way
    #print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1

    else: # if there is no book then create new book wiht id one
        book.id = 1

    return book
        








