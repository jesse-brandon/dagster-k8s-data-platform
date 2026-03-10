# Dagster Kubernetes Data Platform

A modern **data pipeline orchestration platform** built with:

* **Dagster**
* **Docker**
* **PostgreSQL**
* **Kubernetes** (planned)
* **Terraform** (planned)

This project demonstrates how to build a **production-ready data orchestration environment** using Dagster with containerized infrastructure.

---

# Architecture

The platform separates **orchestration**, **execution**, and **metadata storage**.

```
Dagster Webserver (UI)
│
├── Dagster Daemon
│   ├── Schedules
│   ├── Sensors
│   └── Run coordination
│
├── Postgres Metadata Database
│   ├── Pipeline runs
│   ├── Event logs
│   └── Schedule state
│
└── User Code Repository
    ├── Assets
    ├── Jobs
    └── Resources
```

Future production architecture:

```
Dagster UI
   │
   ▼
Dagster Daemon
   │
   ▼
Kubernetes Job Launcher
   │
   ▼
Pipeline Containers
   │
   ▼
Data Warehouse / Data Lake
```

---

# Repository Structure

```
dagster-kubernetes-data-platform
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
├── pipelines/
│   ├── __init__.py
│   ├── assets.py
│   ├── jobs.py
│   └── resources.py
│
├── dagster_workspace/
│   └── workspace.yaml
│
├── dagster_home/
│   └── dagster.yaml
│
├── k8s/
│   └── (future Kubernetes manifests)
│
└── README.md
```

---

# Features

Current capabilities:

* Dagster orchestration platform
* Containerized development environment
* PostgreSQL metadata storage
* Dagster daemon for background services
* Asset-based pipelines

Planned enhancements:

* Kubernetes job execution
* Cloud storage integration (S3 / GCS)
* Terraform infrastructure
* Data warehouse integration
* Observability and pipeline monitoring

---

# Running the Platform

Start the platform locally with Docker:

```
docker compose up --build
```

Dagster UI will be available at:

```
http://localhost:3000
```

---

# Example Pipeline

Current example pipeline:

```
raw_data → transformed_data
```

Example asset:

```python
from dagster import asset
import pandas as pd

@asset
def raw_data():
    data = {
        "id": [1, 2, 3],
        "value": [10, 20, 30]
    }
    return pd.DataFrame(data)

@asset
def transformed_data(raw_data):
    raw_data["value_x2"] = raw_data["value"] * 2
    return raw_data
```

Dagster assets allow:

* **data lineage tracking**
* **dependency management**
* **observable pipelines**

---

# Why Dagster

Dagster provides modern orchestration features:

* Asset-based pipeline modeling
* Data lineage tracking
* Observability
* Scalable execution
* Strong Python integration

Compared to traditional orchestration tools like **Airflow**, Dagster focuses on **data asset management rather than task scheduling**.

---

# Roadmap

Next platform improvements:

* Kubernetes run launcher
* Distributed pipeline execution
* Terraform infrastructure provisioning
* Warehouse ingestion pipelines
* ML workflow orchestration

---

# Author

**Jesse Brandon**

Senior SQL Developer → Data Engineering

This repository is part of a broader **data engineering portfolio platform** exploring:

* modern data platform architecture
* infrastructure automation
* AI-assisted data workflows
