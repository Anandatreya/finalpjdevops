//    This Jenkinsfile will login to GitHub repository , performs a lint on app program, perform a docker build based
//    on Dockerfile in Github. The image is then pushed into Docker Hub  
//    The Docker container is then deployed  on the Target BLUE Deployment server Kubernetes cluster
//    PLease change the server IP address to the BLUE server before uploading this script to GitHub  

    pipeline{
            agent any
            stages {
                stage('GitHub Connect') {
                steps {
                    git (url:'https://github.com/Anandatreya/finalpjdevops', branch:'Blue-Deployment')
                }
            }
            
            stage('Linting for Python code') {
             
             steps {
                sh 'make'
                sh 'make all'
            //    sh 'python3 -m venv ~/.devops'
            //    sh 'pip install --upgrade pip && pip install -r requirements.txt'
                sh 'pylint --disable=R,C,W1203 app.py'
             }
         }
           
                stage ('Docker Container Build'){
                steps{
                        
                    sh 'docker build -t anandatreya/finalpjdevops --tag=finalpjdevops .'
                }
                
                }
                stage ('Push Docker Image to Hub'){
                steps{
                withCredentials([string(credentialsId: 'docker-id', variable: 'dockerhubPw')]) {
                    sh "docker login -u anandatreya -p ${dockerhubPw}"
                }       
                    sh 'docker push anandatreya/finalpjdevops'
                }
                
                }
               stage('Deploy Kubernetes Cluster') {
             steps {
                 sshagent(['ubuntu-server']) {
    
    sh "scp -o StrictHostKeyChecking=no blue-controller.json ubuntu@54.212.118.220:/home/ubuntu"
    sh "scp  blue-green-service.json ubuntu@54.212.118.220:/home/ubuntu"
    
    sh "ssh -o StrictHostKeyChecking=no ubuntu@54.212.118.220 kubectl apply -f blue-controller.json"
    sh "ssh ubuntu@54.212.118.220 kubectl apply -f blue-green-service.json"
  
}             
}
         }


            }
        }