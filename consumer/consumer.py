from pyspark.sql import SparkSession
from pyspark.sql.types import TimestampType
from pyspark.sql.functions import from_json, col
from pyspark.sql import DataFrame
from config import postgres_config, checkpoint_dir, kafka_data_schema

# Initialize Spark session
spark = SparkSession.builder.appName("KafkaSparkStreaming").getOrCreate()

# Read stream from Kafka
df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "stock_analysis")
    .option("kafka.group.id", "spark-consumer-group")
    .option("startingOffsets", "latest")
    .option("failOnDataLoss", "false")
    .load()
)

# Convert Kafka value (JSON string) to structured columns
parsed_df = (
    df.selectExpr("CAST(value AS STRING)")
    .select(from_json(col("value"), kafka_data_schema).alias("data"))
    .select("data.*")
)

# Select and cast columns
processed_df = parsed_df.select(
    col("date").cast(TimestampType()).alias("date"),
    col("high"),
    col("low"),
    col("open"),
    col("close"),
    col("symbol"),
)


def write_to_postgres(batch_df: DataFrame, batch_id: int) -> None:
    batch_df.write.format("jdbc").mode("append").options(**postgres_config).save()


# Stream to PostgreSQL
query = (
    processed_df.writeStream.foreachBatch(write_to_postgres)
    .option("checkpointLocation", checkpoint_dir)
    .outputMode("append")
    .start()
)

query.awaitTermination()
