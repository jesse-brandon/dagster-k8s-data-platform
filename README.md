# Dagster Kubernetes Data Platform

A lightweight data engineering platform demonstrating **Dagster asset-based orchestration**, **containerized pipelines**, and **PostgreSQL warehouse persistence**.

This project showcases modern data engineering concepts including asset lineage, ETL layering, and containerized orchestration.

---

# Architecture

```
CSV Data Source
      │
      ▼
Dagster Asset Pipeline
      │
      ▼
Bronze Layer (Raw Structured Data)
      │
      ▼
Silver Layer (Cleaned & Typed Data)
      │
      ▼
Analytics Layer (Aggregated Metrics)
      │
      ▼
PostgreSQL Data Warehouse
```

Platform components:

```
Dagster Webserver
Dagster Daemon
PostgreSQL Run/Event Storage
PostgreSQL Warehouse Tables
Docker Compose Development Environment
```

---

# Asset Pipeline

The project implements a simple layered warehouse pipeline:

| Layer     | Description                   |
| --------- | ----------------------------- |
| Raw       | Ingest CSV data               |
| Bronze    | Minimal schema cleanup        |
| Silver    | Data normalization and typing |
| Analytics | Aggregated business metrics   |

Asset lineage:

```
raw_sales_data
      │
      ▼
bronze_sales
      │
      ▼
silver_sales
      │
      ▼
sales_summary
```

Dagster automatically manages dependency ordering and execution.

---

# Repository Structure

```
dagster-k8s-data-platform
│
├── pipelines/
│   ├── assets.py
│   ├── resources.py
│   └── io_managers/
│
├── dagster_home/
│   └── dagster.yaml
│
├── dagster_workspace/
│   └── workspace.yaml
│
├── data/
│   └── sample_sales.csv
│
├── docker-compose.yml
└── README.md
```

---

# Running the Platform

Start the platform:

```
docker compose up --build
```

Open Dagster UI:

```
http://localhost:3000
```

Materialize assets to run the pipeline.

---

# Verifying Data in Postgres

Connect to the warehouse:

```
docker compose exec postgres psql -U dagster
```

List tables:

```
\dt
```

Expected tables:

```
raw_sales_data
bronze_sales
silver_sales
sales_summary
```

---

# Key Concepts Demonstrated

* Dagster asset-based orchestration
* Data lineage visualization
* Layered warehouse modeling (bronze / silver / analytics)
* Containerized development environment
* PostgreSQL warehouse persistence
* Modular pipeline architecture

---

# Future Enhancements

Potential extensions:

* Kubernetes job execution
* S3 / object storage ingestion
* Terraform infrastructure provisioning
* dbt warehouse transformations
* streaming ingestion pipelines

---

# Purpose

This repository is part of a personal **data engineering learning platform** used to explore modern orchestration and data platform patterns.
