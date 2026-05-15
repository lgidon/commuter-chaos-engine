pipeline {
    agent {
        docker { 
            image 'python:3.11-slim' 
            // We use a specific version to ensure parity with our venv
            args '-u root:root' 
        }
    }

    stages {
        stage('Install') {
            steps {
                // Inside the container, we don't need a venv!
                sh 'pip install --no-cache-dir -r requirements.txt'
		sh 'pip install ruff'
            }
        }

        stage('Lint') {
            steps {
                // Ruff configuration is read from pyproject.toml[cite: 2]
                sh 'ruff check app/'
            }
        }

        stage('Test') {
            steps {
                // Pytest configuration is read from pyproject.toml[cite: 1]
                sh 'pytest tests/'
            }
        }
    }
}
