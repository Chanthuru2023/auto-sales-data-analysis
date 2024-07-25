pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the Git repository
                git branch: 'main', url: 'https://github.com/Chanthuru2023/auto-sales-data-analysis.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    dockerImage = docker.build('auto-sales-data-analysis:latest')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests inside the Docker container
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
