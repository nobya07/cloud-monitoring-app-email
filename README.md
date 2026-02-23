# ☁️ Cloud Monitoring App

A Flask-based cloud monitoring dashboard that displays real-time CPU, memory, disk usage, Kubernetes pod/node status, and sends daily AWS cost reports via email.

---

## 📁 Project Structure

```
cloud-monitoring-app/
│
├── app.py                  # Flask application
├── cost_report.py          # AWS cost email script
├── Dockerfile              # Docker image setup
├── requirements.txt        # Python dependencies
├── deployment.yaml         # Kubernetes deployment and service
├── Jenkinsfile             # CI/CD pipeline
└── templates/
    └── index.html          # Dashboard UI
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python + Flask | Web application |
| Docker | Containerization |
| Kubernetes (Minikube) | Container orchestration |
| Jenkins | CI/CD pipeline |
| AWS Cost Explorer | Daily cost reporting |
| Gmail SMTP | Email notifications |
| EC2 | Cloud hosting |

---

## ⚙️ Prerequisites

- AWS EC2 instance (Ubuntu)
- Docker installed
- Minikube installed
- kubectl installed
- Jenkins installed
- DockerHub account
- Gmail account with App Password

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nobya07/cloud-monitoring-app-email.git
cd cloud-monitoring-app-email
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

```bash
sudo nano /etc/environment

# Add these lines
EMAIL_USER="your@gmail.com"
EMAIL_PASS="your_16_digit_app_password"

# Save and reload
source /etc/environment
```

### 4. Build and Run with Docker

```bash
docker build -t gajendra1/cloud-native:latest .

docker run --name cloud-native -d -p 5000:5000 \
  -v ~/.kube/config:/root/.kube/config \
  -e EMAIL_USER=$EMAIL_USER \
  -e EMAIL_PASS=$EMAIL_PASS \
  gajendra1/cloud-native:latest
```

### 5. Deploy to Kubernetes

```bash
kubectl create namespace gajendra
kubectl apply -f deployment.yaml
kubectl get pods -n gajendra
kubectl get service -n gajendra
```

---

## 🌐 Access the App

| Method | URL |
|--------|-----|
| Docker | `http://<EC2-PUBLIC-IP>:5000` |
| Kubernetes | `http://<EC2-PUBLIC-IP>:30500` |

---

## 📧 AWS Cost Report

The `cost_report.py` script fetches yesterday's AWS cost and sends it via email every day at 9 AM.

### Setup Cron Job

```bash
crontab -e

# Add this line
0 9 * * * EMAIL_USER="your@gmail.com" EMAIL_PASS="yourpassword" /usr/bin/python3 /home/ubuntu/cost_report.py >> /var/log/cost_report.log 2>&1
```

### Check Logs

```bash
cat /var/log/cost_report.log
```

---

## 🔧 Jenkins CI/CD Pipeline

### Jenkins Credentials Required

| ID | Type | Value |
|----|------|-------|
| `docker-creds` | Username with password | DockerHub username + password |
| `email-creds` | Username with password | Gmail address + App password |

### Pipeline Stages

```
Cleanup → Build → Push to DockerHub → Run Container → Deploy to Kubernetes → Verify
```

### Setup Steps

```
1. Jenkins → New Item → Pipeline
2. Configure → Pipeline → Pipeline script from SCM
3. SCM → Git → enter your GitHub repo URL
4. Branch → main
5. Script Path → Jenkinsfile
6. Build Triggers → Poll SCM → H/5 * * * *
7. Save
```

---

## 🔒 EC2 Security Group Rules

| Port | Purpose |
|------|---------|
| 22 | SSH |
| 8080 | Jenkins |
| 5000 | Docker app |
| 30500 | Kubernetes app |

---

## 📊 Dashboard Features

- CPU Usage gauge
- Memory Usage gauge
- Disk Usage gauge
- Pod Status
- Restart Count
- Node Status
- System Uptime
- Network Sent / Received

---

## 📝 Gmail App Password Setup

```
Google Account → Security
→ 2-Step Verification → App Passwords
→ Select app: Mail
→ Select device: Other → name it "AWS Report"
→ Copy the 16-character password
```

---

## 👤 Author

**Gajendra Punekar**
GitHub: [@nobya07](https://github.com/nobya07)