# Security in AWS

## General recommendations

To make sure, our systems are secured we have to consider these best practices: 
- Restricts access to AWS S3 and EC2 to a minimum, using AWS IAM
- Use SSL/TLS to communicate with AWS resources
- Configuring a firewall for your virtual network with security groups and ACLs
- Enable data encryption for your database or other storage systems
- Enable multi-factor authentication (MFA)
- Encrypt Personal Identifiable Information (PII) using AWS Key Management Service (KMS)
- Use AWS CloudTrail to log the history of AWS API calls (user, IP address, time) in the Management Console, AWS SDKs, command line, and other services


## AWS Identity and Access Management (IAM)

IAM is a web service for securely controlling access to AWS services through different levels of abstraction.

- IAM user: authenticate people accessing a AWS account
- IAM group: collection of users
- IAM role: use to authenticate a specific resources i.e a EC2 instance
- IAM policy: define the permissions for a user, group, or role

### IAM in SageMaker

- **Actions that need user permissions:** CreateTrainingJob, CreateModel, CreateEndpointConfig, CreateTransformJob, CreateHyperParameterTuningJob, CreateNotebookInstance and UpdateNotebookInstance
- **Predefined policies:** AmazonSageMakerReadOnly, AmazonSageMakerFullAccess, AdministratorAccess and DataScientist

## Amazon Virtual Private Cloud (Amazon VPC)

Enable execution of resources into a private virtual network. Inside a VPC, subnets can be created to add more layers of security.

Working with VPCs
- Have public subnets for load balancers and web servers, and private subnets for databases
- If the internet is disable for notebooks, the VPC needs a PrivateLink or Network Address Translation (NAT) Gateway. 

**NAT Gateway**: allows private subnets to reach internet through a public IP address, while internet can't reach the private subnet. AWS charges NAT Gateways per hour of availability plus data processing charges per Gigabytes. 
**AWS PrivateLink**: allows access to some AWS services (EC2, ELB, Kinesis Streams, Systems Manager (SSM), Service Catalog, and Amazon SNS) from private subnets. It doesn't create public IPs; instead, a Elastic Network Interfaces (ENI) with private IPs in the VPC.

**References**

- WITTIG, Michael; WITTIG, Andreas; WHALEY, Ben. Amazon web services in action. Second Edition. Manning, 2018.
