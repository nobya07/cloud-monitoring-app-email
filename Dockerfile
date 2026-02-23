FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Install uptime (procps) and kubectl
RUN apt-get update && apt-get install -y \
    procps \
    curl \
    && curl -LO "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/kubectl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

CMD ["python", "app.py"]