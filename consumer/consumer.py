# ==========================================
# Imports
# ==========================================

import os

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    FloatType,
)
from pyspark.sql.functions import (
    from_json,
    col,
    to_timestamp,
)

# ==========================================
# Checkpoint Directory
# ==========================================

checkpoint_dir = "/tmp/checkpoint/kafka_to_postgres"

# (No need to manually create directory in Spark containers)

# ==========================================
# Kafka Schema (Matches extract_json output)
# ==========================================

kafka_data_schema = StructType(
    [
        StructField("symbol", StringType(), True),
        StructField("date", StringType(), True),
        StructField("open", FloatType(), True),
        StructField("high", FloatType(), True),
        StructField("low", FloatType(), True),
        StructField("close", FloatType(), True),
    ]
)

# ==========================================
# Spark Session
# ==========================================

spark = SparkSession.builder.appName("KafkaSparkStreaming").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ==========================================
# Read Stream From Kafka
# ==========================================

raw_df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "stock_analysis")
    .option("startingOffsets", "latest")
    .option("failOnDataLoss", "false")
    .load()
)

# ==========================================
# Parse JSON
# ==========================================

parsed_df = (
    raw_df.selectExpr("CAST(value AS STRING) as json_value")
    .select(from_json(col("json_value"), kafka_data_schema).alias("data"))
    .select("data.*")
)

# ==========================================
# Cast Proper Types
# ==========================================

processed_df = parsed_df.withColumn("date", to_timestamp(col("date"))).select(
    "date",
    "symbol",
    "open",
    "high",
    "low",
    "close",
)

# ==========================================
# Write To Console (Debug Mode)
# ==========================================

query = (
    processed_df.writeStream.outputMode("append")
    .format("console")
    .option("truncate", "false")
    .option("checkpointLocation", checkpoint_dir)
    .start()
)

query.awaitTermination()
