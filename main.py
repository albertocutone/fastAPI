from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog/')
def create_blog(request: Blog):
    return {'data', f"Blog is created with {request.title}"}

@app.get('/blog')
def index(limit = 10, published : bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} blog list' }
    else:
        return {'data':{'NO'}}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'2',id}}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)


