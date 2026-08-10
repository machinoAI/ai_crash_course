from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import string
import  secrets
from fastapi.responses import RedirectResponse


app = FastAPI()


temp_url_store= {}

# Request model

class URLRequest(BaseModel):
    url: HttpUrl



# Generate short code:

def generate_short_code(length: int = 6)
    characters = string.ascii_letters + string.digits
    return "".join((secrets.choice(characters))) for _ in range(length)

# create short url
@app.post("/shorten")
def shorten_url(request: URLRequest):

    short_code = generate_short_code()

    while short_code in temp_url_store:
        short_code = generate_short_code()

    temp_url_store[short_code] = str(request.url)

    return {

        "short_code":short_code,
        "shorten_url": f"http://localhost:8000/{short_code}"
    }



# Redirect short URL

@app.get("/{short_code}")
def redirect_url(short_code: str):
    original_url = temp_url_store.get(short_code)

    if not original_url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

     return RedirectResponse(
            url=original_url,
            status_code=307
        )

