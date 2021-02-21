import logging
import os

from boto3.session import Session
from botocore.exceptions import ClientError

access_key_id = os.getenv('aws_access_key_id')
if not access_key_id:
    # In case, it's not execute in container
    ## from dotenv import load_dotenv
    ## load_dotenv('secret.env')
    access_key_id = os.getenv('aws_access_key_id')
secret_access_key = os.getenv('aws_secret_access_key')
region_name = os.getenv('region_name')


def create_resource(service, session=None):
    if not session:
        try:
            session = create_session()
        except ClientError as e:
            logging.error(e)
            raise
    return session.resource(service)


def create_client(service, session=None):
    if not session:
        try:
            session = create_session()
        except ClientError as e:
            logging.error(e)
            raise
    return session.client(service)


def execute_task(resource, task, **kwargs):
    try:
        return getattr(resource, task)(**kwargs)
    except ClientError as e:
        logging.error(e)
        raise


def create_session():
    return Session(aws_access_key_id=access_key_id,
                   aws_secret_access_key=secret_access_key,
                   region_name=region_name)
