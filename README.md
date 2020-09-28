# finalpjdevops
This is the repository for the Capstone  Project for the Cloud Devops Nano degree program 
The  project involves developing a comprehensive CI/CD pipeline for a microservices application using a Blue/Green deployment strategy.

Following technologies have been employed to achieve the project objectives:
Jenkins - To manage an automated CI/CD pipeline integrating with Docker Hub, AWS and Kubernetes cluster
Docker - Containerize a Python based microservices application
Kubernetes - Provide a container orchestration approach
AWS - All the servers are deployed completely in the AWS cloud
AWS Cloudformation - Extensive use of AWS stacks capability to automate provisioning of AWS back end networking and server infrastructure
AWS CLI - To help create the AWS Cloudformation stacks
Visual Studio Code - This IDE is used to develop the scripts and code required for the project
GitHub - All source code repositories are managed via GitHub

a) Jenkins Pipeline:

A Jenkins pipeline serves as the core automation engine of the project architecture.
The Jenkins pipeline delivers a Continuous Integration service environment automating real time code updates made to the GitHub repository and taking the code through linting checks. 
Further, the Jenkins pipeline code is extended to organize a Continuous Delivery environment, packaging the application code and operating system environment into a Docker container. The Docker container is managed via Docker Hub.

b) Docker Containers:
The application code and essential Operating system environment is packaged and containerized using Docker. All Docker code repositories are managed via the Docker Hub.

Container Orchestration:
Container Orchestration is achieved using Kubernetes cluster (MiniKube) that hosts and manages the containerized code for the application. 

c) AWS Cloudformation (IAC):
The project makes use IAC (Infrastructure AS a Code) methodology using AWS Cloudformation to provision the AWS EC2 servers for the Kubernetes cluster components.
The Cloudformation automated templates provision the base network components (composed of a VPC, Private/Public subnets and Routing, Autoscaling group), EC2 servers and the Kubernetes cluster installation on each server during server provisioning (as startup scripts). 
Cloudformation templates allow for rapid provisioning and tear down of the environment through the usage of Cloudformation stacks. Also, usage of pre-defined, parameterized and reusable Cloudformation templates allow for expanding the environment with changing needs.  

d) How does the code work:
There are three separate pipelines to the Jenkins pipeline functionality:

Part A - CloudFormation stack creation pipeline stage - This stage logs in to the GitHub repository where the Cloudformation stack scripts are stored and executes the Stack creation process to build the EC2 instances as well as install the Kubernetes cluster software in each server (as startup scripts).

Part B - Blue Deployment pipeline - This multi-stage pipeline logs in to the GitHub repository, prepares the python runtime environment, performs linting of the application code using pylint, builds a Docker container, pushes Docker image to the Docker hub and finally deploys the containerized code to the Kubernetes cluster. The deployment is exposed through the service that points to the new deployment.

Part C - Green Deployment pipeline - This multi-stage pipeline logs in to the GitHub repository, makes the python environment, performing linting of the application code using pylint, builds a Docker container, pushes Docker image to the Docker hub and finally deploys the containerized code to the Kubernetes cluster. The deployment is exposed through the service that points to the new deployment.


