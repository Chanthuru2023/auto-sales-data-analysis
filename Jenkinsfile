pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the Git repository
                git 'https://github.com/Chanthuru2023/auto-sales-data-analysis'
            }
        }
        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    dockerImage = docker.build('auto-sales-data-analysis:latest')
                }
            }
        }
        stage('Test') {
            steps {
                // Run tests inside the Docker container
                script {
                    dockerImage.inside {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                // Run the Docker container
                sh 'docker run -d -p 5000:5000 auto-sales-data-analysis:latest'
            }
        }
    }
}
