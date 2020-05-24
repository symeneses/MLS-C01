# RDS

Amazon Relational Database Service (Amazon RDS) is used to set up and operate scalable DB instances which run on a DB engine. 
It manages backups, software patching, automatic failure detection, replicas (read replicas for MySQL, MariaDB, or PostgreSQL) and recovery. 

# Aurora

Amazon Aurora (Aurora) is an open source relational database engine that supports MySQL and PostgreSQL. 

# Redshift

Relational database query and management system designed to build data warehouses for business intelligence applications. It optimizes query performance through a combination of parallel processing, **columnar data storage**, and data compression encoding schemes: compressed data is load in memory and uncompressed for query execution. 
Data can be query directly in S3 using Redshift Spectrum. 

# DynamoDB

Amazon DynamoDB is a fully managed NoSQL **Key-value** database service. It scales the data and traffic for a table over a sufficient number of servers to handle the request capacity. 
It supports on demand backups and point-in-time recovery (to any point in time during the last 35 days) and DynamoDB Streams which captures data modification events in DynamoDB tables.
It is serverless as S3, so it doesn't require provisioning.

# ElastiCache

**In-memory** NoSQL database ideal to deploy a distributed cache environment. It works for Redis and Memcached engines.

# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
