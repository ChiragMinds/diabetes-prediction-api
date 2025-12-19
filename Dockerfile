# Use python 3.14 base image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy paste the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Command to start fastapi application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]