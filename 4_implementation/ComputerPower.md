## Distributed training

### Parameter Servers
Uses dedicated processes to collect gradients computed by workers, aggregate them and distribute the updated gradients back to the workers in an asynchronous manner. Each instance runs a parameter server process and a worker and communicate with the other workers.  
If a worker falls behind, it might submit stale gradients, which means gradients are not updated. If this is happening, reducing the learning rate can be useful. 
To work with this option, a script is available tin the SageMaker TensorFlow container.

### Horovod Framework
Uber's Open Source Distributed Deep Learning Framework for TensorFlow 1.12 or newer, Keras, PyTorch, and Apache MXNet. Horovod uses `Ring-AllReduce`, which means the data depends on the number of clusters and not on the number of workers or processes. The gradients are updated synchronously, then, gradients are sent with all the processes in the batch finish. 
SageMaker automates the Horovod cluster setup.

## Managed Spot Training

For training complex model with large data, using spot instances is an option to save money. They need some time to become available, thus, they should be used for time taking tasks.
Spot instances can be *interrupted* at any moment 2 minutes after being warned, therefore, it's a good practice to save `checkpoints` in S3. 

## Elastic Inference

Accelerates deep learning inference by adding low-cost GPUs (e.g ml.eia2.medium) to multiple machines. It has support for TensorFlow, Apache MXNet, and ONNX models through MXNet.

# References

- [Launching TensorFlow distributed training easily with Horovod or Parameter Servers in Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/launching-tensorflow-distributed-training-easily-with-horovod-or-parameter-servers-in-amazon-sagemaker/)
- [AWS Documentation](https://docs.aws.amazon.com/index.html)