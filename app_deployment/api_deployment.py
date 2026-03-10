from fastapi import APIRouter

api_code_deployment = APIRouter()
@api_code_deployment.post("/azure-cloud/kubernetes/api-code-deployment")
def deployed_function1():
    return {"message": "Hello From Azure Kubernetes"}
