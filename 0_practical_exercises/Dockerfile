FROM python:3.7

RUN apt-get update -qq && apt-get install -y python3-dev && \
    ln -sfn /usr/bin/python3 /usr/bin/python

RUN mkdir /aws
WORKDIR /aws

ADD requirements.txt /aws/
RUN pip install -r requirements.txt

ADD . /aws/

# copy the training script inside the container
# COPY train.py /opt/ml/code/train.py

# define train.py as the script entry point
# ENV SAGEMAKER_PROGRAM train.py