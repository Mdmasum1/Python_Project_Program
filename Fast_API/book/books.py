
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

@app.get("/books/mybook")
async def read_all_books():
    return {"book_title": 'My favorite book!'}

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
   return {'dynamic_param' : dynamic_param}










