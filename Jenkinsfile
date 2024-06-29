def version
def stagingServers = ["10.112.86.169"]
pipeline {


  agent none

  environment {
   APP_IMAGE = "tnt-test"
  }


  stages {
    stage ('Clone') {
      agent { label 'slave_linux'}
      steps {
        echo "Cloning from Git."
        git branch: 'master',
        credentialsId: 'gitlab_man',
        url: 'http://SSiriprapasak:pVzMofdJzUikP4reo6W7@gitlab.th.kerryexpress.com/SSiriprapasak/tnt-test.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
            docker.build(APP_IMAGE)
        }
      }
    }
    stage('Run Tests') {
      steps {
          script {
              docker.image(APP_IMAGE).inside {
                  sh 'pytest app/test_example.py --html=/app/output/report.html'
              }
          }
      }
    }

    // stage("Run Tests") {
    //   agent {
    //     docker {
    //       image 'python:3.7.7-alpine3.11'
    //       label 'slave_linux'
    //     }
    //   }

    //   steps {
    //     withEnv(["HOME=${WORKSPACE}","PYTHONPATH=${WORKSPACE}:${WORKSPACE}/api:${WORKSPACE}/api/app:${WORKSPACE}/test:${WORKSPACE}/config"]) {
    //       echo "Running unit testing."
    //       sh 'rm -rf ${WORKSPACE}/log'
    //       sh 'mkdir -p ${WORKSPACE}/log'
    //       sh 'pip install -r requirements.txt'
    //       sh "python -m pytest ${WORKSPACE}/test/test_service.py --junitxml=${env.WORKSPACE}/test-coverage.xml --cov-config=.coveragerc --cov=api --cov-report=xml"
    //     }
    //   }
    }

}
