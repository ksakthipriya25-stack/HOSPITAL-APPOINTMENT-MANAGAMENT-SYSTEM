pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Hospital Appointment Management System...'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Hospital Appointment Management System...'
                bat 'python hospital.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Hospital Appointment Management System...'
            }
        }
    }

    post {
        success {
            echo 'Hospital Appointment Management System deployed successfully.'
        }

        failure {
            echo 'Pipeline failed. Please check the console output.'
        }
    }
}
