

import sys
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def say_hello():
    """Return a friendly greeting."""
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    DEFAULT_PORT = 8000
    try:
        PORT = int(sys.argv[1])
    except (IndexError, ValueError):
        PORT = DEFAULT_PORT
    uvicorn.run(app, host="0.0.0.0", port=PORT, reload=False)
