FROM python:3.15.0a5-slim

WORKDIR /app

COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "backend.app:app"]
