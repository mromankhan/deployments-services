# Project Instructions (GEMINI.md)

## Role
You are a **Senior Software Engineer** expert in:
- **Python & FastAPI**: For building high-performance backend microservices.
- **Docker**: For containerization and environment consistency.
- **Kubernetes (K8s)**: For orchestration, managing pods, services, and deployments.
- **Microservices Architecture**: Designing scalable, resilient, and decoupled systems.

## Project Overview
This project is dedicated to the deployment and development of backend microservices. The focus is on leveraging Python (FastAPI) for service logic, Docker for packaging, and Kubernetes for production-grade orchestration.

## Building and Running

### Local Development (FastAPI)
- **Install Dependencies**: `pip install -r requirements.txt` (TODO: Ensure file exists)
- **Run Service**: `uvicorn main:app --reload` (TODO: Ensure entry point exists)

### Containerization (Docker)
- **Build Image**: `docker build -t <service-name> .`
- **Run Container**: `docker run -p 8000:8000 <service-name>`

### Orchestration (Kubernetes)
- **Apply Manifests**: `kubectl apply -f k8s/`
- **Check Pods**: `kubectl get pods`

## Development Conventions

### Coding Standards
- Follow **PEP 8** for Python code.
- Use **Type Hints** extensively for FastAPI models and function signatures.
- Implement **Pydantic** models for request/response validation.

### Testing
- Use **Pytest** for unit and integration tests.
- Maintain high test coverage for core business logic.

### Deployment
- Ensure all microservices include a `Dockerfile`.
- Kubernetes manifests should be stored in the `k8s/` directory.
- Use environment variables for configuration (Secret/ConfigMap).
