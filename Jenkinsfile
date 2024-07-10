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
                sh 'docker build -t scheduler:1.0.0 .'
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
