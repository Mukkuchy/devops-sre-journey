# DevOps/SRE Journey

This repository tracks my 30-day transition from Senior QA Engineer to DevOps/SRE candidate.

## Project

A simple REST API built with Python's standard library (`http.server`). No external dependencies.

## Day 1 Progress

- Initialized project structure
- Created a basic REST API with `/health` and `/api/v1/message` endpoints
- Practiced Linux basics: file inspection, process management, system resources, network checks
- Created sample logs and troubleshooting notes

## How to Run the App

```bash
python3 app.py

curl http://localhost:5000/health
curl http://localhost:5000/api/v1/message
