pipeline {
  agent any

  environment {
    IMAGE_NAME = "animal-api"
    VERSION = "1.0.${BUILD_NUMBER}" // Пример версионирования
    REGISTRY = "192.168.150.167:8083"
  }

  stages {
    stage('Build Docker image') {
      steps {
        sh "docker build -t ${REGISTRY}/docker/${IMAGE_NAME}:${VERSION} ."
      }
    }

    stage('Login to Nexus') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'nexus-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh "echo $PASS | docker login ${REGISTRY} -u $USER --password-stdin"
        }
      }
    }

    stage('Push Docker image') {
      steps {
        sh "docker push ${REGISTRY}/docker/${IMAGE_NAME}:${VERSION}"
      }
    }

    stage('Tag latest (optional)') {
      steps {
        sh "docker tag ${REGISTRY}/docker/${IMAGE_NAME}:${VERSION} ${REGISTRY}/docker/${IMAGE_NAME}:latest"
        sh "docker push ${REGISTRY}/docker/${IMAGE_NAME}:latest"
      }
    }
  }
}
