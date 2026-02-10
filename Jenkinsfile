pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pulling from your real repo
                git branch: 'main', url: 'https://github.com/Mohith4648/digital-factory-backend.git'
            }
        }
        stage('Podman Build') {
            steps {
                echo 'Starting Local Build...'
                // We use the full path to ensure it finds podman
                sh '/usr/bin/podman build -t digital-factory-backend:local .'
            }
        }
    }
}
