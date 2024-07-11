pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Push5875/todo-deployment.git'
            }
        }

        stage('Checkout Branch') {
            steps {
                sh 'git checkout dev'
            }
        }

        stage('Pull latest code') {
            steps{
                sh 'git pull'
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
                script {
                    dockerImage.inside {
                        sh 'pytest --maxfail=1 --disable-warnings --html=report.html'
                    }
                }
            }
        }

    }

    post {
        always {
            sh 'echo "Pipeline and Clean Up finished."'
        }

        success {
            sh 'echo "Pipeline success"'
        }

        failure {
            sh 'echo "Pipeline failed"'
            mail to: 'mhatrepushpak00@rediffmail.com',
             subject: "Pipeline failed",
             body: "The pipeline has failed. Check the Jenkins console for details."
        }
    }
}
