# AWS Glue

ETL **serverless** service to categorize, clean and enrich data. Glue can be used for most data warehouse or data lake related tasks.

## AWS Glue Data Catalog

Metadata repository which auto infers and versions schemas, including semi-structured data as  such as clickstream or process logs. Integrated with Athena and Redshift.

This metadata is saved in **Databases** with different **Tables**. The tables can have as a source: S3, Kinesis and Kafka. New databases and tables can be create in the console, using AWS CloudFormation templates, or through migration from an Apache Hive metastore.

The catalog is normally populated using **Crawlers** (compatible with JSON, Parquet, CSV, relational DB) which can be executed on a Schedule or On Demand. The crawlers can be created from a data source (S3, JDBC, DynamoDB) or existing catalog tables. T

This allows us to execute serverless queries against a S3 data lake or Kinesis stream, as the Data Catalog keeps the metadata in sync. 

## ETL engine

Execute ETL jobs in predefined python or scala or your own Spark/PySpark scripts.

Most common Transformations
- DropFields, DropNullFields
- Filter
- Join
- Map
- **FindMatches** using ML

AWS Glue provides access in the console to Amazon SageMaker notebooks, Apache Zeppelin notebooks (locally or on EC2) for scripting. You can create a development endpoint and access it locally using Zeppelin or PyCharm.

### Glue Scheduler

Schedule jobs and crawlers using a Unix-like CRON syntax.

### Glue Triggers

Triggers are Data Catalog objects that execute ETL jobs based on events. They can be used to start crawlers, or execute ETL jobs as chains of dependent tasks.
AWS Glue offers **Workflows** to connected multiple crawlers, jobs, and triggers.


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
- [New – Serverless Streaming ETL with AWS Glue](https://aws.amazon.com/blogs/aws/new-serverless-streaming-etl-with-aws-glue/)