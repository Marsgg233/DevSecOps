```python
import os
from fastapi import FastAPI, HTTPException
import bcrypt

app = FastAPI()

LOG_FILE = os.getenv("LOG_FILE", "/var/log/app/app_logs.txt")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/hash")
def hash_password(password: str = "default_secret"):
    try:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        with open(LOG_FILE, "a") as f:
            f.write("Generated hash for a user\n")

        return {"hash": hashed.decode("utf-8")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
```
