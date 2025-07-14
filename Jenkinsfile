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
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        stage('Run Python Scripts') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && python -m pytest src/api -vs --alluredir reports/allure/allure-results --md-report --md-report-output md_report.md'
            }
        }
        stage('Run Behave Tests') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && behave -f allure_behave.formatter:AllureFormatter -o allure-results'
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
