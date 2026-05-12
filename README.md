# Cold Storage API
Cold Storage is a distributed backend system designed to simulate real‑world warehouse operations including inventory tracking, shipment workflows, and temperature‑controlled storage.
It mirrors enterprise architecture patterns such as microservices, service boundaries, and legacy‑to‑modern authentication transitions.

This project is part of a four‑system engineering portfolio demonstrating:

- Backend engineering
- Distributed testing
- CI/CD automation
- Identity migration patterns
- Systems debugging

---
## 🚀 Architecture Overview
Cold Storage is built as a modular FastAPI service with multiple domains:

- **Inventory Service**  
Tracks items, quantities, and storage locations.

- **Shipment Service**
Simulates shipment creation, retrieval, and status tracking.

- **Temperature Service**
Mock temperature sensor API with threshold alerts.

- **Storage Zones**
Logical partitions representing cold rooms, freezers, and controlled environments.

-**Authentication Layer (Pluggable)**
Supports two modes:

- LEGACY — simulated session‑based auth
- TOKEN — JWT‑based modern auth

This models real enterprise identity migrations where both systems must coexist.
  
---

## 🎯 Project Goals
- Demonstrate realistic backend service design
- Provide a platform for unit, integration, and contract testing
- Showcase CI/CD pipelines using Jenkins
- Support future expansion into event‑driven flows
- Serve as a foundation for distributed systems practice

---

## 🧰 Tech Stack
- **Python 3.11**
- **FastAPI + Uvicorn**
- **PyTest**
- **Docker + Docker Compose**
- **Jenkins (Pipeline)**
- **PostgreSQL (future extension)**

---

## 📁 Project Structure
warehouse_api/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── inventory.py
│   │   ├── shipment.py
│   │   └── __init__.py
│   └── models/
│
├── temperature_service/
│   ├── app.py
│   └── requirements.txt
│
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
└── tests/

## 🧪 Running Tests
- **Unit Tests**

pytest -q

- **Integration Tests (Docker)**

docker compose up --build -d
pytest tests/integration
docker compose down

## 🐳 Running the Services
docker compose up --build

Services:

http://localhost:8000 → warehouse_api

http://localhost:8001 → temperature_service

## 🔧 Jenkins CI/CD Pipeline
The Jenkinsfile performs:
1. SCM checkout
2. Python venv setup
3. Install dependencies
4. Run unit tests
5. Build Docker images
6. Spin up integration environment
7. Run integration tests
8. Archive test results












