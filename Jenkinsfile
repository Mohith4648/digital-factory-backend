pipeline {
    agent any

    environment {
        APP_NAME = "digital-factory-backend"
        // Update this to your actual email
        USER_EMAIL = "your-email@gmail.com" 
    }

    stages {
        stage('1. Checkout') {
            steps {
                echo 'Pulling source code from GitHub...'
                git branch: 'main', 
                    credentialsId: 'github-creds', 
                    url: 'https://github.com/Mohith4648/digital-factory-backend.git'
            }
        }

        stage('2. Environment Check') {
            steps {
                echo 'Checking for required tools...'
                sh 'whoami'
                sh 'echo $PATH'
                // This checks if podman exists before trying to run it
                sh 'which podman || echo "Podman not found on this path"'
            }
        }

        stage('3. Build Image') {
            steps {
                echo "Building Container Image: ${APP_NAME}"
                // Adding PATH export to help Jenkins find the tool
                sh 'export PATH=$PATH:/usr/bin:/usr/local/bin && podman build -t ${APP_NAME} .'
            }
        }

        stage('4. Deploy') {
            steps {
                echo "Deploying ${APP_NAME} to Production Port 8000..."
                sh "export PATH=$PATH:/usr/bin && podman stop ${APP_NAME} || true"
                sh "export PATH=$PATH:/usr/bin && podman rm ${APP_NAME} || true"
                sh "export PATH=$PATH:/usr/bin && podman run -d --name ${APP_NAME} -p 8000:8000 ${APP_NAME}"
            }
        }
    }

    post {
        always {
            echo "Pipeline Execution Finished."
        }
        success {
            emailext body: """
                <h3>Build SUCCESSFUL</h3>
                <p>Project: ${env.JOB_NAME}</p>
                <p>Build Number: ${env.BUILD_NUMBER}</p>
                <p>URL: <a href='${env.BUILD_URL}'>View Build</a></p>
                <p>Digital Factory Backend is now live on Port 8000.</p>
            """,
            subject: "SUCCESS: ${env.JOB_NAME} [Build #${env.BUILD_NUMBER}]",
            to: "${env.USER_EMAIL}"
        }
        failure {
            emailext body: """
                <h3>Build FAILED</h3>
                <p>Project: ${env.JOB_NAME}</p>
                <p>Build Number: ${env.BUILD_NUMBER}</p>
                <p>Check the console logs here: <a href='${env.BUILD_URL}console'>Console Output</a></p>
            """,
            subject: "ALERT: ${env.JOB_NAME} Failed",
            to: "${env.USER_EMAIL}"
        }
    }
}
