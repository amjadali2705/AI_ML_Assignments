# 🚀 Assignment 2: Backend API & Containerization

This assignment focuses on building a functional Python backend using **FastAPI**, managing dependencies for reproducibility, and packaging the entire application using **Docker**.

## 📝 Tasks: 

### 1. Backend API Development
- Developed a RESTful API using **FastAPI** and **Uvicorn**.
- Created a root endpoint (`/`) returning a "Hello World" message.
- Created a data endpoint (`/data`) returning sample JSON metadata.

### 2. Dependency Management
- Generated a `requirements.txt` file to track essential libraries (`fastapi`, `uvicorn`).

### 3. Containerization
- Authored a **Dockerfile** using a lightweight Python base image (`python:3.10-slim`).
- Configured the container to expose port `8000` and run the server on host `0.0.0.0`.

### 4. Version Control (Git)
- Practiced atomic commits for each major step (API setup, Requirements, Dockerfile).

---

## 🛠️ How to Run

### Using Python Locally
```bash
pip install -r requirements.txt
uvicorn app:app
```

### Using Docker
```bash
docker build -t ass2:1.0 .
docker run -d -p 8000:8000 --name assignment2 ass2:1.0
```