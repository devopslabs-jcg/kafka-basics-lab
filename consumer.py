from kafka import KafkaConsumer

# Kafka Consumer 설정 (Docker 외부에서 접속)
consumer = KafkaConsumer(
    'hello-kafka',
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest', # 처음부터 모든 메시지를 읽음
    group_id='my-consumer-group',
    value_deserializer=lambda m: m.decode('utf-8')
)

print(" Start consuming messages...")
try:
    for message in consumer:
        print(f"Received: '{message.value}' from Topic '{message.topic}'")
except KeyboardInterrupt:
    print("\n Stop consuming messages.")
finally:
    consumer.close()
