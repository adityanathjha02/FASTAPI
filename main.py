from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
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
        title : str
        body : str
        published: Optional[bool]
    
    
    
@app.post('/blog')
def create_blog(blog: Blog):
    return{'data':f'{blog.title} blog created'}
    
    
# if __name__ == '__main__':
#         uvicorn.run(app, host='127.0.0.1', port=9000)
