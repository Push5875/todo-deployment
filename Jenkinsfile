pipeline{
    agent any

    stages{
        stage('Clone repository'){
            steps{
                git 'https://github.com/Push5875/todo-deployment.git'
            }

        stage('Build'){
            steps{
                sh 'echo "Building project..."'
                'docker build -t scheduler:1.0.0 .'
            }
        }
        }
    }
}