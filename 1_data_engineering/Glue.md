# Glue

ETL Service to categorize, clean and enrich data. 

## AWS Glue Data Catalog

Metadata repository which auto infers and versions schemas. Integrated with Athena and Redshift. 

This catalog is normally populated using **Crawlers** (compatible with JSON, Parquet, CSV, relational DB) which can be executed on a Schedule or on demand.  

## ETL engine

Execute ETL jobs in predefined python or scala or your own Spark/PySpark scripts.

Most common Transformations
- DropFields, DropNullFields
- Filter
- Join
- Map
- **FindMatches** using ML

### Glue Scheduler

Schedule Jobs

### Glue Triggers

Execute ETL jobs based on events.