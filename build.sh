#!/bin/bash

# set vars
image="trivia_tips_bot"
account_id=$(aws sts get-caller-identity --query "Account" | grep -o [0-9]*)
region=$(aws configure get region)

# build the image
docker build -t $image .

# push image to ecr
aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $account_id.dkr.ecr.$region.amazonaws.com
docker tag  $image:latest $account_id.dkr.ecr.$region.amazonaws.com/$image:latest
docker push $account_id.dkr.ecr.$region.amazonaws.com/$image:latest
