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
                    pip install --force-reinstall -r requirements-pytest.txt
                '''
            }
        }
        stage('Clean Reports') {
            steps {
                bat 'if exist reports\\allure\\allure-results (rmdir /s /q reports\\allure\\allure-results)'
                bat 'mkdir reports\\allure\\allure-results'
            }
        }
        stage('Run Python Scripts') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && python -m pytest src/api -vs --alluredir reports/allure/allure-results --md-report --md-report-output md_report.md'
            }
        }
        stage('Run Behave Scripts') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && behave'
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
