pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo "📦 Checking out code from GitHub..."
                git branch: 'main', url: 'https://github.com/Bhav885/python-tests.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "🐍 Installing Python dependencies..."
                // Upgrade pip
                bat 'python -m pip install --upgrade pip'
                // Install requirements from requirements.txt
                bat 'pip install -r Guru99BankAutomation/requirements.txt'
                // Ensure pytest-html is installed for HTML reports
                bat 'pip install pytest-html'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Running Selenium tests with Pytest...'
                // Create reports folder if it doesn't exist
                bat 'if not exist reports mkdir reports'
                // Run tests with HTML report
                bat 'python -m pytest Guru99BankAutomation/tests/ --html=reports/report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                echo "📄 Publishing test report..."
                publishHTML([
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
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
            echo '✅ Build and tests succeeded!'
        }
        failure {
            echo '❌ Build failed. Check logs.'
        }
    }
}
