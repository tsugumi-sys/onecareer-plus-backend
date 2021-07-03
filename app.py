from typing import Optional
from fastapi import FastAPI, Query, Path, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from google_test import google_account


app = FastAPI()

templates = Jinja2Templates(directory='templates')
@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/test')
async def index():
    return { 'message': 'Hello World' }

@app.get('/goog')
async def goog():
    res = google_account()
    return res

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))