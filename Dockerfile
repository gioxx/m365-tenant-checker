FROM python:3.13-slim

WORKDIR /app

# Copy backend and frontend
COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

# Install requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["gunicorn", "backend.app:app"]
