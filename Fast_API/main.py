
from fastapi import FastAPI
from typing import Union

#Create fast api object
app = FastAPI()

@app.get("/")  # use this decorator to allow this path or route
def read_root():
    return {"Hello": "world"} # use dictionary that automatically convert to json



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

