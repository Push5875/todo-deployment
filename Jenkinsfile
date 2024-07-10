pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Push5875/todo-deployment.git'
            }
        }

        stage {
            steps {
                sh 'git checkout dev'
            }
        }

        stage('Build docker image') {
            steps {
                script{
                    dockerImage = docker.build("scheduler-app:1.0.0")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

    }

    post {
        always {
            cleanWS()
            sh 'echo "Pipeline and Clean Up finished."'
        }
    }
}
