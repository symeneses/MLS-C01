# SageMaker

SageMaker was designed to help data scientist to do the entire ML flow:
- Fetching and cleaning data
- Training and evaluating models
- Deployment and results evaluation

To accomplish its mission SageMaker is powered by these nice functionalities:

**SageMaker Studio**
- New Integrated Development Environment (IDE) for ML including Studio Notebooks, SageMaker Experiments, Autopilot, Debugger and the Model Monitor
- It creates a domain to access the UI and saves the data of each user in a Amazon Elastic File System (Amazon EFS), the EFS volume can be seen in the `HomeEfsFileSystemId`
- It produces real-time data visualizations to compare the best performing models in the **trial leaderboard** ranked by SageMaker Experiments
- It has Git integration

**Notebook Instance**
- Fully managed EC2 instance running within the service accounts
- It is used to orchestrate ETL and ML jobs, that is, extracting data from S3, transforming it with Glue or EMR
- Notebooks can work with EMR clusters using `Sparkmagic`, tool that works using `Apache Livy`
- It has the option to have root access to install tools and packages. Using a **Lifecycle Configuration Script**, the installation of packages or access to other AWS services can be configured, this script is executed when the notebook instance is created

**SageMaker Autopilot**
- Automatic model tuning for classification and regression giving a S3 with the input date, a target attribute and a metric
- Available as a module in the SageMaker SDK `from sagemaker.automl.automl import AutoML`
- `AutoML` preprocess the data, find the best pipeline and creates features, and it creates notebooks as **artifacts** in S3 with the data exploration and the candidate definition with the suggested pipelines
- It allows to deploy the best candidate

**SageMaker Experiments**
- Tracks, compares and evaluates **experiments** and model versions, each experiment has multiple **trials**
- Visualizes ongoing jobs to compare trials
- It can be used to start the SageMaker Autopilot, by default, it tracks SageMaker Autopilot
- It also tracks automatically and SageMaker job, which can be added to a trail afterwards

**SageMaker Debugger**
- Identifies issues during training jobs in Studio and Notebook instances saving the internal model state (e.g, metrics, feature importance) at periodic intervals in S3
- Allows to visualize **Tensors** which contains metrics (weights, gradients, losses) updated during the backpropagation and optimization of deep learning models
- With the library `smdebug`, the user can set up **hooks** to save tensors and **rules** that are checked during training. It supports TensorFlow, PyTorch, MxNet and XGBoost.
- Each rule is a debugging job running in parallel to the training checking the tensors, if the rule is triggered the training will stop.
- Rules enable us to perform, among others, gradient checking (e.g. vanishing gradients) and make sure if the loss is decreasing 

**SageMaker Model Monitor**
- Monitors model performance in production and the quality of the data input
- `DataCaptureConfig` to save data in S3 is configured in the `deploy` function of the model
- It creates a baseline with the training data which estimates **constrains** and **statistics** (e.g. min, max, median, quantile sketches (KLL)) 
- It compares continuously the incoming data with the baseline to alert if there are **violations** like quality issues (e.g. missing values, data with different types) or drifting features


## SageMaker workflow

![sm-model](https://docs.aws.amazon.com/sagemaker/latest/dg/images/sagemaker-architecture.png "Train and deploy a model with Amazon SageMaker")
*Source: https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html*


### Automatic Model Tuning

- SageMaker offers automatic model tuning for built-in algorithms and custom algorithms using pre-built containers
- It applies:
  - **Random Search**: tries random combination of values facilitating concurrent jobs
  - **Bayesian Search**: adjust hyperparameters after each iteration to maximize a given metric using Bayesian Optimization
- If performance is not improving and **Early Stopping** is `Auto` the jobs will stop reducing time and avoiding overfitting
- Previous tuning jobs can be used as **Warm Start**
- It supports multi-algorithm Hyperparameter Optimization (HPO) defening different training definitions.  Warm start and early stopping features are not available for multiple models
- It assumes the parameters are linear-scaled in the beginning, therefore, it's recommended to set as log-scaled the ones you know have a logarithmic scale

### Training parameters

- S3 URL for training data
- The compute resources to be use for model training (see options [here](ComputerPower.md)). It can also work in local mode
- S3 URL to store the output
- ECR path where the training code is stored

### Deployment options 

- Persistent endpoint `InvokeEndpoint` using Amazon SageMaker hosting services
  - Invocation requests can be distributed across multiple `production variants` with predefined weights to perform A/B test
  - For testing, a `TargetVariant` can be selected in the request
  - Weights of variants can be updated to choose the best performing model using `UpdateEndpointWeightsAndCapacities`
- Amazon SageMaker batch transform to get predictions for a entire dataset
- Other AWS Services useful to deploy models are discussed [here](/4_implementation/Deploying.md)

## SageMaker SDK

Along with Boto3, the SageMaker SDK provides the capabilities to go through the ML lifecycle using SageMaker, making possible to develop the code to work with SageMaker anywhere.
- Compatible with Apache MXNet, Chainer, PyTorch, Scikit-Learn, SparkML Serving, TensorFlow and XGBoost
- It has a Reinforcement Learning module
- Supports integration for training and inference workflows with Airflow and Kubernetes

Its functionality is split in these APIs.
**Training APIs**
- Module for tuning and training jobs, including AutoML and Debugger
- The `Processor` class performs data pre- and post- processing
- An `Estimator` trains an algorithm object and return a `Model`
**Inference APIs**
- The class `Model` is deployable in an `Endpoint`
- The `RealTimePredictor` makes requests to get predictions the `Endpoint` 
- Options to configure the Model Monitor 
- `PipelineModel` creates a Model to build an **Inference Pipeline**
**Utility APIs**
- Interacts with objects and jobs in the SageMaker session
- It contains configuration to access a `S3DataSource` or a `FileSystemInput`, upload `S3Uploader` and download `S3Downloader` data from S3
- Functions to configure the network (Internet access, VPC, encryption) with `NetworkConfig` 

# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
- [Amazon SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-dg.pdf?icmpid=docs_sagemaker_lp)
- [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/index.html)
- [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)