pipeline {
    agent any
    environment {
        APP_NAME = "digital-factory-backend"
    }
    stages {
        stage('Checkout') {
            steps {
                // Jenkins pulls your code from GitHub
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/Mohith4648/digital-factory-backend.git'
            }
        }
        stage('Build Image') {
    steps {
        echo 'Building Podman Image...'
        // We use the full path to avoid "not found" errors
        sh "/usr/bin/podman build -t ${APP_NAME} ."
    }
}
        stage('Deploy') {
            steps {
                echo 'Deploying to Port 8000...'
                sh "podman stop ${APP_NAME} || true"
                sh "podman rm ${APP_NAME} || true"
                sh "podman run -d --name ${APP_NAME} -p 8000:8000 ${APP_NAME}"
            }
        }
    }
}
