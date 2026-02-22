🚀 Cloud Native Monitoring Application using Jenkins & Kubernetes
📌 Project Overview

This project demonstrates a complete CI/CD pipeline for deploying a Cloud Native Monitoring Application using:

Docker for containerization

Kubernetes (Minikube) for orchestration

Jenkins for CI/CD automation

AWS EC2 as deployment server

AWS Cost Explorer for daily cost monitoring

⚙️ Pre-Requisites

Before running this project, make sure the following tools are installed and configured on your EC2 instance:

-Jenkins

-Docker

-Kubernetes

-Minikube

-kubectl

🔁 CI/CD Pipeline Flow
    GitHub Push
        ↓
    Jenkins Build Triggered
        ↓
    Old Docker Container Stopped
        ↓
    Old Container Removed
        ↓
    New Docker Image Built
        ↓
    New Container Created
        ↓
    Kubernetes Deployment Updated
        ↓
    New Pod Created
        ↓
    Application Updated Automatically


📦 Create Jenkins Job

    Create:

    New Item → Freestyle Project
    Name → cloud-monitoring

    Add GitHub Repository:

    https://github.com/<your-username>/<repo-name>.git

🛠️ Jenkins Build Steps Used

    docker stop cloud-native
    docker rm cloud-native
    docker build -t cloud-native .
    docker run --name cloud-native -d -p 5000:5000 cloud-native
    kubectl apply -f deployment.yaml


☸️ Kubernetes Deployment

Application is deployed using Kubernetes Deployment

Rolling Update strategy is used to avoid downtime

Kubernetes Service exposes the application externally using NodePort

💰 AWS Cost Automation
    Create IAM Role

    Go to:
    IAM → Roles → Create Role → EC2

    Attach Policy:
    BillingReadOnlyAccess

    Attach Role to EC2 Instance.

📧 Store Email Credentials Securely
    nano ~/.bashrc

    Add:

    export EMAIL_USER="your_email@gmail.com"
    export EMAIL_PASS="your_app_password"

    Apply:

    source ~/.bashrc

⏰ Setup Daily Cron Job
    crontab -e

    Add:

    0 9 * * * EMAIL_USER="your_email@gmail.com" EMAIL_PASS="your_app_password" /usr/bin/python3 /home/ubuntu/cloud-monitoring-app-email/cost_report.py

    Verify:

    crontab -l

🌐  Access Application

    Check Service:

    kubectl get svc -n gajendra

    Open in Browser:

    http://<EC2-PUBLIC-IP>:<NODEPORT>



🎯 Final Output

    Monitoring Application deployed on Kubernetes

    CI/CD Pipeline Automated using Jenkins

    Docker Image built automatically

    Rolling Deployment enabled

    Daily AWS Cost Email Automation

    Secure IAM Role based AWS access


🧠 DevOps Concepts Implemented

    CI/CD Pipeline

    Containerization

    Kubernetes Deployment

    Rolling Updates

    IAM Role Based Access

    Cron Job Scheduling

    Secure Environment Variables


✅ Conclusion

This project demonstrates an end-to-end DevOps implementation of deploying a cloud-native monitoring application on Kubernetes with automated CI/CD and cost monitoring using AWS services.