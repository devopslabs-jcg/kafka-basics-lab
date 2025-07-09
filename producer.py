import time
from kafka import KafkaProducer

# Kafka Producer 설정 (Docker 외부에서 접속)
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda v: str(v).encode('utf-8')
)

topic_name = 'hello-kafka'
message_id = 0

print("Start producing messages...")
try:
    while True:
        message = f"Message ID: {message_id}"
        producer.send(topic_name, value=message)
        print(f"Sent: {message}")
        message_id += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\n Stop producing messages.")
finally:
    producer.close()
