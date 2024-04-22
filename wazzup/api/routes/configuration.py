from fastapi import APIRouter, Depends
from database.models import User, SamplingConfig, GenerationConfig
from api.dependencies import get_current_user

router = APIRouter(prefix="/configuration", tags=["Configuration"])

@router.get("/sampling-config")
def get_sampling_config(current_user: User = Depends(get_current_user)):
    # Retrieve the sampling configuration for the current user
    return {"sampling_config": current_user.sampling_config}

@router.put("/sampling-config")
def update_sampling_config(config: SamplingConfig, current_user: User = Depends(get_current_user)):
    # Update the sampling configuration for the current user
    return {"message": "Sampling configuration updated successfully"}

@router.get("/generation-config")
def get_generation_config(current_user: User = Depends(get_current_user)):
    # Retrieve the generation configuration for the current user
    return {"generation_config": current_user.generation_config}

@router.put("/generation-config")
def update_generation_config(config: GenerationConfig, current_user: User = Depends(get_current_user)):
    # Update the generation configuration for the current user
    return {"message": "Generation configuration updated successfully"}

