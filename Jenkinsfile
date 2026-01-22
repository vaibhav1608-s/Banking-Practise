pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Skipping tests for now'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t fastapi-jwt .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                /usr/local/bin/docker stop fastapi-jwt-container || true
                /usr/local/bin/docker rm fastapi-jwt-container || true
                /usr/local/bin/docker run -d -p 8000:8000 --name fastapi-jwt-container fastapi-jwt
                '''
            }
        }
    }
}
