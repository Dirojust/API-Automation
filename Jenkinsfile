pipeline {
    agent any

    stages {
        stage('Python version') {
            steps {
                bat 'python -V'
            }
        }
        stage('Setup virtualenv') {
            steps {
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && python -m pytest src/api -v -s --alluredir=reports/allure/allure-results'
            }
        }
        stage('Allure Report') {
            steps {
                allure([
                    results: [[path: 'reports/allure/allure-results']],
                    reportBuildPolicy: 'ALWAYS'
                ])
            }
        }
    }
}