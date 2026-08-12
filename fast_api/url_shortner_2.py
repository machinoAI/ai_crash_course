from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random
import string

app = FastAPI()

url_db = {}       # short_key -> long_url
long_to_short = {}  # long_url -> short_key
visits = {}       # short_key -> number of visits


def generate_key():
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=5))


@app.post("/", status_code=201)
def create_short_url(data: dict):

    if "long_url" not in data:
        raise HTTPException(
            status_code=422,
            detail="invalid input"
        )

    long_url = data["long_url"]

    # Same long URL → same short URL
    if long_url in long_to_short:
        key = long_to_short[long_url]

        return {
            "short_url": f"http://localhost:8000/{key}"
        }

    # Generate new key
    key = generate_key()

    while key in url_db:
        key = generate_key()

    # Store mappings
    url_db[key] = long_url
    long_to_short[long_url] = key

    # New URL starts with zero visits
    visits[key] = 0

    return {
        "short_url": f"http://localhost:8000/{key}"
    }


@app.get("/{key}")
def get_url(key: str):

    if key not in url_db:
        raise HTTPException(
            status_code=422,
            detail="invalid input"
        )

    # Count the visit
    visits[key] += 1

    return RedirectResponse(url=url_db[key])


@app.get("/info/{key}")
def get_info(key: str):

    # If short URL doesn't exist → 0 visits
    if key not in visits:
        return {
            "visits": 0
        }

    return {
        "visits": visits[key]
    }