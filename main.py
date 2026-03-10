from fastapi import FastAPI
from app_deployment.api_deployment import api_code_deployment

app = FastAPI()
app.include_router(api_code_deployment)