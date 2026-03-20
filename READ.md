# ECS + ECR Container Deployment (AWS)

## Overview
This project demonstrates how to containerize a Python application using Docker and deploy it to AWS using ECR and ECS Fargate.

## Architecture
Local App → Docker → ECR → ECS Fargate → Public Endpoint

## Technologies Used
- Python
- Docker
- AWS ECR
- AWS ECS (Fargate)
- Linux CLI

## Features
- Containerized Python web server
- Deployed to AWS without managing servers
- Publicly accessible via ECS networking

## Key Learnings
- Docker image creation and tagging
- AWS authentication via CLI
- ECR image push and storage
- ECS task definitions and container orchestration
- Debugging platform mismatches (ARM vs AMD64)
- Cloud networking and security groups

## How to Run Locally

```bash
docker build -t myapp .
docker run -p 8080:8080 myapp
