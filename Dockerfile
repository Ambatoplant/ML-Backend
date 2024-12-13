# Gunakan base image Python 3.10 slim
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Salin requirements dan install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi
COPY . .

# Ekspos port Flask default
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "app.py"]