from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

@app.get('/blog')
def index(limit=10,published: bool=False, sort: Optional[str]=None):    
   if published:
       return {'data': f"{limit} published blog from db"} 
   else:
    return {published}

@app.get('/blog/unpublished')
def unpublished():
   return{'data':'unpublished blogs'}

@app.get('/blog/{id}')
def blogs(id:int):
    return{'data':id,}



@app.get('/blog/{id}/comments')
def comments(id):
    return{'data':{'2','1'}}

class Blog(BaseModel):
        pass
    
@app.post('/blog')
def create_blog(req: Blog):
        return{'data':'blog created'}
    
    
