# 🚀 Real-Time Stock Market Data Pipeline

A fully containerized real-time data engineering pipeline built using:

- 🐍 Python  
- 📨 Apache Kafka  
- ⚡ PySpark  
- 🐘 PostgreSQL  
- 🐳 Docker & Docker Compose  
- 📊 Power BI (Visualization – Planned)  

---

## 📌 Project Overview

This project implements an end-to-end real-time stock market data pipeline.

The system ingests stock data from the Alpha Vantage API, streams it through Kafka, processes it with Spark, and stores it in PostgreSQL for visualization.

---

## 🏗️ Architecture

```
Alpha Vantage API
        ↓
   Python Producer
        ↓
      Kafka
        ↓
      Spark
        ↓
   PostgreSQL
        ↓
     Power BI
```

All services are orchestrated using Docker Compose.

---

## 🐳 Dockerized Services

| Service        | Image Used                        | Port |
|---------------|-----------------------------------|------|
| Kafka         | confluentinc/cp-kafka:7.4.10      | 9092 |
| Spark Master  | spark:3.5.1-python3               | 7077 |
| Spark Worker  | spark:3.5.1-python3               | —    |
| PostgreSQL    | debezium/postgres:17              | 5434 |
| pgAdmin       | dpage/pgadmin4:9                  | 5050 |
| Kafka UI      | provectuslabs/kafka-ui:v0.7.2     | 8085 |
| Producer      | Custom Docker image               | —    |

---

## 🔗 Access Services (Local Development)

Once containers are running:

| Service         | URL |
|----------------|-----|
| Kafka UI        | http://localhost:8085 |
| pgAdmin         | http://localhost:5050 |
| Spark Master UI | http://localhost:8081 |
| Kafka Broker    | localhost:9092 |

⚠️ These URLs are for local development only.  
They do not expose sensitive data and are safe to include in documentation.

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
API_KEY=your_alpha_vantage_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

⚠️ `.env` is excluded via `.gitignore` and must never be committed.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Real-Time-Stock-Market-Analyses.git
cd Real-Time-Stock-Market-Analyses
```

### 2️⃣ Build and start services

```bash
docker compose up -d --build
```

### 3️⃣ Verify containers

```bash
docker ps
```

### 4️⃣ View logs (example)

```bash
docker logs consumer
```

---

## 🔄 Producer Behavior

The producer:

- Fetches TSLA, MSFT, and GOOGL stock data  
- Runs continuously in a loop  
- Respects Alpha Vantage free tier limits  
- Handles API errors and rate limits gracefully  
- Sleeps between cycles to prevent throttling  

Example log output:

```
INFO - Starting new fetch cycle...
INFO - TSLA stock successfully loaded
INFO - Fetched 120 records
INFO - Sleeping for 90 seconds...
```

---

## 🚦 API Rate Limiting

The system handles:

- 1 request per second limit  
- 25 requests per day limit  
- Invalid API key errors  
- Premium endpoint warnings  

If the rate limit is reached, the producer waits before retrying.

---

## 🚧 Current Status

### ✅ Completed

- Dockerized microservices  
- Kafka broker (KRaft mode)  
- Spark cluster setup  
- PostgreSQL containerized  
- Alpha Vantage API integration  
- Rate-limit handling  
- Continuous producer loop  
- Environment variable security  
- Kafka UI integration  
- pgAdmin integration  

### 🔜 In Progress / Next Steps

- Connect producer to Kafka topic  
- Implement Spark Structured Streaming  
- Write processed data to PostgreSQL  
- Build Power BI dashboard  
- Add schema validation  
- Add unit tests  
- Add CI/CD pipeline  
- Deploy to cloud (AWS / Azure / GCP)  

---

## 🧠 Engineering Concepts Demonstrated

- Real-time streaming architecture  
- Event-driven processing  
- Distributed computing (Spark cluster)  
- Container orchestration  
- Environment-based configuration  
- Fault-tolerant API consumption  
- Infrastructure as Code (Docker Compose)  

---

## 🛡️ Security Notes

- No API keys stored in repository  
- `.env` file excluded via `.gitignore`  
- Services run on internal Docker network  
- PostgreSQL not publicly exposed  
- Localhost ports are development-only  

---

## 📂 Project Structure

```
.
├── Producer/
│   ├── config.py
│   ├── extract.py
│   └── main.py
├── Dockerfile
├── compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Future Improvements

- Kafka topic partitioning strategy  
- Dead-letter queue handling  
- Monitoring (Prometheus + Grafana)  
- Logging centralization  
- Kubernetes deployment  
- Production-ready configuration profiles  

---

## 👨‍💻 Author

Tony Kwofie  
Real-Time Data Engineering Project  
2026
