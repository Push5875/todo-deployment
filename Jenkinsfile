pipeline {
    agent any  // Runs on any available agent

    environment {
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials')
        REPO_URL = 'https://github.com/Push5875/todo-deployment.git'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        // stage('Build') {
        //     steps {
        //         echo 'Building the project...'
        //         sh 'make build'  // Example build command
        //     }
        // }
        
        // stage('Test') {
        //     steps {
        //         echo 'Running tests...'
        //         sh 'make test'  // Example test command
        //     }
        // }
        
        // stage('Docker Build & Push') {
        //     steps {
        //         script {
        //             docker.build('my-app-image:latest')
        //                 .withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS)
        //                 .push('latest')
        //         }
        //     }
        // }
        
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying the application...'
        //         sh './deploy.sh'  // Example deployment script
        //     }
        // }
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
