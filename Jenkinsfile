pipeline {
    agent any  
    environment {
        REPO_URL = 'https://github.com/Push5875/todo-deployment.git'
        BRANCH_NAME = "dev"
        AWS_REGION = 'us-east-1'
        AWS_ACCOUNT_ID = '992382393618'
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: env.REPO_URL, branch: env.BRANCH_NAME
            }
        }

        stage('Logging into AWS ECR') {
            steps {
                    script {
                            sh "aws ecr get-login-password - region ${AWS_DEFAULT_REGION} | docker login - username AWS - password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                            }   
                }
        }

        stage('Building image') {
                    steps{
                    script {
                            dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                    }
                    }
                    }
       
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
