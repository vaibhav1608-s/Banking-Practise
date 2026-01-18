pipeline{
    agent any

    stages{
        stages('Checkout Code'){
            steps{
                echo'Code Checked Out'
                Checkout scm
            }
        }
        stages('Install Dependencies'){
            steps{
                echo'Building Application'
                sh 'pip install -r requirements.txt'
            }
            stages('Code Quality Check'){
                steps{
                    echo 'Skipping test for Now'
                }
            }
            stage('Build Docker Image'){
                steps{
                    echo'Building Docker image'
                    sh 'docker build -t fastapi-jwt .'
                }
            }
            stage('Run Docker Container'){
                steps{
                    echo'Running  Docker conatiner'
                    sh '''
                    docker stop fastapi-jwt-container || true
                    docker rm fastapi-jwt-container || true
                    docker run -p 8000:8000 --name fastapi-jwt-container fastapi-jwt
                }
            }
        }
    }
} 