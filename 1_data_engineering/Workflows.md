# Workflows

## AWS Data Pipeline

It automates the movement and transformation of data (S3, RDS, Redshift, DynamoDB) based on task dependencies definitions.
A pipeline schedules and runs tasks in EC2 instances (allowing more control than Glue), which are executed by a task runner assigned by Data Pipeline. Data Pipeline support retries and notifies on failures.


## AWS Step Functions

AWS Step Functions coordinates the components of distributed applications as a series of **tasks** in a visual workflow. It builds and runs state machines to execute each task. Tasks are triggered, tracked and retried if necessary automatically.


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)