# Elastic MapReduce

Managed cluster platform based on the Hadoop framework to run Big Data tools such as Spark, Hive, Flink, Presto. MapReduce is an obsolete programming model from Hadoop.

- Resources are managed be default with YARN (Yet Another Resource Negotiator)
- Collection of nodes (EC2 instances) with different roles: master, core (host HDFS data) and task (which can be **spot instances**)
- Provision nodes if core nodes fails and can add task nodes on the fly
- Clusters can be started and scheduled from **AWS Data Pipeline**
- Spark streaming dataset can be created from a **Kineses Data Stream**
- Includes notebooks capabilities with **Apache Zeppelin**
- Offers EMR Notebooks (for free!) as extension of Jupyter notebooks with more AWS integrations
  - Backed up to S3
  - Provision cluster from the notebook
  - Secured through a VPC
- Apart fom IAM, SSH and IAM roles along with notebooks tags, it can integrate Kerberos authentication

## Storage

- **Hadoop Distributed File System (HDFS)**: Good performance but it's ephemeral, used only to save intermediate results
- **EMR File System (EMRFS)**: Access data in S3 directly via the `s3://` scheme, saves the metadata in Dynamo DB
- **Local system**: default disk in the EC2 instance


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)