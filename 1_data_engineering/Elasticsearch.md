# Elasticsearch

Search NoSQL database and high-performance search engine used normally for log analytics, real-time application monitoring, and clickstream analysis. AWS offers **Kibana** to create dashboards with the indexed data. 

To use Elasticsearch a domain is created, this domain is the access point to an Elasticsearch cluster. The clusters has one or multiple instance of a given type and storage resources.

## Data Indexing

Indices are distributed into **shards**, which is a horizontal partition that is held in a DB server. Each shard can have zero or more replicas. 

ES as a RESTful search engine enables data indexing through HTTP requests. Stream data can be loaded to ES from Amazon Kinesis Data Firehose, Amazon CloudWatch Logs, and using AWS Lambda functions from Amazon S3, Amazon Kinesis Data Streams, and Amazon DynamoDB.

## Best practices

- Estimate the number of shards based on data size and the expected shard size as changing the number of primary shards while data is indexed is not possible
- For development and testing purposes, a domain can be in only one availability zone but in production, it's recommended to use Multi-AZ and dedicated master nodes.


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
