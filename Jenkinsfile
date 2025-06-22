pipeline {
    agent any

    environment {
        PYTHON_ENV = "${WORKSPACE}/.venv/bin"
    }

    stages {
        stage('📥 Checkout') {
            steps {
                git 'https://github.com/Gokulakrishnan24/amazon-appium-pytest.git'
            }
        }

        stage('🐍 Set Up Python VirtualEnv') {
            steps {
                sh '''
                    python3 -m venv .venv
                    source .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('🚀 Start Appium & Emulator') {
            steps {
                sh '''
                    nohup appium --log appium.log &
                    emulator -avd YOUR_AVD_NAME -no-snapshot-load -no-audio -no-boot-anim &
                    adb wait-for-device
                    sleep 30
                '''
            }
        }

        stage('🧪 Run Pytest') {
            steps {
                sh '''
                    source .venv/bin/activate
                    pytest tests/test_search_product.py \
                        --html=reports/report.html \
                        --self-contained-html || true
                '''
            }
        }

        stage('📊 Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/**/*.html', allowEmptyArchive: true
                archiveArtifacts artifacts: 'reports/screenshots/*.png', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo '✅ Job Finished'
        }
        failure {
            mail to: 'your-email@example.com',
                 subject: "❌ Jenkins Job Failed: ${env.JOB_NAME}",
                 body: "Job failed: ${env.BUILD_URL}"
        }
    }
}
