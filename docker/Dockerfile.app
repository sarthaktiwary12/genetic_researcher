FROM python:3.12-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY agents/ agents/
COPY platform/ platform/
COPY crops/ crops/
COPY knowledge_base/ knowledge_base/
COPY targets_config.json .

# Create data directories
RUN mkdir -p data/chromadb

EXPOSE 8000

CMD ["uvicorn", "platform.app:app", "--host", "0.0.0.0", "--port", "8000"]
