FROM public.ecr.aws/lambda/python:3.9

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code to the root (NOT /app)
COPY ./app/main.py .

COPY ./app /app

# Set the handler for Lambda
CMD ["main.lambda_handler"]
