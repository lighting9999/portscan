from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Port and Ping Scanner")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)