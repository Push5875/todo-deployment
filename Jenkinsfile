pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Push5875/todo-deployment.git'
            }
        }

        stage('Build') {
            steps {
                // Commands to build your project (e.g., mvn clean install for a Maven project)
                sh 'echo "Building project..."'
            }
        }

        stage('Test') {
            steps {
                // Commands to test your project
                sh 'echo "Running tests..."'
            }
        }

        stage('Deploy') {
            steps {
                // Commands to deploy your project
                sh 'echo "Deploying project..."'
            }
        }
    }

    post {
        always {
            // Commands that should always run after the pipeline (e.g., clean up)
            sh 'echo "Pipeline finished."'
        }
    }
}
