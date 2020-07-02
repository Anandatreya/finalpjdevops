#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath="anandatreya/finalpjdevops"

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run podfinalpjdevops\
	    --generator=run-pod/v1\
	        --image=$dockerpath\
		    --port=8000 --labels app=finalpjdevps

# Step 3:
# List kubernetes pods
kubectl get pods finalpjdevops 

# Step 4:
# Forward the container port to a host
kubectl port-forward podfinalpjdevops  8000:8000
