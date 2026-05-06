# Microservices Project (Gold Standard)

This project contains two microservices optimized for production with standardized ports and inter-service discovery.

## Quick Start (Docker Compose)
The recommended way to run the stack. It includes health checks and resource limits.

```bash
docker compose up --build
```

---

## Service Details

### 1. Todo Service
- **External Port**: 8001
- **Internal Port**: 8000
- **Service URL**: http://localhost:8001
- **Discovery**: Accesses Progress Service via `PROGRESS_API_URL`

### 2. Progress Service
- **External Port**: 8002
- **Internal Port**: 8000
- **Service URL**: http://localhost:8002

---

## API Documentation

### Todo Endpoints
- `GET /todos`: List all
- `POST /todos?task=Name`: Create
- `PUT /todos/{id}?completed=true`: Update
- `DELETE /todos/{id}`: Delete

### Progress Endpoints
- `GET /progress`: Current status
- `POST /progress`: Update (Body: `{"percentage": 75.0}`)
