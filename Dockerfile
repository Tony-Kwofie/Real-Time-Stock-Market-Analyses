FROM spark:3.5.1-python3

# Switch to root to install packages
USER root

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Switch back to spark user (best practice)
USER spark

CMD ["python3", "producer/main.py"]
