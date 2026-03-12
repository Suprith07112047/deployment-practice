from fastapi import APIRouter

api_code_deployment = APIRouter()
@api_code_deployment.post("/aws-cloud/ec2/api-code-deployment")
def deployed_function1():
    return {"message": "Hello From AWS Cloud EC2 API Code Deployment!"}


# Basic GET endpoint
@api_code_deployment.get("/ping")
def ping():
    return {"message": "Hello Jai Shree Ram! This is a simple GET endpoint."}

# Health check endpoint
@api_code_deployment.get("/health")
def health_check():
    return {"status": "ok", "service": "EC2 deployment"}

# Static info endpoint
@api_code_deployment.get("/info")
def info():
    return {"app": "deployment-practice", "version": "1.0.0"}

# Simple DELETE endpoint
@api_code_deployment.delete("/remove")
def remove():
    return {"message": "delete operation simulated"}

