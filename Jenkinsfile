/* groovylint-disable LineLength */
pipeline {
    agent any
    environment {
        REPO_URL = 'https://github.com/Push5875/todo-deployment.git'
        BRANCH_NAME = 'dev'
        AWS_REGION = 'us-east-1'
        AWS_ACCOUNT_ID = '992382393618'
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/stockhub"
        IMAGE_REPO_NAME = 'stockhub'
        SERVICE_IMAGE_NAME = 'stockhub-service'
        FRONTEND_IMAGE_NAME = 'stockhub-frontend'
        IMAGE_TAG = 'latest'
        AWS_CRED = 'stockhub-production'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: env.REPO_URL, branch: env.BRANCH_NAME
            }
        }

        stage('Logging into AWS ECR') {
            steps {
                withCredentials([aws(credentialsId: "${AWS_CRED}", region: 'us-east-1')]) {
                    sh '''
                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                    '''
                }
            }
        }

        stage('Build, Tag and Push Docker Images'){
            steps {
                sh '''docker build -t ${SERVICE_IMAGE_NAME}:${IMAGE_TAG} ./backend
                      docker build -t ${FRONTEND_IMAGE_NAME}:${IMAGE_TAG} ./frontend'''
            }
        }
        // stage('Building Docker Images') {
        //     parallel {
        //         stage('Building service image') {
        //             steps {
        //                 script {
        //                     dockerImage = docker.build("${SERVICE_IMAGE_NAME}:${IMAGE_TAG}", 'backend')
        //                 }
        //             }
        //         }

        //         stage('Building frontend image') {
        //             steps {
        //                 script {
        //                     dockerImage = docker.build("${FRONTEND_IMAGE_NAME}:${IMAGE_TAG}", 'frontend')
        //                 }
        //             }
        //         }
        //     }
        // }

        // stage('Pushing to ECR') {
        //     parallel {
        //         stage('Push service image') {
        //             steps {
        //                 script {
        //                     sh """
        //                         docker tag ${SERVICE_IMAGE_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:${IMAGE_TAG}
        //                         docker push ${REPOSITORY_URI}/${IMAGE_REPO_NAME}:${IMAGE_TAG}
        //                     """
        //                 }
        //             }
        //         }

        //         stage('Push frontend image') {
        //             steps {
        //                 script {
        //                     sh """
        //                         docker tag ${FRONTEND_IMAGE_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:${IMAGE_TAG}
        //                         docker push ${REPOSITORY_URI}/${IMAGE_REPO_NAME}:${IMAGE_TAG}
        //                     """
        //                 }
        //             }
        //         }
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
