pipeline {
    agent any 

    environment {
        // Ensuring Python knows where the app code is
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // We use --user to avoid permission issues on the Jenkins host
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Static Analysis (Ruff)') {
            steps {
                // This will fail the build if Ruff finds unfixable errors[cite: 2]
                sh 'python3 -m ruff check app/'
            }
        }

        stage('Unit Tests (Pytest)') {
            steps {
                // This will fail the build if any test fails
                sh 'python3 -m pytest tests/'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        failure {
            echo 'The build failed! Check the Ruff or Pytest logs above.'
        }
    }
}
