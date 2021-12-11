from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "New Hello World"
