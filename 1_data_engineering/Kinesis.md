# Kinesis

Managed Apache Kafka, which is used for streaming data (log, IoT, clickstreams).


## Services

1. Kinesis Streams: low latency normally used to ingest data. It can be replay from 1 to 7 days.

`Producers > Shards (Provisioned in advance) > Consumers`

2. Kinesis Analytics: for real time analytics.

`Input stream + Reference tables (S3) > Analytics > Output stream + Errors`

ML Model available:
- Random Cut Forest: For anomaly detection
- Hotspots: Locate dense regions

3. Kinesis Firehose: to ingest data in near real-time and transform  it (CSV/JSON to Parquet/ORC or through AWS Lambda) and storage data  in storage services: S3 (Support compression (GZIP, ZIP)), Redshift, Elasticsearch (Amazon ES), Splunk.

4. Kinesis Video Streams: for real-time video processing or batch-oriented video analytics.

`Producer (i.e. security camera, AWS DeepLens) > Consumer (Any DL model on EC2, AWS SageMaker, Amazon Rekognition video)`