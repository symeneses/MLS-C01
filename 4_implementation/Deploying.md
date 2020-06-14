# AWS services for ML solutions deployment

## SageMaker Neo 

Optimizes trained models in the hardware (Intel, NVIDIA, ARM, Cadence, Qualcomm, and Xilinx) where the model is deployed. It compiles TensorFlow, MXNet, and PyTorch models to create a executable that runs anywhere.

## AWS IoTGreengrass

AWS IoT Greengrass executes AWS Lambda functions locally reducing network transactions while using the cloud for management, analytics, and storage. Having a model compiled by SageMaker Neo, it can infer using local data with the model trained in the cloud.

## Inference Pipelines

Flow of containers that process requests for real-time and batch inferences on data. With this services, you can define a pipeline to execute preprocessing, predictions, and post-processing. It supports Spark ML and scikit-learn.

## CloudWatch

CloudWatch is a repository of performance metrics and allows automatic scaling of SageMaker endpoints

# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)