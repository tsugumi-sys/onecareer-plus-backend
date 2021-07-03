from typing import Optional
from fastapi import FastAPI, Query, Path, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os

class Student(BaseModel):
    name: str
    major: str
    industry: str

class User(BaseModel):
    name: int
    bf_industry_id: int
    af_industry_id: int
    bf_company_id: int
    af_company_id: int

class Post(BaseModel):
    user_id: int
    major: str
    industry: str

class Company(BaseModel):
    name: str

app = FastAPI()

templates = Jinja2Templates(directory='templates')
@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/test')
async def index():
    return { 'message': 'Hello World' }

@app.get('/students/{student_id}')
async def index(student_id: 1):
    sql="select * from Student where id=1"
    return cursor.execute(sql)

@app.get('/posts')
async def index():
    return student

@app.post("/users")
async def create_item(user: User):
    return user

@app.post("/posts")
async def create_item(post: Post):
    return post

@app.post("/companies")
async def create_item(company: Company):
    return company

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))