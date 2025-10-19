FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

# Reuse the API requirements to keep environments identical
COPY ./api/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY ./api/app /code/app

RUN mkdir -p /data/uploads
ENV UPLOAD_DIR=/data/uploads

CMD ["celery", "-A", "app.tasks", "worker", "--loglevel=info"]
