from fastapi import FastAPI
from src.products.router import router as prod_router
from src.summary.router import router as summary_router


app = FastAPI(debug=True)


@app.get("/")
def index():
    return {"message": "First step PP2P"}


app.include_router(prod_router)
app.include_router(summary_router)
