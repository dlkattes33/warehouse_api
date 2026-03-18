# Cold Storage API

Cold Storage is a distributed backend service designed to simulate real-world
inventory, temperature monitoring, and storage operations. The project is built
to mirror the architecture patterns found in large-scale enterprise systems,
including legacy-to-modern authentication transitions, service boundaries, and
API-driven workflows.

This project is part of a four-system portfolio demonstrating backend
engineering, distributed testing, identity migration patterns, and systems
debugging.

---

## Architecture Overview

Cold Storage is structured as a modular FastAPI service with the following components:

- **Inventory Service**  
  Tracks items, quantities, and storage locations.

- **Temperature Service**  
  Simulates temperature readings and threshold alerts.

- **Storage Zones**  
  Logical partitions representing cold rooms, freezers, and controlled areas.

- **Auth Layer (Pluggable)**  
  Supports two modes:
  - `LEGACY` — session-based authentication (simulated)
  - `TOKEN` — JWT-based authentication (modern)

This mirrors real enterprise migrations where applications must support both
legacy and modern identity systems during phased cutovers.

---

## Project Goals

- Model a realistic backend service with multiple domains.
- Provide a platform for API testing, integration testing, and contract testing.
- Demonstrate how applications adapt during identity migrations.
- Serve as a foundation for CI/CD pipelines (Jenkins, GitHub Actions).
- Support future expansion into distributed systems and event-driven flows.

---

## Tech Stack

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **PyTest**
- **Playwright (API mode)**
- **Docker**
- **PostgreSQL (optional future extension)**

---

## Running the Service

### Local (without Docker)
