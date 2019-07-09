#!/usr/bin/env bash

export AWS_ACCOUNT="your_account_id"
export AWS_REGION="us-east-1"
export IMAGE_TAG="whatever_v1"

rm -rf k8s/application.yml

envsubst < k8s/application.yml.template > k8s/application.yml
