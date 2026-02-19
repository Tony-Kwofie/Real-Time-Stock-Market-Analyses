🚀 Real-Time Stock Market Data Pipeline

A fully containerized real-time data engineering pipeline built using:

🐍 Python

📨 Apache Kafka

⚡ PySpark

🐘 PostgreSQL

🐳 Docker & Docker Compose

📊 Power BI (for visualization)

📌 Project Overview

This project implements an end-to-end real-time stock market data pipeline:

Python Producer

Fetches stock market data from Alpha Vantage API

Handles rate limits and API errors

Sends structured data downstream

Kafka

Acts as a real-time message broker

Buffers streaming stock data

Spark

Processes streaming data

Enables scalable distributed computation

PostgreSQL

Stores processed stock data

Power BI

Connects to PostgreSQL

Visualizes stock trends in real-time

🏗️ Architecture
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


All services are orchestrated using Docker Compose.

🐳 Dockerized Services
Service	Image Used	Port
Kafka	confluentinc/cp-kafka:7.4.10	9092
Spark Master	spark:3.5.1-python3	7077
Spark Worker	spark:3.5.1-python3	—
PostgreSQL	debezium/postgres:17	5434
pgAdmin	dpage/pgadmin4:9	5050
Kafka UI	provectuslabs/kafka-ui:v0.7.2	8085
Producer	Custom Docker image	—
🔗 Access Services (Local Development)

Once containers are running:

Service	URL
Kafka UI	http://localhost:8085

pgAdmin	http://localhost:5050

Spark Master UI	http://localhost:8081

Kafka Broker	localhost:9092

⚠️ These URLs are for local development only.
They do not expose sensitive data and are safe to include in documentation.

⚙️ Environment Variables

Create a .env file in the root directory:

API_KEY=your_alpha_vantage_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres


⚠️ .env is excluded via .gitignore and should never be committed.

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/Real-Time-Stock-Market-Analyses.git
cd Real-Time-Stock-Market-Analyses

2️⃣ Build and start services
docker compose up -d --build

3️⃣ Verify containers
docker ps

4️⃣ View logs (example)
docker logs consumer

🔄 Producer Behavior

The producer:

Fetches TSLA, MSFT, GOOGL stock data

Runs continuously

Respects API rate limits

Sleeps between cycles to prevent throttling

Example log output:

INFO - Starting new fetch cycle...
INFO - TSLA stock successfully loaded
INFO - Fetched 120 records
INFO - Sleeping for 90 seconds...

🚧 Current Status

✔ Dockerized microservices
✔ Kafka broker configured (KRaft mode)
✔ Spark cluster configured
✔ PostgreSQL containerized
✔ API integration with rate limit handling
✔ Continuous producer loop

🔜 Next Steps:

Connect Spark streaming to Kafka

Write processed data to PostgreSQL

Connect Power BI dashboard

Deploy to cloud (AWS / Azure / GCP)

🧠 Engineering Concepts Demonstrated

Real-time streaming architecture

Event-driven data processing

Distributed systems (Spark cluster)

Container orchestration

Environment-based configuration

Fault-tolerant API consumption

Rate-limit handling

Infrastructure as Code

🛡️ Security Notes

No API keys are stored in the repository

Environment variables are externalized

Services run on internal Docker network

PostgreSQL is not publicly exposed

📂 Project Structure
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

📈 Future Improvements

Add schema validation

Add unit testing

Implement Kafka topic partitioning

Add CI/CD pipeline

Deploy with Kubernetes

Add monitoring (Prometheus + Grafana)

👨‍💻 Author

Tony Kwofie

Real-time Data Engineering Project
2026
