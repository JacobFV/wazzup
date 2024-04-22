from fastapi import APIRouter, Depends
from core.sampling_and_generation import Sampler, DraftGenerator
from database.models import User, Draft
from api.dependencies import get_current_user

router = APIRouter(prefix="/query-and-submission", tags=["Query and Submission"])

@router.post("/sample-messages")
def sample_messages(current_user: User = Depends(get_current_user)):
    sampler = Sampler()
    messages = sampler.sample_messages(current_user.id)
    return {"messages": messages}

@router.post("/generate-draft")
def generate_draft(current_user: User = Depends(get_current_user)):
    generator = DraftGenerator()
    draft = generator.generate_draft(current_user.id)
    return {"draft": draft}

@router.post("/submit-draft")
def submit_draft(draft: Draft, current_user: User = Depends(get_current_user)):
    # Implement logic to submit the draft to the selected platform
    return {"message": "Draft submitted successfully"}

