pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Code Checked Out'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Skipping tests for now'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t fastapi-jwt .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container'
                sh '''
                docker stop fastapi-jwt-container || true
                docker rm fastapi-jwt-container || true
                docker run -d -p 8000:8000 --name fastapi-jwt-container fastapi-jwt
                '''
            }
        }
    }
}
