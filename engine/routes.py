from fastapi import APIRouter
from models import Pipeline
from db import pipelines_collection


router = APIRouter()


@router.post("/pipelines")
def create_pipeline(pipeline: Pipeline):
    result = pipelines_collection.insert_one(pipeline.dict())
    return {"pipeline_id": str(result.inserted_id)}


@router.get("/pipelines")
def get_pipelines():
    pipelines = list(pipelines_collection.find())
    return pipelines


@router.post("/webhook")
def receive_webhook(payload: dict):
    # Process webhook (trigger pipeline based on repo/branch)
    # Example: You could update pipeline status here
    return {"message": "Webhook received"}
