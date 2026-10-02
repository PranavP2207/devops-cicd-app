pipeline {
    agent any

    environment {
        IMAGE_NAME     = 'flask-cicd-app'
        CONTAINER_NAME = 'flask-cicd-container'
        APP_PORT       = '5000'
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER -t $IMAGE_NAME:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
                sh 'docker run -d --name $CONTAINER_NAME -p $APP_PORT:5000 $IMAGE_NAME:latest'
            }
        }

        stage('Verify Application') {
            steps {
                sh 'for i in 1 2 3 4 5 6 7 8 9 10; do curl -fsS http://localhost:$APP_PORT/health && exit 0; sleep 2; done; exit 1'
                sh 'docker ps --filter name=$CONTAINER_NAME'
            }
        }
    }

    post {
        success {
            echo "SUCCESS: $IMAGE_NAME:$BUILD_NUMBER is running at http://localhost:$APP_PORT"
        }
        failure {
            echo 'FAILED: showing container logs (if any)'
            sh 'docker logs $CONTAINER_NAME || true'
        }
    }
}
