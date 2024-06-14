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
    }
}
