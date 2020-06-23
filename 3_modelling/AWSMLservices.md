# AWS services for Machine Learning

Apart from SageMaker, Amazon offers multiple services for computing, storage and high-level services to add ML capabilities to our applications.

## Computing 

### EC2 Instances

AWS offers instances types designed to accelerate training and inference of ML algorithms. These types start with `ml`, and are available in different configuration of CPU, GPU, memory, and networking capacity.

For Sagemaker, these instance types are recommended:
- ml.m4.{xlarge, 4xlarge, 10xlarge}: standard
- ml.c4.{xlarge, 2xlarge, 8xlarge}: compute optimized 
- ml.p2.{xlarge, 8xlarge, 16xlarge}: accelerate computing with GPUs
- ml.eia2.{medium, large, xlarge}: inference acceleration 

### Amazon Machine Images (AMI)

If EC2 instances are used for ML without SageMaker, it's useful to use AMIs created for ML and DL tasks:

- AWS Deep Learning AMIs: instances pre-installed with deep learning frameworks and interfaces such as TensorFlow, PyTorch, Apache MXNet, Chainer, Gluon, Horovod, and Keras. They are available options with Conda, Amazon Linux, Ubuntu and CUDA.

### ECR

SageMaker executes code in training and inference docker images. There are prebuilt images or one can be customized. 

To make a container Sagemaker compatible, AWS developed the [SageMaker Training Toolkit](https://github.com/aws/sagemaker-training-toolkit) python library.

```sh 
pip install sagemaker-training
```

Especify the environment variable `SAGEMAKER_PROGRAM` with the script containing the training code.

To use GPU devices, the containers need to be NVIDIA-docker compatible, for that, the `CUDA toolkit` has to be included in the containers.

For inference, use the [SageMaker Inference Toolkit](https://github.com/aws/sagemaker-inference-toolkit). Install the library in the container and set the entrypoint with a script that calls the model server.

```sh 
pip3 install multi-model-server sagemaker-inference
```
To load a model artifact not trained in SageMaker, set the `ModelDataUrl` with the model location, the file should be a `tar.gz`. 
The web server in the container should respond to `/invocations` and `/ping` (HTTP 200 status code and an empty body) on port 8080 and accept socket connection requests within 250 ms, and the model should respond within 60 seconds.


## High-Level Services

### Amazon Forecast

Forecasts for time series using DL. **AutoML** chooses best model for the given dataset or one built-in algorithm can be selected: ARIMA, DeepAR+, Exponential Smoothing (ETS), Non-Parametric Time Series (NPTS) and Prophet.

### Amazon Comprehend

NLP services to extract insights from documents: key phrases, entities, sentiment, language, topics and classification. It includes **Amazon Comprehend Medical** which is specific for clinical tests.
Using **AutoML**, it can be customized with your own data.

### Amazon Transcribe

Transform audio to text. The input can be a FLAC, MP3, MP4, or WAV file, in a specified language or streaming audio (HTTP/2 or WebSocket) for some languages ('fr', 'en' 'es'). It can return the output by speaker.

### Amazon Translate

Translate CSV or TMX files. New words can be added for translation.

### Amazon Polly

Neural Text-To-Speech with many voices and supports many languages. You can customized lexicon, speech rate, pitch, and pauses. With Speech Synthesis Markup Language (SSML), additionally emphasis of words or sentences, pronunciation, breathing and whispering can be controlled. 
As output, Polly can return speech marks, which is metadata indicating when a word starts or ends. This is useful for visualizations as facial animation or highlighting of words in a text when they are pronounced. 

### Amazon Lex

Natural-language chatbot deep learning engine which powers Amazon Alexa. Lambda functions are invoked to determine the intent of the speaker and take an action. It can be deployed in AWS Mobile SDK, Facebook Messenger, Slack, and Twilio.

### Amazon Rekognition

It makes image and video analysis easier. It includes: facial analysis, celebrity recognition, inappropriate content recognition, text detection, among others. Images should be save in S3, and videos in Kinesis Video Streams.

## Complementary services

- **Amazon Personalize**: Recommender system
- **Amazon Textract**: Optical Character Recognition (OCR)
- **AWS DeepRacer**: Reinforcement learning powered race car
- **Amazon CodeGuru**: Automated code reviews
- **Amazon Augmented AI (A2I)**: workflows for human review of predictions
- **DeepLens**: Deep learning-enabled video camera
- **Amazon Sumerian**: Tools to create high-quality virtual reality (VR) experiences
- **Amazon Braket**: Quantum computing, now in preview


# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
- [Amazon SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-dg.pdf)
