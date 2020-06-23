# Built-In Algorithms

SageMaker provides different algorithms for most ML use cases. We will review them seeing their input and important aspects to consider for training.

## General considerations

### Data Input
- **RecordIO**: is a set of binary data exchange formats to divide data in records. This format reduces size and facilitate continuos reading. AWS recommends this format as build-in algorithms are optimized to with work with it
- **CSV**: CSV file with no header with the target variable in the first column, for unsupervised learning defined `text/csv;label_size=0` in the content type 

### Modes

- **File**: training data is downloaded to an encrypted Amazon Elastic Block Store (EBS)
- **Pipe**: use streamed data to the training instances, saving disk space and speeding up the jobs. Only supported with RecordIO formatted input data

### Training

- Most algorithms perform better with GPUs instances, with exception of `XGBoost` which was not developed by Amazon
- Amazon SageMaker models are stored as `model.tar.gz` in a S3 bucket, when the model is untarred, it contains the file `model_algo-1`, which is a serialized **Apache MXNet** object
- For inference, the content type can be `text/csv`, `application/json`, and `application/x-recordio-protobuf`. XGBoost only supports `text/csv`

## Linear Learner

**Input**
- Data has to be normalized before or on demand while executing
- For better performance, data should be shuffled

**Training**
- It runs multiple optimizers simultaneously with Stochastic Gradient Descent (SGD) and chooses the best one.
- It includes L1 and L2 regularization.
- Important Hyperparameters: 
  - `learning_rate`
  - `mini_batch_size`
  - `l1`: Regularization parameter for L1
  - `wd`: Weight decay for L2

## Random Cut Forest

Unsupervised anomaly detection algorithm developed by Amazon. Available also in Kinesis Analytics.

**Input**
- RecordIO or CSV
- Optional test channel to compute metrics

**Training**
- It runs on CPUs
- Creates trees and evaluate complexity after a data point is added
- Important Hyperparameters: 
  - `num_trees`: number of trees
  - `num_samples_per_tree`: random samples given to each tree, it should be in inverse proportion to the anomalies ratio.

## XGBoost

**Input**
- CSV files as it wasn't designed specifically for SageMaker

**Training**
- It's memory intensive and runs on CPU only, therefore, a `ml.m4` instance is recommended
- Important Hyperparameters: 
  - `subsample`: subsample ratio, it helps to prevent overfitting
  - `eta`: step size shrinkage used in updates to prevent overfitting
  - `num_round`: numbers of runs
  - `alpha`: Regularization parameter for L1
  - `lambda`: Regularization parameter for L2 
  - `min_child_weight`: Minimum sum of instance weight (hessian) needed in a child to continue partitioning.

## K-Nearest Neighbors (KNN)

**Input**
- First columns are labels

**Training**
- It reduces dimensions and does random sampling
- Important Hyperparameters: 
  - `k`: number of neighbors


## Principal Components Analysis (PCA)

**Input**
- RecordIO or CSV

**Training**
- It can use the regular algorithm or randomized for large datasets

## K-Means

**Input**
- Optional test channel

**Training**
- To initialize, it can do it at random or with kmeans++, which tries to get clusters' centers far apart from each other
- Important Hyperparameters: 
  - `k`: number of clusters
  - `extra_center_factor`: create extra centers (`num_clusters` * `extra_center_factor`), and during training, it reduces them to the desired cluster.

## Latent Dirichlet Allocation (LDA)

**Input**
- CSV with word counts, total size = number of records * vocabulary size

**Training**
- It runs on CPUs
- Important Hyperparameters: 
  - `num_topics`: number of topics
  - `alpha0`: concentration parameter, low values give more sparse topics

## Factorization Machines

Used mainly for recommended systems or use cases with sparse data

**Input**
- RecordIO with Float32

**Training**
- It calculates feature interactions as the inner product of the factors (vectors embeddings) of each feature. If 2 features are similar, their cosine similarity is higher.
- CPU recommended

## IP Insights

Unsupervised model to find patterns in IP addresses usage, used for security to analyze logs

**Input**
- CSV containing `<entity>, <IP>`

**Training**
- It generates negative samples automatically
- GPU recommended as it's based on NN
- Important Hyperparameters:
  - `vector_dim`: dimension of the vector to represent entities and IP addresses
  - `num_entity_vectors`: number of entities vectors. If too small, it can cause collisions and if too big, it increases memory consumption

## DeepAR

RNN for time series prediction

**Input**
- It can train multiple related time series

**Training**
- Finds frequencies and seasonality
- Runs on CPU's and GPU's
- Special Hyperparameters: 
  - `context_length`: number of time-points seen before making a prediction

## BlazingText

Used mainly for text classification and Word2Vec.

**Input**
- For text classification: `<label> <sentence>`
- For Word2Vec: `<sentence>`

**Training**
- Word2Vec works with different modes: Continuous Bag of Words (CBOW), Skip-gram and Batch Skip-gram which can be distributed as the order of words doesn't matter.
- Special Hyperparameters: 
  - `vector_dim`: dimension of the word vectors
  - `window_size`: (for W2V) number of words surrounding the target word used for training
  - `negative_samples`: (for W2V) number of negative samples (random contexts different to the target words)

## Neural Topic Model

Based on the Neural Variational Inference algorithm. Used to organized documents by topic or classify or summarize documents.

**Input**
- Integer tokens

**Training**
- It runs on CPUs or GPUs
- Important Hyperparameters:
  - `num_topics`: number of topics

## Seq2Seq

Implemented using RNN and CNN with attention.

**Input**
- Integers tokens

**Training**
- It runs on GPU's and a single machine
- Pre-trained models available
- Can automatize for accuracy, BLEU score and perplexity
- Special Hyperparameters: 
  - `num_layers_encoder`: Number of layers for Encoder rnn or cnn.
  - `num_layers_decoder`: Number of layers for Decoder rnn or cnn.

## Object2Vec

[//]: <> (TODO Extend as it's unique in AWS)

Create vectors or embeddings of high-dimensional objects, where similar objects are close. Similar to Word2Vec, encoding sentences or paragraphs.

**Input**
- Pairs of integer token lists, these can be of different size
- The label can be a tag with the relation of the pairs or the strength of their relation

**Training**
- Encoders are Average-pooled embeddings, Hierarchical CNNs or BiLSTMs.
- With the environment variable `INFERENCE_PREFERRED_MODE`, it can be selected which embeddings are loaded in the GPU for inference (`classification` or `embeddings`)

## Image Classification

**Input**
- RecordIO or images (jpg or png)
- .lst file with: `Image index`, `class`, and `path` 
- Augmented Manifest (configurable JSON file) 

**Training**
- ResNet CNN

## Object Detection

Identify objects with their bounding boxes.

**Input**
- RecordIO or images (jpg or png)

**Training**
- Uses Single Shot multibox Detector (SSD) on top of a CCN (VGG-16 or ResNet-50)

## Semantic Segmentation

Pixel-level object classification

**Input**
- RecordIO or images (jpg or png)
- Augmented Manifest (configurable JSON file) 

**Training**
- Can be trained on GPUs (p2 and p3)
- Built on MXNet Gluon

# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
- [Amazon SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-dg.pdf?icmpid=docs_sagemaker_lp)
