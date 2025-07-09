## 목표

-   Docker-Compose를 활용한 로컬 Kafka 클러스터 구축.
-   Python을 이용한 Producer/Consumer 구현으로 메시지 스트리밍 파이프라인 경험.
-   Kafka 핵심 아키텍처(Broker, Topic, Partition)에 대한 실질적인 이해도 확보.

## 아키텍처

[Kafdrop Success Screen]
<img width="1072" height="782" alt="Image" src="https://github.com/user-attachments/assets/3c4221a1-8cb4-4e8f-9509-a0768fc8aa8a" />

<img width="1031" height="851" alt="Image" src="https://github.com/user-attachments/assets/0fcadd69-ebc7-4741-8c3d-d9d31aa94607" />

-   **Zookeeper:** 카프카 클러스터의 메타데이터 관리 및 브로커 상태 모니터링.
-   **Kafka Broker:** 메시지 수신, 디스크 저장, 컨슈머 요청에 따른 메시지 제공.
-   **Producer (`producer.py`):** `hello-kafka` 토픽으로 1초마다 메시지 발행.
-   **Consumer (`consumer.py`):** `hello-kafka` 토픽을 구독하여 새로운 메시지 수신 및 출력.
-   **Kafdrop:** 웹 UI를 통한 Kafka 클러스터 상태 및 토픽/메시지의 시각적 모니터링.

## 실행 방법

1.  **Prerequisites:** Docker Desktop, Python 3.x
2.  **Install Library:** `pip install kafka-python`
3.  **Run Cluster:** `docker-compose up -d`
4.  **Run Producer:** `python producer.py`
5.  **Run Consumer:** `python consumer.py`
6.  **Check UI:** 웹 브라우저에서 `http://localhost:19000` 주소로 접속.

## 주요 내용 (Learnings)

-   Producer-Broker-Consumer 모델의 데이터 흐름을 코드로 직접 구현하며 명확히 이해함.
-   Docker-Compose를 통해 여러 컴포넌트로 이루어진 분산 시스템의 격리된 구성 및 관리 방법 습득.
-   Kafdrop UI를 통해 토픽과 파티션의 개념, 그리고 메시지가 실제로 저장되고 소비되는 방식을 시각적으로 확인.

## 향후 계획 (Future Works)

-   본 프로젝트는 Kafka의 기본 동작 원리 학습을 위해 로컬 환경에 구축함.
-   다음 단계로, 주력 기술인 **Terraform을 활용**하여 이 환경을 **AWS MSK(Managed Streaming for Kafka)로 마이그레이션**하는 것을 목표로 함.
-   이를 통해 클라우드 환경에서의 고가용성 구성, 모니터링, 비용 최적화 방안 등 **안정적인 대규모 데이터 플랫폼을 책임지는 플랫폼 엔지니어**로서의 실무 역량을 확보해 나갈 계획.
