pipeline {
    agent any  
    environment {
        REPO_URL = 'https://github.com/Push5875/todo-deployment.git'
        BRANCH_NAME = "dev"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: env.REPO_URL, branch: env.BRANCH_NAME
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
