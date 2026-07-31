pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Hospital Appointment System') {
            steps {
                bat 'python hospital.py'
            }
        }
    }
}
