from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import FileResponse
import logging


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # prefix
)
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
def health_check():
    query_parameter = Request.query_params
    logging.info(f"Health check endpoint called--with-query-parameter --> {query_parameter}")

    return {"status": "ok"}


@app.get('/log')
def log():
    return FileResponse("app.log", filename="app.log", media_type="text/plain")

# Sample endpoint
@app.get("/")
def root():
    return {"message": "FastAPI is running"}