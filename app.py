from typing import Optional
from fastapi import FastAPI, Query, Path, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

templates = Jinja2Templates(directory='templates')
@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/test')
async def index():
    return { 'message': 'Hello World' }

@app.post("/items/")
async def create_item(item: Item):
    return item

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))