FROM confluentinc/cp-kafka:7.4.10  

USER root

# 1. Create the application directory
RUN mkdir -p /usr/app

ADD https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/1.0.1/jmx_prometheus_javaagent-1.0.1.jar /usr/app/jmx_prometheus_javaagent.jar

COPY prom-jmx-agent-config.yml /usr/app/prom-jmx-agent-config.yml

# 4. Set ownership to 'appuser' so Kafka can read the files
RUN chown -R appuser:appuser /usr/app && \
    chmod 644 /usr/app/jmx_prometheus_javaagent.jar /usr/app/prom-jmx-agent-config.yml

# Switch back to the non-root user provided by Confluent
USER appuser