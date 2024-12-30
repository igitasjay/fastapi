from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {"message": "Hello, World!"}

@app.get('/about')
async def about():
    return "An exceptional company"