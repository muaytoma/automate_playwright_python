pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'git_url'  // Change this to your repository URL
        GIT_BRANCH = 'master'  // Change this to your branch
        PYTHONPATH = ".:${env.WORKSPACE}"  // Add the workspace to the PYTHONPATH
    }
    stages {

        stage('Checkout Code') {
            steps {
                // Checkout code from GitHub
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO_URL}", credentialsId: 'github-token'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh '''
                pip install -r requirements.txt
                python -m playwright install
                '''
            }
        }
        stage('Run E2E Tests') {
            steps {
                // Run Playwright tests with pytest
                sh '''
            
                export PYTHONPATH=$PYTHONPATH:$(pwd)
                pytest tests/test_search.py --maxfail=1 --disable-warnings -v --junitxml=test-results/results.xml || true
                '''
            }
        }
        stage('Archive Test Results') {
            steps {
                // Archive the test results
                junit 'test-results/results.xml'
            }
        }
    }
    post {
        always {
            // Archive artifacts
            archiveArtifacts artifacts: 'test-results/results.xml', allowEmptyArchive: true
        }
        cleanup {
            // Clean workspace after build
            cleanWs()
        }
    }
}
