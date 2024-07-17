pipeline {
    agent any
     
    environment {
        SONARQUBE_SERVER = 'sonarqube-scanner'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Push5875/todo-deployment.git'
            }
        }

        stage('Checkout Branch Development') {
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
                    dockerImage = docker.build("scheduler-app:dev")
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

        stage("Execute SonarQube Scanner"){
            steps{
                withSonarQubeEnv(SONARQUBE_SERVER) {
                    sh 'sonar-scanner'
                }
            }
        }
        
        stage('Quality-Gate') {
            steps{
                def qg = waitForQualityGate()
                if (qg.status != 'OK') {
                    error "Pipeline aborted due to quality gate failure: ${qg.status}"
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
        }
    }
}
