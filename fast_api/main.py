from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message":"Hello FastAPI!!"
    }


@app.get("/hello")
def home():
    return {
        "message":"Hello there!"
    }

@app.get("/about")
def about():
    return {
        "message":"FastAPI application!"
    }

@app.get("/health")
def health():
    return {
        "Status":"Health"
    }

