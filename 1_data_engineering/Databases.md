# RDS

Amazon Relational Database Service (Amazon RDS) is used to set up and operate scalable DB instances which run on a DB engine. In `High Availability` mode (HA), the master and standby databases are deployed in different availability zones (Multi-AZ). 
It manages backups, software patching, automatic failure detection, replicas (read replicas for MySQL, MariaDB, or PostgreSQL) and recovery.
For large database migration to RDS with minimal downtime, AWS offers the `Database Migration Service (DMS)`.

# Aurora

Amazon Aurora (Aurora) is an open source **relational database** engine built by Amazon that supports MySQL and PostgreSQL. Data is store on a cluster volume, unlike RDS which stores data on EBS volume.

# Redshift

Relational database query and management system designed to build data warehouses for business intelligence applications. It optimizes query performance through a combination of parallel processing, **columnar data storage**, and data compression encoding schemes: compressed data is load in memory and uncompressed for query execution.
To create a data warehouse with Redshift, a **Redshift Cluster** needs to be created, which can have multiple databases. Data can be queried in the console, in the query editor or from any SQL client tool using JDBC and ODBC connections.
Data can be query directly in S3 using **Redshift Spectrum**.

# DynamoDB

Amazon DynamoDB is a fully managed NoSQL **Key-value** database service. It scales the data and traffic for a table over a sufficient number of servers to handle the request capacity. 
It supports on demand backups and point-in-time recovery (to any point in time during the last 35 days) and `DynamoDB Streams` which captures data modification events in DynamoDB tables.
It is serverless as S3, so it doesn't require provisioning.

# ElastiCache

**In-memory** NoSQL database ideal to deploy a distributed cache environment.  A caching layer helps to speed up applications while reducing costs on the DB. To keep the data update, data will expire after some time and if the cache is full, unused data is evicted.

It works for Redis and Memcached engines with AWS added enhancements.


# References

- WITTIG, Michael; WITTIG, Andreas; WHALEY, Ben. Amazon web services in action. Second Edition. Manning, 2018.
- [AWS Documentation](https://docs.aws.amazon.com/index.html)
