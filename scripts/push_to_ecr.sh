#!/usr/bin/env bash

if [ -z "$AWS_ACCOUNT" ]; then
	echo "Please set the AWS_ACCOUNT environment variable"
	exit 1
fi

if [ -z "$AWS_DEFAULT_REGION" ]; then
	echo "Please set the AWS_DEFAULT_REGION environment variable"
	exit 1
fi

IMAGE_NAME=$1

echo "Building image: $IMAGE_NAME:latest"

docker build --rm -t $IMAGE_NAME:latest .

eval $(aws ecr get-login --no-include-email) || EXIT_STATUS=$?

docker tag $IMAGE_NAME $AWS_ACCOUNT.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_NAME:latest || EXIT_STATUS=$?

docker push $AWS_ACCOUNT.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_NAME:latest || EXIT_STATUS=$?

exit $EXIT_STATUS
