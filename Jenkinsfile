def version
def stagingServers = ["10.112.86.169"]
pipeline {

  environment {
    APP_NAME = "tntest"
    STAGING_USER = "docker"
    STAGING_BASED_PATH = "/home/" + "$STAGING_USER"
    PACKAGE_NAME = "package_tntest"
    PACKAGE_PATH = "/nfs-package/" + "$APP_NAME"
    ARCHIVED_PKG = "$PACKAGE_NAME" + ".tgz"
    registry = "ke-registry.th.kerryexpress.com"
    registryUrl = "https://" + "$registry"
    image = "$registry" + "/" + "$APP_NAME" + ":"
    registryCredential = 'ke_registry'
  
  }

  agent none

  stages {
    stage ('Clone') {
      agent { label 'slave_linux'}
      steps {
        echo "Cloning from Git."
        git branch: 'master',
        credentialsId: 'gitlab_man',
        url: 'http://JSaetung:s_yPukyW_cNCZYA4eL2B@gitlab.th.kerryexpress.com/it-architecture/track-and-trace-api.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
            docker.build('playwright-python')
        }
      }
    }

    stage('Run Tests') {
      steps {
        script {
          docker.image('playwright-python').inside {
              sh 'pytest --html=output/report.html'
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
}
