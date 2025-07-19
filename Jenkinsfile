pipeline {
  agent any

  environment {
    IMAGE_NAME = "small-api"
    VERSION = "1.0.${BUILD_NUMBER}"
    REGISTRY = "192.168.150.167:8083"
    IMAGE_FULL = "${REGISTRY}/${IMAGE_NAME}:${VERSION}"
    IMAGE_LATEST = "${REGISTRY}/${IMAGE_NAME}:latest"
  }

  stages {
    stage('Build Docker image') {
      steps {
        echo "Сборка ${IMAGE_FULL} началась!"
        sh "docker build -t ${IMAGE_FULL} ."
      }
    }

    stage('Login to Nexus') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'nexus-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh "echo \$PASS | docker login ${REGISTRY} -u \$USER --password-stdin"
        }
      }
    }

    stage('Push Docker image') {
      steps {
        sh "docker push ${IMAGE_FULL}"
      }
    }

    stage('Tag latest') {
      steps {
        sh "docker tag ${IMAGE_FULL} ${IMAGE_LATEST}"
        sh "docker push ${IMAGE_LATEST}"
      }
    }
  }
}
