# Built-In Algorithms

SageMaker provides different algorithms for most ML use cases. We will review them seeing their input and important aspects to consider for training.

## General considerations

### Data Input
- **RecordIO**: is a set of binary data exchange formats to divide data in records. This format reduces size and facilitate continuos reading. AWS recommends this format as build-in algorithms are optimized to with work with it
- **CSV**: CSV file with no header with the target variable in the first column, for unsupervised learning defined `text/csv;label_size=0` in the content type 

### Modes

- **File**: training data is downloaded to an encrypted Amazon Elastic Block Store (EBS)
- **Pipe**: use streamed data to the training instances, saving disk space and speeding up the jobs. Only supported with RecordIO formatted input data for some algorithms

### Training

- Most algorithms perform better with GPUs instances, with exception of `XGBoost` which was not developed by Amazon
- Amazon SageMaker models are stored as `model.tar.gz` in a S3 bucket, when the model is untarred, it contains the file `model_algo-1`, which is a serialized **Apache MXNet** object
- For inference, the content type can be `text/csv`, `application/json`, and `application/x-recordio-protobuf`. XGBoost only supports `text/csv`

## Linear Learner

**Input**
- RecordIO with `Float32` tensors or CSV, supporting Pipe mode for both formats
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

Open-source software library that distributed Gradient Boosting

**Input**
- CSV files or LibSVM (`<label> <index1>:<value1>... <indexN>:<valueN>`)
- Supported only in File mode
- Optional validation channel

**Training**
- It's memory intensive and runs on CPU only, therefore, a `ml.m4` instance is recommended
- Important Hyperparameters: 
  - `subsample`: subsample ratio, it helps to prevent overfitting
  - `eta` or `learning_rate`: step size shrinkage used in updates to prevent overfitting
  - `gamma` or `min_split_loss`: minimum loss reduction required to do a partition
  - `scale_pos_weight`: balance of positive and negative weights, helpful for unbalanced datasets, recommended to set with `sum(negative_samples)/sum(positive_samples)`
  - `num_round`: numbers of runs
  - `alpha`: Regularization parameter for L1
  - `lambda`: Regularization parameter for L2 
  - `min_child_weight`: Minimum sum of instance weight (hessian) needed in a child to continue partitioning

## K-Nearest Neighbors (KNN)

**Input**
- First columns are labels
- RecordIO or CSV
- Optional test channel

**Training**
- It reduces dimensions and does random sampling
- Runs on CPU or instances with single GPU
- Important Hyperparameters: 
  - `k`: number of neighbors

## Principal Components Analysis (PCA)

**Input**
- RecordIO or CSV in File mode
- Optional test channel

**Training**
- Runs on GPU or CPU
- It can use the regular algorithm or randomized for large datasets

## K-Means

**Input**
- RecordIO or CSV
- Optional test channel

**Training**
- Runs on CPU or instances with single GPU
- To initialize, it can do it at random or with kmeans++, which tries to get clusters' centers far apart from each other
- Important Hyperparameters: 
  - `k`: number of clusters
  - `extra_center_factor`: create extra centers (`num_clusters` * `extra_center_factor`), and during training, it reduces them to the desired cluster.

## Latent Dirichlet Allocation (LDA)

**Input**
- RecordIO or CSV in File mode
- For CSV with word counts and total size = number of records * vocabulary size

**Training**
- It supports only single-instance CPU training
- Important Hyperparameters: 
  - `num_topics`: number of topics
  - `alpha0`: concentration parameter, low values give more sparse topics

## Factorization Machines

Used mainly for recommended systems or use cases with sparse data. It calculates feature interactions as the inner product of the factors (vectors embeddings) of each feature. If 2 features are similar, their cosine similarity is higher.

**Input**
- RecordIO with `Float32`
- Optional Test channel 

**Training**
- CPU is recommended, GPU for dense data

## IP Insights

Unsupervised model to find patterns in IP addresses usage, used for security to analyze logs

**Input**
- CSV containing `<entity>, <IP>`
- Optional validation channel
- Supported only in File mode

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
- Supported only in File mode
- Input is given in JSON lines in a json, gzip or Parquet file
- Optional test channel

**Training**
- Finds frequencies and seasonality
- I needs at least training time series is at least 300
- Runs on CPU's or GPU's
- Special Hyperparameters: 
  - `context_length`: number of time-points seen before making a prediction

## BlazingText

Used mainly for multi-class, multi-label text classification and Word2Vec. It extends the **fastText** text classifier to work with multi-core CPUs or GPUs and Word2Vec on GPUs with optimized `CUDA` kernels.

**Input**
- File with text with space-separated tokens, including punctuation marks
- For text classification: `<label> <sentence>`, or Augmented Manifest (configurable JSON file) in Pipe Mode
- For Word2Vec: `<sentence>`
- Validation channel in the supervised mode (classification)

**Training**
- Word2Vec works with different modes: Continuous Bag of Words (CBOW), Skip-gram and Batch Skip-gram which can be distributed as the order of words doesn't matter.
- Single instance GPU or CPU
- Special Hyperparameters: 
  - `vector_dim`: dimension of the word vectors
  - `window_size`: (for W2V) number of words surrounding the target word used for training
  - `negative_samples`: (for W2V) number of negative samples (random contexts different to the target words)

## Neural Topic Model

Based on the Neural Variational Inference algorithm. Used to organized documents by topic or classify or summarize documents.

**Input**
- Integer tokens
- Optional test and validation channels

**Training**
- It runs on CPUs or GPUs
- Important Hyperparameters:
  - `num_topics`: number of topics

## Seq2Seq

Encode-decoder architecture implemented using RNN and CNN with attention. Used for, among others, Machine Translation (MT), text summarization, speech-to-text.

**Input**
- Integers tokens in RecordIO format
- Train, validation and vocab (`vocab.src.json and vocab.trg.json`) channels
- It supports only File mode

**Training**
- It runs on GPU's and a single machine
- Pre-trained models available
- Can automatize for accuracy, BLEU score and perplexity
- Special Hyperparameters: 
  - `num_layers_encoder`: Number of layers for Encoder rnn or cnn.
  - `num_layers_decoder`: Number of layers for Decoder rnn or cnn.

## Object2Vec

Create vectors or embeddings of high-dimensional objects, where similar objects are close. Two **Encoders** convert the two **Input** channels in vectors on a fixed length which are the input to a **Comparator**, which scores the relation of the pairs. The algorithm aims to find encoders that minimize the difference between the values calculated by the comparator and the given label.
Similar to Word2Vec, encoding sentences or paragraphs in vectors which can be used as features in downstream tasks. Useful for recommendation systems as well.

**Input**
- Pairs of integer token lists, these can be of different size
- The label can be a tag with the relation of the pairs or the strength of their relation
- Supported only in File mode with JSON lines as input
- Optional test and validation channels

**Training**
- It runs on CPU or on multiple GPUs in a single instance 
- Encoders are Average-pooled embeddings, Hierarchical CNNs or BiLSTMs.
- With the environment variable `INFERENCE_PREFERRED_MODE`, it can be selected which embeddings are loaded in the GPU for inference (`classification` or `embeddings`)
- Special Hyperparameters: 
  - `token_embedding_dim`: input layer dimension
  - `enc_dim`: encoding dimension
  - `negative_sampling_rate`: ratio of negative to positive samples to be created automatically
  - `comparator_list`: ways to compare the embedding: `hadamard` (element-wise product), `concat` (concatenation), and `abs_diff` (absolute difference). It can take multiple options, concatenating vectors in the given order.

## Image Classification

**Input**
- RecordIO or images (jpg or png)
- .lst file with: `Image index`, `class`, and `path` 
- Augmented Manifest (configurable JSON file) 

**Training**
- ResNet CNN, therefor
- Trained only on GPU

## Object Detection

Identify objects with their bounding boxes.

**Input**
- RecordIO or images (jpg or png)
- Optional test and validation channels

**Training**
- Runs only on GPUs
- Uses Single Shot multibox Detector (SSD) on top of a CCN (VGG-16 or ResNet-50)

## Semantic Segmentation

Pixel-level object classification

**Input**
- RecordIO or images (jpg or png)
- Augmented Manifest (configurable JSON file)
- Train and validation channels, and label_map and model optional channels

**Training**
- Trained only on a single instance GPU (p2 and p3)
- Built on MXNet Gluon

# References

- [AWS Documentation](https://docs.aws.amazon.com/index.html)
- [Amazon SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-dg.pdf?icmpid=docs_sagemaker_lp)
