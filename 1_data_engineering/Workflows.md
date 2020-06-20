# Workflows

## AWS Data Pipeline

It automates the movement and transformation of data (S3, RDS, Redshift, DynamoDB) based on task dependencies definitions.
A pipeline schedules and runs tasks in EC2 or EMR instances (allowing more control than Glue), which are executed by a task runner assigned by Data Pipeline. Data Pipeline support retries and notifies on failures.


## AWS Step Functions

AWS Step Functions coordinates the components of distributed applications as a series of **tasks** in a visual workflow. It builds and runs **state machines** to execute each task. Tasks are triggered, tracked and retried if necessary automatically.

States machines are defined using Amazon States Language, JSON-based language to define a collection of states (Tasks for execution and Choices for transitions) with their dependencies. Tasks states use **Lambda functions** or an **Activity** to execute a tasks. Activities are executed in workers on EC2 or ECS and are only available in **Standard workflows**.

For long tasks **Standard workflows**, it's recommended to set the `TimeoutSeconds` to configure for how long the state will wait and send a heartbeat from the activity worker `SendTaskHeartbeat` within the time set in `TimeoutSeconds`. For some services (AWS Batch, ECS, Glue, SageMaker and EMR), you can specify the `.sync` suffix to tell the Step Functions to wait for the job till completion. CloudWatch Logs can be enabled for these types of state machines.


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)