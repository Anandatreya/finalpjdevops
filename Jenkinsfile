//    This Jenkinsfile will login to gitHub repository , performs a lint on app program, perform a docker build based
//    on Dockerfile in Github. The image is then pushed into Docker Hub  
//    The Docker image is then run on the Target Green Deployment server
//    PLease change the server IP address to the Green server before uploading this script to GitHub  
//    def dockerRun= 'docker run -p 8000:80 -d anandatreya/finalpjdevops --name finalpjdevop'
pipeline{
            agent any
            stages {
                stage('GitHub Connect') {
                steps {
                    git (url:'https://github.com/Anandatreya/finalpjdevops', branch:'Green-Deployment')
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
                stage ('Run Docker on Target Host'){
                steps{
//              def dockerRun= 'docker run -p 8000:80 -d anandatreya/finalpjdevops '       
                sshagent(['ubuntu-server']) {
    // some block
                sh 'ssh -o StrictHostKeyChecking=no ubuntu@54.214.60.157 docker run -p 8000:8000 -d anandatreya/finalpjdevops'
}
                }
                
                }


            }
        }