# finalpjdevops
This is the repository for the Capstone  Project for the Cloud Devops Nano degree program 
This is the sub-branch of the master branch and is used to execute the Cloudformation scripts to build the EC2 instances. 
The Repository contains the following files:

1. Jenkinsfile
2. Project Submission_K8ClusterInitdocx - This is the step by step screenshot of the Cloudformation script of the Jenkins workflow.
3. UdagramNetwork.yml - This is the network setup of the cloudformation. THis was run outside the jenkins environment via CLoudformation CLI.
4. UdagramNetwork-parameters.json - This is the parameter file for the UdagramNetwork.yml
5. UdagramServer.yml - This is the server setup of the cloudformation and is executed from the Jenkins pipeline. This builds the EC2 instances as well as brings the instances under a Load Balancer.
6. UdagramServer-parameters.json - This is the parameter file for the UdagramServer.yml
