"""
@app.get("/users")
async def get_users():
    time.sleep(5)
    return {"users": []}

Note:
    - time.sleep() is blocking.
    - You're inside an async endpoint but blocking the event loop.


"""
