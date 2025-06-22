pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        REPORT_DIR = 'reports'
    }

    stages {
        stage('📥 Checkout') {
            steps {
                checkout scm
            }
        }

        stage('🐍 Set Up Python VirtualEnv') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install --upgrade pip'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('🚀 Start Appium & Emulator') {
            steps {
                echo '⚙️ Make sure emulator and Appium server are started manually or via a different job.'
            }
        }

        stage('🧪 Run Pytest') {
            steps {
                sh '.venv/bin/pytest tests/test_search_product.py --html=reports/report.html --self-contained-html || true'
            }
        }

        stage('📊 Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo '✅ Job Finished'
        }

        failure {
            echo '❌ Job Failed'
            // Optional safe email block (remove if not configured):
            // mail to: 'you@example.com', subject: 'Jenkins Job Failed', body: "Job URL: ${env.BUILD_URL}"
        }
    }
}
