from typing import Optional
from fastapi import FastAPI, Query, Path, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os
#from google_test import google_account
from index import index

# GET Method
from google_sheets import get_all_posts, google_account

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    name: str
    user_type: str
    major: str
    industry: str

app = FastAPI()

templates = Jinja2Templates(directory='templates')
@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/test')
async def index():
    return { 'message': 'Hello World' }

@app.get('/get_all_posts/')
async def getAllPosts():
    res = get_all_posts(RANGE_NAME='Posts!A1:H')
    return res
    
@app.get('/goog')
async def goog():
    res = google_account(RANGE_NAME='Users!A1:B')
    return res

@app.post("/items/")
async def create_item(item: Item):
    return item

# @app.get('/students/{student_id}')
# async def index(student_id: 1):
#     sql="select * from Student where id=1"
#     return cursor.execute(sql)

@app.post("/users")
async def create_item(user: User):
    return user

# @app.post("/posts")
# async def create_item(post: Post):
#     return post

# @app.post("/companies")
# async def create_item(company: Company):
#     return company

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))