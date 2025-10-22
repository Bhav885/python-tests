pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/Bhav885/python-tests.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '🐍 Installing dependencies...'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r Guru99BankAutomation/requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Running Selenium tests with Pytest...'
                bat 'if not exist reports mkdir reports'
                bat 'python -m pytest Guru99BankAutomation/tests/ --html=reports/report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                echo '📊 Publishing HTML report...'
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report',
                    alwaysLinkToLastBuild: true,
                    keepAll: true
                ])
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning workspace after publishing report...'
        }
        success {
            echo '🎉 Build successful!'
        }
        failure {
            echo '❌ Build failed. Check logs.'
        }
    }
}
