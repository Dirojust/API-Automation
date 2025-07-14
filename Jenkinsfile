pipeline {
    agent any

    stages {
        stage('Python version') {
            steps {
                bat 'python --version'
            }
        }
        stage('Setup virtualenv and install deps') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install --force-reinstall -r requirements-behave.txt
                '''
            }
        }
        stage('Clean Reports') {
            steps {
                bat 'if exist reports\\allure\\allure-results (rmdir /s /q reports\\allure\\allure-results)'
                bat 'mkdir reports\\allure\\allure-results'
            }
        }
        stage('Run Behave Tests') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && python -m behave -f allure_behave.formatter:AllureFormatter -o reports\\allure\\allure-results'
            }
        }
        stage('Reports') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'reports/allure/allure-results']]
                ])
            }
        }
        stage('Send Report to Teams') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && python web_hook.py'
            }
        }
    }
}
