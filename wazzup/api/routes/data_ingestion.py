from fastapi import APIRouter, Depends
from wazzup.core.tentacles import NotionImporter, TwitterImporter, FacebookImporter, QuoraImporter, RedditImporter, ChatGPTImporter
from wazzup.database.models import User
from wazzup.api.dependencies import get_current_user

router = APIRouter(prefix="/data-ingestion", tags=["Data Ingestion"])

@router.post("/notion/authenticate")
def authenticate_notion(credentials: dict, current_user: User = Depends(get_current_user)):
    importer = NotionImporter()
    importer.authenticate(credentials)
    return {"message": "Notion authentication successful"}

@router.post("/notion/fetch-data")
def fetch_notion_data(current_user: User = Depends(get_current_user)):
    importer = NotionImporter()
    data = importer.fetch_data(current_user.id)
    return {"data": data}

# Implement similar endpoints for other platforms

