# AWS services for ML solutions deployment

## SageMaker Neo 

Optimizes trained models in the hardware (Intel, NVIDIA, ARM, Cadence, Qualcomm, and Xilinx) where the model is deployed. It compiles TensorFlow, MXNet, and PyTorch models to create binary code and writes it in a shared object library, getting an executable that can run anywhere. The `compiler` saves two files: model definition and parameters. The `runtime` in execution loads these two files, and the shared object library.

## AWS IoTGreengrass

AWS IoT Greengrass executes AWS Lambda functions locally reducing network transactions while using the cloud for management, analytics, and storage. Having a model compiled by SageMaker Neo, it can infer using local data with the model trained in the cloud.

## Inference Pipelines

Flow of containers that process requests for real-time and batch inferences on data. With this services, you can define a pipeline to execute preprocessing, predictions, and post-processing. It supports Spark ML and scikit-learn.

# Monitoring

Apart from the SageMaker model monitor, we can use AWS CloudWatch to keep track of SageMaker services.

## CloudWatch

CloudWatch is monitoring services for AWS Services. It collects and tracks predefined and customs performance metric, which can be used for automatic scaling of SageMaker endpoints. Metrics are kept for 15 months, but the console limits the search to metrics updated in the last 2 weeks.
It supports setting alarms (SNS, SQS), AWS Batch jobs, Lambda or Step functions execution, among others, if metrics are outside defined thresholds, dashboards and integration with Grafana.

### Endpoint Invocation Metrics in SageMaker

**InvokeEndpoint**: Inference
- Invocation4XXErrors: request with 4xx HTTP response code
- Invocation5XXErrors: request with 5xx HTTP response code 	
- Invocations: InvokeEndpoint requests sent to a model endpoint
- ModelLatency: time models takes to respond with the inference
- OverheadLatency: total time minus the `ModelLatency`

Additional metrics are measured for multi-model endpoints

**Processing Job, Training Job, Batch Transform Job, and Endpoint Instance Metrics**
- CPUUtilization: CPU units used by containers on an instance in percentage
- MemoryUtilization : percentage of memory that is used by the containers on an instance
- GPUUtilization: GPU units that are used by the containers on an instance in percentage
- GPUMemoryUtilization: percentage of GPU memory used by the containers on an instance
- DiskUtilization: percentage of disk space used by the containers

CloudWatch also reports metrics for Amazon SageMaker Ground Truth.


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)