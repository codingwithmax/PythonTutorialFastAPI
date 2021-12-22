from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse


app = FastAPI()


@app.get("/test", response_class=JSONResponse)
def test_endpoint():
    return {"test key": "some value", "another key": 'another value', 4: "some more values", 5: 4,
            "nested key": {"some internal key": "some internal value"}}


@app.get("/", response_class=PlainTextResponse)
def home():
    return "welcome"
