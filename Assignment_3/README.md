# Kubernetes Assignment

## Overview

This project demonstrates deployment and management of a full-stack application.

The project includes:

- Python backend
- Frontend UI with two versions
- Docker image versioning
- Pod creation
- ReplicaSet scaling
- Deployment with rolling updates
- Service exposure
- Health monitoring using probes

---

# Project Structure

```txt
k8s-assignment/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend-v1/
│   ├── index.html
│   └── Dockerfile
│
├── frontend-v2/
│   ├── index.html
│   └── Dockerfile
│
├── k8s/
│   ├── pod.yml
│   ├── rs.yml
│   ├── deployment.yml
│   ├── service.yml
│   ├── backend-deployment.yml
│   └── backend-service.yml
│
└── README.md
```


---

# Backend Setup

Go to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend URLs:

Home:

```txt
http://localhost:8000
```

Swagger:

```txt
http://localhost:8000/docs
```

Health:

```txt
http://localhost:8000/health
```

---

# Frontend Setup

## Version 1

```bash
cd frontend-v1
python -m http.server 8080
```

Open:

```txt
http://localhost:8080
```

---

## Version 2

```bash
cd frontend-v2
python -m http.server 8080
```

Open:

```txt
http://localhost:8080
```

---

# Docker Image Creation

## Backend

```bash
cd backend
docker build -t backend:v1 .
```

## Frontend v1

```bash
cd frontend-v1
docker build -t frontend:v1 .
```

## Frontend v2

```bash
cd frontend-v2
docker build -t frontend:v2 .
```

Verify:

```bash
docker images
```

---

# Minikube Setup

Start cluster:

```bash
minikube start
```

Use Minikube Docker:

### PowerShell

```powershell
minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

---

# Kubernetes Deployment

Go to k8s folder:

```bash
cd k8s
```

---

# Pod

Create pod:

```bash
kubectl apply -f pod.yml
```

Check:

```bash
kubectl get pods
```

---

# ReplicaSet

Create ReplicaSet:

```bash
kubectl apply -f rs.yml
```

Check:

```bash
kubectl get rs
kubectl get pods
```

---

Deploy:

```bash
kubectl apply -f deployment.yml
```

Deploy frontend service:

```bash
kubectl apply -f service.yml
```

Check:

```bash
kubectl get deployments
kubectl get svc
```

---

# Access Application

Run:

```bash
minikube service frontend-service
```

Browser opens automatically.

---

# Probes

The deployment includes:

- Liveness Probe
- Readiness Probe
- Startup Probe

Verify:

```bash
kubectl describe pod <pod-name>
```

---

# Rolling Update

Update frontend from v1 to v2:

```bash
kubectl set image deployment/frontend-deployment frontend=frontend:v2
```

Watch rollout:

```bash
kubectl get pods -w
```

Verify:

```bash
kubectl get pods
```

Browser should now display:

```txt
Version 2
```

---

# Useful Commands

View pods:

```bash
kubectl get pods
```

View services:

```bash
kubectl get svc
```

View ReplicaSets:

```bash
kubectl get rs
```

View deployments:

```bash
kubectl get deployments
```

Describe pod:

```bash
kubectl describe pod <pod-name>
```

Delete all resources:

```bash
kubectl delete -f .
```


---

# Author

Md Amjad Ali