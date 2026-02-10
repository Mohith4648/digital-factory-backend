pipeline {
    agent any
    stages {
        stage('1. Environment Setup') {
            steps {
                // We force the permission again inside the pipeline just to be 100% sure
                sh 'sudo chmod 666 /run/user/$(id -u)/podman/podman.sock || true'
                sh 'podman --version'
            }
        }
        stage('2. Build Backend') {
            steps {
                script {
                    // Using 'script' block with a try-catch to catch the "Silent Exit"
                    try {
                        sh 'podman build -t digital-factory-backend:local .'
                    } catch (Exception e) {
                        echo "Build failed: ${e.message}"
                        // This forces the error to show up in the logs
                        sh 'podman build -t digital-factory-backend:local . 2>&1'
                    }
                }
            }
        }
    }
}
