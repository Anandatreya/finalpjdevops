# finalpjdevops
This is the repository for the Capstone  Project for the Cloud Devops Nano degree program 
The  project involves developing a comprehensive CI/CD pipeline for a microservices application using a Blue/Green deployment strategy.

A Jenkins pipeline serves as the core automation engine of the project architecture.
The Jenkins pipeline delivers a Continuous Integration service environment automating real time code updates made from the GitHub repository and taking the code through linting checks. Further, the Jenkins pipeline code is extended to organize a Contininuous Deployment environment, packaging the microservices application code and operating system environment into a Docker container. The Docker container is managed via Docker Hub.
Container Orchestration is achieved using Kubernetes cluster (MiniKube) that hosts and manages the containerized code for the application. 
The project makes use of automating the build of AWS EC2 servers for the Minikube cluster components using automated IAC (Infrastructure AS a Code) methodology using AWS Cloudformation. The Cloudformation automated templates that provision the base network components (composed of a VPC, Private/Public subnets and Routing), EC2 server and the Kubernetes cluster installation on each server during server provisioning (as startup scripts). Cloudformation templates allow for rapid provisioning and tear down of the environment through the usage of Cloudformation stacks. Also, usage of pre-defined and reusable Cloudformation templates allow for expanding the environment with changing needs.  
