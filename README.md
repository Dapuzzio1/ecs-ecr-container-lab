# Multi-App Docker + NGINX Lab

## Overview
This project demonstrates running multiple Python applications inside a single Docker container and routing traffic using NGINX as a reverse proxy.

## Architecture

Client (Browser / curl)
        ↓
     NGINX (Port 80)
      /        \
 app.py      app2.py
(8080)       (9090)

## Technologies Used
- Python
- Docker
- Linux CLI
- NGINX

## Features
- Runs two apps inside one container
- NGINX routes traffic between services
- Demonstrates reverse proxy behavior
- Uses multiple ports inside a container

## Key Learnings
- Running multiple processes in Linux
- Background vs foreground execution
- NGINX reverse proxy configuration
- Container networking and port mapping

## How to Run Locally

```bash
docker build -t multiapp .
docker run -p 8081:80 myapp

## Test

```bash
curl localhost:8081
curl localhost:8081/app2

Author
Daniel Apuzzio Cloud Engineer | AWS | Linux
