pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Bandit') {
            steps {
                bat 'python -m pip install bandit'
            }
        }

        stage('Bandit Scan') {
            steps {
                bat 'bandit -r src/ -f json -o bandit-report.json'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'bandit-report.json',
                              allowEmptyArchive: true
        }
    }
}
