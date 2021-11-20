from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!!!"}


@app.get("/ping/")
def return_ping():
    data = {"message": "pong"}
    return data

