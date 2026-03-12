from fastapi import APIRouter

api_code_deployment = APIRouter()
@api_code_deployment.post("/aws-cloud/ec2/api-code-deployment")
def deployed_function1():
    return {"message": "Hello From AWS Cloud EC2 API Code Deployment!"}
