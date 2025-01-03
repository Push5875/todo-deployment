 pipeline {
    agent any

    // environment {
    //     // Define environment variables
    //     AWS_REGION = 'us-east-1'
    //     EB_APP_NAME = 'my-python-app'
    //     EB_ENV_NAME = 'my-python-env'
    //     S3_BUCKET_NAME = 'my-app-bucket'
    //     TERRAFORM_REPO = 'git@github.com:your-org/terraform-repo.git'
    // }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the source code repository
                checkout scm
            }
        }

        // stage('Install Dependencies') {
        //     steps {
        //         script {
        //             // Install Python dependencies from requirements.txt
        //             sh 'pip install -r requirements.txt'
        //         }
        //     }
        // }

        // stage('Run Tests') {
        //     steps {
        //         script {
        //             // Run tests (e.g., unit tests, integration tests)
        //             sh 'pytest tests/'
        //         }
        //     }
        // }

        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             // Build Docker image (optional, if using Docker for Elastic Beanstalk)
        //             sh 'docker build -t $EB_APP_NAME .'
        //         }
        //     }
        // }

        // stage('Deploy with Terraform') {
        //     steps {
        //         script {
        //             // Clone the Terraform repository to configure infrastructure
        //             dir('terraform') {
        //                 git url: env.TERRAFORM_REPO

        //                 // Apply Terraform configurations for Elastic Beanstalk
        //                 sh 'terraform init'
        //                 sh 'terraform apply -auto-approve'
        //             }
        //         }
        //     }
        // }

        // stage('Deploy to Elastic Beanstalk') {
        //     steps {
        //         script {
        //             // Deploy the application to Elastic Beanstalk using AWS CLI
        //             sh 'eb init $EB_APP_NAME --region $AWS_REGION'
        //             sh 'eb use $EB_ENV_NAME'
        //             sh 'eb deploy'
        //         }
        //     }
        // }

        // stage('Post-Deploy Cleanup') {
        //     steps {
        //         script {
        //             // Clean up any resources if necessary
        //             echo 'Cleaning up temporary files'
        //             sh 'rm -rf .ebextensions'
        //         }
        //     }
        // }
    }

    post {
        success {
            // Notify on successful deployment
            echo "Deployment was successful"
        }
        failure {
            // Notify on failure (could be extended for Slack, email, etc.)
            echo "Deployment failed"
        }
    }
}
