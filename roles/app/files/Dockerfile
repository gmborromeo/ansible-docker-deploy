FROM python:3.11-slim
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY app.py .
RUN pip install flask psycopg2-binary
EXPOSE 5000
CMD ["python", "app.py"]
