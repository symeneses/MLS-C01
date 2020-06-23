## Athena

Serverless query service to analyze data in Amazon S3. It supports CSV, JSON, and columnar data such as Apache Parquet or Apache ORC (Optimized Row Columnar), giving a much better performance. Athena is integrated with the AWS Glue Data Catalog. 

- It is based on Apache Presto
- It can be accessed through the console, API, or SQL clients connected with JDBC or ODBC drivers (i.e. PowerBI, Tableau).
- User-defined functions and stored procedures are not supported
- It could be used to analyze logs from CloudTrail, CloudFront, ELB, etc.
- A typical pipeline for a data lake could be: S3 > Glue or Kinesis Firehose (ETL) > Athena > QuickSight (Visualizations).

## QuickSight

Serverless business intelligence service. It offers data analysis as a basic workspace where different visuals (combo charts, heat and tree maps, pivot tables, etc) or stories (slideshow to show thought process) are created. To share data with other users, it has dashboards which are read-only snapshots.

- It can be used by a broader audience, not only for developers
- Calculations are executed by SPICE a Parallel, In-memory Engine
- ML models (anomaly detection, forecasts based on Random Forest) can be included in analyses and dashboards through Amazon SageMaker
- Price is per user/month plus additional SPICE (> 10 GB)

### Data Sources
- Relational: S3, Aurora, Athena, RedShift, MySQL, Presto, Spark
- Files: CSV, JSON, Excel, zip
- SaaS sources: Adobe Analytics, GitHub, JIRA, Salesforce, Twitter


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)