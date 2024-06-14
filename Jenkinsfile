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
        stage('Build & Push Docker Image'){
            steps{
                script{
                    sh 'docker build -t sundayfagbuaro/myapp-new:1.0.0 .'
                    withCredentials([string(credentialsId: 'DOCKER-HUB-TOKEN', variable: 'docker-pass')]) {
                    sh 'docker login -u sundayfagbuaro -p $docker-pass'
                    sh 'docker push sundayfagbuaro/myapp-new:1.0.0'
                    }
                }
            }
        }
    }
}
