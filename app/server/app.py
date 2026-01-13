from fastapi import FastAPI
from .routes.student import router as StudentRouter

app = FastAPI()
app.include_router(StudentRouter, tags= ["Student"], prefix="/student")

@app.get("/",tags=["Root"])
def read_root():
    return {"message":"helo world"}