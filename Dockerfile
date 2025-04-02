# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies required for cryptography
RUN apt-get update && apt-get install -y libssl-dev libffi-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --upgrade cryptography mysql-connector-python pymysql \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port and start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
