from fastapi import FastAPI
from .routes import data_ingestion, query_and_submission, configuration

app = FastAPI()

# Include API routes
app.include_router(data_ingestion.router)
app.include_router(query_and_submission.router)
app.include_router(configuration.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Communications Assistant Backend"}
