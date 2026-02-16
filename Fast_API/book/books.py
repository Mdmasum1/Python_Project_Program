
from fastapi import FastAPI 


app = FastAPI()  #Create fast api object

#create a list of books
BOOKS = [

    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}

]

@app.get("/books")
async def read_all_books():
    return BOOKS

# @app.get("/books/mybook")
# async def read_all_books():
#     return {"book_title": 'My favorite book!'}

@app.get("/books/{book_title: str}")
async def read_books(book_title: str):
   for book in BOOKS:
       if book.get('title').casefold() == book_title.casefold():
           return book
   

#For query parameter
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []

    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return



        













