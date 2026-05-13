pipeline {
    agent {
        docker { image 'python:3.11-slim' }
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install requests pytest'
            }
        }
        stage('Unit Tests') {
            steps {
                // This will fail the build if any test fails
                sh 'pytest tests/test_sniffer.py'
            }
        }
        stage('Quality Gate') {
            steps {
                echo "Tests passed! Ready for K8s deployment."
            }
        }
    }
}
