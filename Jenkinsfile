
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
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install bandit'
            }
        }

        stage('Bandit Scan') {
            steps {
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts\\bandit.exe" -r src/ -f json -o bandit-report.json'
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
