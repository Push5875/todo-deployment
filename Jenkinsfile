pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Push5875/todo-deployment.git'
            }
        }

        stage('Build docker image') {
            steps {
                script{
                    dockerImage = docker.build("scheduler-app:1.0.0")
                }
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
