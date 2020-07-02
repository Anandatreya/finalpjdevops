// Pipeline script to run create a stack in Cloudformation
// The script creates a Server stack
pipeline{
        agent any
        stages {
            stage('GitHub Connect') {
             steps {
                git (url:'https://github.com/Anandatreya/finalpjdevops', branch:'cloudformation-setup')
             }
         }
            
             stage ('AWS server Stack Creation'){
              steps{
                // Creating a server stack
                sh "aws cloudformation create-stack --stack-name myudagramserverstack --region 'us-west-2' --template-body file://UdagramServer.yml --parameters file://Udagramserver-parameters.json"
              }
            
        }
    }
}