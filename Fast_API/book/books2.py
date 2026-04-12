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

