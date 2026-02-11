pipeline {
    agent any

    environment {
        // Define your Docker Hub credentials ID (stored in Jenkins Credentials)
        DOCKER_CREDS = credentials('docker-hub-credentials-id')
        IMAGE_NAME = "your-docker-username/angular-app"
    }

    stages {
        // 1. CHECKOUT
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // 2. INSTALL DEPENDENCIES
        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }

        // 3. CODE QUALITY
        stage('Code Quality') {
            steps {
                sh 'npm run lint'
                sh 'npx tsc --noEmit'
            }
        }

        // 4. RUN UNIT TESTS
        stage('Run Unit Tests') {
            steps {
                // Runs tests in headless mode so Jenkins doesn't hang
                sh 'npm test -- --watch=false --browsers=ChromeHeadless'
            }
        }

        // 5. BUILD PRODUCTION
        stage('Build Production') {
            steps {
                sh 'npm run build -- --prod'
            }
        }

        // 6. BUILD DOCKER IMAGE
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        // 7. PUSH & DEPLOY
        stage('Push & Deploy') {
            steps {
                // Login and Push to Docker Hub
                sh "echo ${DOCKER_CREDS_PSW} | docker login -u ${DOCKER_CREDS_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                sh "docker push ${IMAGE_NAME}:latest"
                
                // Smoke Test (Example: check if container starts)
                sh "docker run --rm ${IMAGE_NAME}:latest /bin/sh -c 'ls /usr/share/nginx/html'"
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
