# 📊 Real-Time Stock Market Data Engineering Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-black.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C.svg)
![Architecture](https://img.shields.io/badge/Architecture-Event--Driven-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Grade-success.svg)

> A scalable, event-driven, production-grade real-time data engineering platform for ingesting, streaming, processing, storing, and monitoring live stock market data.

---

# 📌 Executive Summary

This platform simulates real-world financial data infrastructure using distributed streaming systems and containerized services.

It demonstrates practical implementation of:

- Real-time event streaming
- Producer–consumer architecture
- Distributed message brokering (Kafka)
- Persistent analytical storage (PostgreSQL)
- Infrastructure monitoring (Prometheus)
- Docker-based service orchestration

The system is engineered with scalability, reliability, and observability as core design principles.

---

# 🏗️ System Architecture

## 📌 Real-Time Pipeline Overview

<p align="center">
  <img src="img/real_time_pipeline.png" alt="Real-Time Stock Market Data Pipeline Architecture" width="950">
</p>

---

## 🔄 Data Flow Explanation

1. **Stock Market API** provides real-time financial data.
2. **Python Producer Service** extracts and publishes structured events.
3. **Apache Kafka** acts as the distributed streaming backbone.
4. **Consumer Service** processes streaming events.
5. **PostgreSQL** persists structured stock data.
6. **Prometheus** monitors Kafka and system metrics.

---

# 🧠 Advanced Architecture Design

## 1️⃣ Event-Driven Architecture

The system follows an event-driven model:

- Producers publish events asynchronously.
- Kafka decouples producers and consumers.
- Consumers independently process data streams.
- Services scale independently without tight coupling.

This architecture improves throughput, resilience, and modularity.

---

## 2️⃣ Scalability Strategy

### 🔹 Horizontal Scaling

- Kafka topics support partition-based scaling.
- Consumers scale via consumer groups.
- Docker enables service replication.
- Database scaling via read replicas.

### 🔹 Vertical Scaling

- Kafka broker memory tuning (JVM configuration).
- PostgreSQL resource optimization.
- Container CPU and memory allocation adjustments.

---

## 3️⃣ Fault Tolerance & Reliability

- Kafka ensures message durability.
- Offset management prevents duplicate processing.
- Docker restart policies improve service resilience.
- Persistent volumes protect stored data.
- System components operate independently to reduce cascading failure risk.

---

## 4️⃣ Observability & Monitoring

Monitoring is integrated at the infrastructure layer:

- Kafka JMX metrics exposed.
- Prometheus scrapes broker metrics.
- Consumer lag tracking.
- JVM memory usage monitoring.
- Throughput and performance visibility.

Observability enables:

- Performance analysis
- Bottleneck detection
- Capacity planning
- Production-readiness validation

---

# 🛠️ Technology Stack

| Layer                  | Technology |
|------------------------|------------|
| Programming Language   | Python |
| Streaming Platform     | Apache Kafka |
| Messaging Pattern      | Producer–Consumer |
| Database               | PostgreSQL |
| Containerization       | Docker |
| Orchestration          | Docker Compose |
| Monitoring             | Prometheus + JMX Exporter |
| Configuration          | Environment Variables (.env) |
| Version Control        | Git |

---

# 📂 Project Structure

```bash
.
├── extract.py
├── producer_setup.py
├── consumer.py
├── main.py
├── config.py
├── Dockerfile
├── compose.yml
├── requirements.txt
├── .env
├── prometheus.yml
├── prom-jmx-agent-config.yml
├── stock_data_logs.log
├── img/
│   └── real_time_pipeline.png
└── README.md
```

---

# ⚙️ Deployment Guide

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd project-directory
```

---

## 2️⃣ Configure Environment Variables

Create `.env` file:

```env
API_KEY=your_stock_api_key
```

---

## 3️⃣ Start Infrastructure

```bash
docker-compose up --build
```

This provisions:

- Zookeeper
- Apache Kafka
- PostgreSQL
- Application Service
- Prometheus Monitoring

---

# 📊 Monitoring Dashboard

Access Prometheus:

```
http://localhost:9090
```

### Key Metrics Monitored

- Broker throughput
- Topic performance
- Consumer lag
- JVM memory usage
- Message production rate

---

# 📈 Core System Capabilities

- Real-time stock data ingestion
- Distributed streaming architecture
- Modular producer-consumer design
- Containerized infrastructure
- Persistent relational storage
- Log-based observability
- Infrastructure-level monitoring

---

# 🔐 Security & Configuration

- API key secured via environment variables
- Sensitive files excluded via `.gitignore`
- Centralized configuration management
- Service isolation via containerization

---

# 🎯 Engineering Competencies Demonstrated

This project reflects hands-on experience in:

- Distributed systems engineering
- Streaming data architecture
- Kafka-based event processing
- Dockerized infrastructure deployment
- Observability engineering
- Production-style system design
- Real-time data persistence workflows

---

# 🚀 Future Enhancements

- Apache Spark Structured Streaming integration
- Schema registry (Avro / Protobuf)
- Dead-letter queue implementation
- Kafka cluster scaling
- Cloud-native deployment (AWS / GCP)
- CI/CD pipeline automation
- Data validation and quality layer

---

# 🏁 Conclusion

This platform represents a production-grade real-time data engineering system built using industry-standard tools and distributed system design principles.

It models financial data streaming infrastructure with emphasis on scalability, reliability, modularity, and observability — reflecting real-world engineering environments.