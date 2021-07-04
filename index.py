from fastapi import FastAPI, Query, Path, Request 
from pydantic import BaseModel

class Post(BaseModel):
    user_id: int
    bf_industry_id: int
    af_industry_id: int
    bf_company_id: int
    af_company_id: int
    reason: str
    point: str

app = FastAPI()

@app.get("/posts/")
async def index():
    res = google_account('Users!A1:B')
    return res