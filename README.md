# AWS ECS + ECR Container Deployment Lab

## Overview

This project demonstrates end-to-end containerization and deployment of a Python-based web application using Docker and AWS cloud services. The application is built locally, containerized, stored in Amazon ECR, and deployed using ECS Fargate with public network access.

---

## Architecture

```
Local Machine
   ↓
Docker Build (linux/amd64)
   ↓
Amazon ECR (Container Registry)
   ↓
ECS Fargate (Serverless Compute)
   ↓
Public IP (Port 8080)
   ↓
User Access (Browser / curl)
```

---

## Technologies Used

* Python (HTTP server)
* Docker (containerization)
* AWS ECR (image registry)
* AWS ECS Fargate (container orchestration)
* AWS VPC + Security Groups (networking)
* AWS CLI (authentication & deployment)
* Linux CLI tools

---

## Key Features

* Containerized Python web application
* Cross-platform Docker build (ARM → AMD64)
* Deployment to AWS without managing EC2 instances
* Public access via ECS networking configuration
* Secure image storage in ECR

---

## Technical Challenges & Solutions

### 1. Architecture Mismatch (ARM vs AMD64)

**Issue:**
ECS failed to pull image due to platform mismatch.

**Fix:**
Used Docker Buildx to build image for correct platform:

```bash
docker buildx build --platform linux/amd64 ...
```

---

### 2. Image Digest Locking

**Issue:**
ECS task definition referenced a fixed image digest.

**Fix:**
Replaced digest with dynamic tag (`v2`) and created new task revision.

---

### 3. AWS Authentication Failure

**Issue:**
Invalid security token when logging into ECR.

**Fix:**
Configured AWS CLI:

```bash
aws configure
```

---

### 4. Network Access Failure

**Issue:**
Application not reachable via browser.

**Fix:**
Updated security group to allow inbound traffic:

* Port: 8080
* Source: 0.0.0.0/0

---

## How to Run Locally

```bash
docker build -t myapp .
docker run -p 8080:8080 myapp
```

---

## Deployment Steps

1. Authenticate AWS CLI
2. Build Docker image (amd64)
3. Push image to ECR
4. Create ECS Task Definition
5. Run ECS task using Fargate
6. Configure networking and security group
7. Access via public IP

---

## Key Learnings

* Container lifecycle from local to cloud
* Differences between ARM and AMD64 architectures
* ECS task definitions vs Docker runtime
* Cloud networking fundamentals (VPC, public IP, security groups)
* Debugging real-world deployment issues

---

## Author

Daniel Apuzzio
Cloud Engineer | AWS | Linux | DevOps

```bash
docker build -t myapp .
docker run -p 8080:8080 myapp
