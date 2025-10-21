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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Running Pytest with Selenium...'
                bat 'pytest --html=reports/report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                echo '📊 Publishing test results...'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report'
                ])
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning workspace...'
            cleanWs()
        }
        success {
            echo '🎉 Build successful!'
        }
        failure {
            echo '❌ Build failed. Check logs.'
        }
    }
}
