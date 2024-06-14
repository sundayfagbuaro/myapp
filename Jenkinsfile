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
        stage('Push Image to Docker Hub'){
            steps{
                echo 'Pushing image to docker hub'
                withCredentials([string(credentialsId: 'docker-pwd', variable: 'DockerHubPwd')]) {
                sh 'docker login -u sundayfagbuaro -p ${DockerHubPwd}' 
                }
                sh 'docker push sundayfagbuaro/myapp:1.0.0'
            }
        }
        stage('Deploy myapp to k8 cluster'){
            kubernetesDeploy (configs: "deployment.yaml", kubeconfigId: 'k8config')
        }
    }
}

