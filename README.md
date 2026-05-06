# Microservices Project

This project contains two microservices created using `uv`.

## 1. Todo Service
An in-memory todo list manager.

### Run
```bash
cd todo-service
uv run main.py
```
Runs on: http://localhost:8001

### Endpoints
- `GET /todos`: Get all todos.
- `POST /todos?task=Buy+Milk`: Create a new todo.
- `PUT /todos/1?completed=true`: Update todo status.
- `DELETE /todos/1`: Delete a todo.

---

## 2. Progress Service
Tracks project/task progress.

### Run
```bash
cd progress-service
uv run main.py
```
Runs on: http://localhost:8002

### Endpoints
- `GET /progress`: Get current progress.
- `POST /progress`: Update progress (Body: `{"percentage": 75.0}`).
