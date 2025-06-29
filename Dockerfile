# Dockerfile at project root
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY models/ models/
COPY data/ data/

EXPOSE 8501

CMD ["streamlit", "run", "app/credit_scoring_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
