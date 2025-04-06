from fastapi import FastAPI
from mangum import Mangum

load_dotenv()

app = FastAPI()

# FastAPI endpoint for testing Lambda
@app.get("/test-lambda")
def test_lambda():
    return {"message": "This is to test Lambda."}

@app.get("/get-lambda-report")
def get_report(applicationId: str = None):
    if applicationId:
        return {"message": f"Report for Application ID: {applicationId}"}
    return {"message": "No Application ID provided"}

# Mangum handler for AWS Lambda
lambda_handler = Mangum(app)
