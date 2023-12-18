from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'message' : 'First step PP2P'}


