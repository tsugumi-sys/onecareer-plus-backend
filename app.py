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
from google_sheets import get_all_posts, google_account, search_posts

app = FastAPI()

templates = Jinja2Templates(directory='templates')
@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/get_all_posts/')
async def getAllPosts():
    res = get_all_posts(RANGE_NAME='Posts!A1:H')
    return res

@app.get('/search_posts/')
async def searchPosts(
    bf_industry_id: Optional[int] = Query(
        None,
        title='Indutry ID of before',
        description='bf_industry_idの値'
    ),
    af_industry_id: Optional[int] = Query(
        None,
        title='Indutry ID of after',
        description='af_industry_idの値'
    )
):
    res = search_posts(RANGE_NAME='Posts!A1:H', bf_industry_id=bf_industry_id, af_industry_id=af_industry_id)
    return res

    


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))