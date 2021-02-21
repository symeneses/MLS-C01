# To execute in chunks in VS Code, Jupyter-like cells are created with # %%
# %%
import datetime
import os

import requests
from requests_aws4auth import AWS4Auth

from mls.aws import (create_client, create_resource, create_session,
                     execute_task)


# %%
# Create AWS session
aws_session = create_session()
region = aws_session.region_name
credentials = aws_session.get_credentials()
aws_user = os.getenv('aws_user')
account_number = os.getenv('account_number')
external_ip = os.getenv('external_ip')
# %%
# Set variables for testing
file_names = ['text1.txt', 'text2.txt', 'text3.txt', 'text4.txt', 'text5.txt']
bucket_name = 'mls-c01-sample-data'
domain_name = 'mls-c01-es-domain'
es_index = 'quotes'
es_index_type = 'quotes-comprehend'

# %%
# Save files in S3
s3_resource = create_resource('s3', aws_session)
s3_bucket = s3_resource.Bucket(bucket_name)
if not s3_bucket.creation_date:
    s3_bucket.create(CreateBucketConfiguration={
        'LocationConstraint': region
    })
for fn in file_names:
    s3_bucket.upload_file(
        'sample_data/text/' + fn,
        'text/' + fn.split('.')[0])

# %%
# Send each file to Comprehend for key phrases and sentiment.
# Index the final data in Elastic search
# Elastic search
es_client = create_client('es', aws_session)
# Create domain
# The activation of the domain takes few minutes
es_domain = execute_task(
    es_client,
    'create_elasticsearch_domain',
    DomainName=domain_name,
    ElasticsearchVersion="6.8",
    ElasticsearchClusterConfig={
        'InstanceType': 't2.medium.elasticsearch',
        'InstanceCount': 1},
    EBSOptions={
        'EBSEnabled': True,
        'VolumeType': 'standard',
        'VolumeSize': 10},
    AccessPolicies='{"Version": "2012-10-17", "Statement":' +
    '[{"Effect": "Allow", "Principal":{"AWS":"arn:aws:iam::' +
    account_number + ':user/' + aws_user +
    '"}, "Action":"es:*", "Resource":"arn:aws:es:' +
    region + ':' + account_number +
    ':domain/' + domain_name + '/*"}, ' +
    '{"Effect": "Allow", "Principal": {"AWS": "*"}, "Action": "es:ESHttp*", ' +
    '"Condition": {"IpAddress": {"aws:SourceIp": ' +
    '"' + external_ip + '"}}, "Resource": "arn:aws:es:' +
    region + ':' + account_number +
    ':domain/' + domain_name + '/*"}]}')

# %%
# Comprehend resource
comprehend_resource = create_client('comprehend', aws_session)
for fn in file_names:
    # Reading text from S3
    text = s3_bucket.Object(
        'text/' +
        fn.split('.')[0]).get()['Body'].read()[
        :5000].decode('utf-8').lower()
    # Getting Key Phrases from text
    kp_request = execute_task(comprehend_resource, 'detect_key_phrases',
                              Text=text,
                              LanguageCode='en')
    key_phrases = [i['Text'] for i in kp_request['KeyPhrases']]
    # Sentiment
    sentiment = execute_task(
        comprehend_resource,
        'detect_sentiment',
        Text=text,
        LanguageCode='en')['Sentiment']
    # Indexing in Amazon Elasticsearch
    # Amazon Elasticsearch Service URL
    try:
        es_endpoint = es_client.describe_elasticsearch_domain(
            DomainName=domain_name)['DomainStatus']['Endpoint']
    except KeyError:
        print('Elasticsearch domain not active')

    url = 'https://' + es_endpoint + '/' + es_index + '/' + es_index_type
    # Create the header
    headers = {'Content-Type': 'application/json'}
    # Create the JSON body
    payload = {'text': text, 'keywords': key_phrases,
               'sentiment': sentiment,
               'timestamp': datetime.datetime.now().isoformat()}
    print(payload)
    # Provide all details necessary to sign the indexing request.
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key,
                       region, 'es', session_token=credentials.token)
    es_request = requests.post(
        url,
        auth=awsauth,
        json=payload,
        headers=headers)
    print(es_request.json())
# Now you can create fancy plots in Kibana :)
# %%
# Delete bucket and domain after finishing the exercises
s3_bucket.objects.delete()
s3_bucket.delete()
es_client.delete_elasticsearch_domain(DomainName=domain_name)
