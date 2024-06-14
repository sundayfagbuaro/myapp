pipeline{
    agent{
        label "JENKINS-AGENT-1"
    }
    stages{
        stage("Checkout SCM"){
            steps{
                script{
                    git branch: 'main', credentialsId: 'git-hub', url: 'https://github.com/sundayfagbuaro/myapp.git'
                }
                
            }
            
        }
        stage('Build Docker Image'){
            steps{
                echo 'Building docker image'
                sh 'docker build -t sundayfagbuaro/myapp:1.0.0 .'
            }
        }
    }
}

