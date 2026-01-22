pipeline {
    agent any

    environment {
        DOCKER_CONFIG = "${WORKSPACE}/.docker"
    }

    stages {

        stage('Prepare Docker Config') {
            steps {
                sh '''
                mkdir -p $DOCKER_CONFIG
                echo '{}' > $DOCKER_CONFIG/config.json
                '''
            }
        }

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
