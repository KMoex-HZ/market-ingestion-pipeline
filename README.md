# 📈 Automated Crypto Market ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.0+-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-336791.svg)

A production-ready, containerized **Extract, Transform, Load (ETL)** pipeline designed to ingest real-time cryptocurrency market data into a centralized PostgreSQL data warehouse.

This project demonstrates **Data Engineering best practices** including modular architecture, container orchestration, and automated scheduling.

---

## 🏗️ System Architecture

The pipeline follows a modern data engineering workflow:

1.  **Extract:** Python script fetches real-time data from the **CoinGecko API**.
2.  **Transform:** Data is cleaned, formatted, and validated using **Pandas**.
3.  **Load:** Processed data is ingested into a **PostgreSQL** database.
4.  **Orchestrate:** Entire workflow is scheduled and monitored via **Apache Airflow**.

---

## 🚀 Key Engineering Features

- **Dockerized Environment:** Fully containerized setup using Docker Compose, ensuring the pipeline runs identically on any machine (eliminating "it works on my machine" issues).
- **Modular Codebase:** Separation of concerns with dedicated modules for Extraction (`src/extract.py`) and Loading (`src/load.py`), making the code maintainable and testable.
- **Automated Orchestration:** Uses Apache Airflow DAGs for reliable hourly scheduling and failure retries.
- **Secure Configuration:** Database credentials and sensitive keys are managed via environment variables (`.env`), following security best practices.

---

## 📁 Repository Structure

```text
market-ingestion-pipeline/
├── dags/                   # Airflow DAG definitions
│   └── crypto_ingestion_dag.py
├── src/                    # Modular Source Code (ETL Logic)
│   ├── extract.py          # API Extraction logic
│   ├── load.py             # Database Loading logic
│   └── utils.py            # DB Connection & Helper functions
├── docker-compose.yml      # Container Orchestration
├── requirements.txt        # Python Dependencies
└── .env.example            # Environment Variables Template

```

---

## 🛠️ Quick Start Guide

Follow these steps to deploy the pipeline locally:

### 1. Clone the Repository

```bash
git clone [https://github.com/yourusername/market-ingestion-pipeline.git](https://github.com/yourusername/market-ingestion-pipeline.git)
cd market-ingestion-pipeline

```

### 2. Configure Environment

Create a `.env` file based on the example and configure your database credentials.

```bash
cp .env.example .env
# Edit .env with your specific configurations

```

### 3. Build and Run Containers

Launch the Airflow and PostgreSQL services in detached mode.

```bash
docker-compose up -d --build

```

### 4. Access the Dashboard

- **Airflow UI:** Navigate to `http://localhost:8080`
- **Credentials:** `admin` / `admin` (or as configured in your docker-compose)
- Enable the DAG `crypto_market_ingestion_pro_v1` to start the pipeline.

---

## 🔮 Future Improvements

- **Data Visualization:** Integrate Metabase or Superset for real-time dashboarding.
- **Data Quality Checks:** Implement Great Expectations for rigorous schema validation.
- **CI/CD:** Add GitHub Actions for automated testing and deployment.

---

## 🛡️ License

Distributed under the MIT License. See `LICENSE` for more information.
