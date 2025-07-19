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
        sh "echo Сборка ${IMAGE_FULL} началась!"
        sh "docker build -t ${IMAGE_FULL} ."
      }
    }

  stage('Docker Push') {
    steps {
      withCredentials([usernamePassword(credentialsId: 'nexus-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
        sh """
          echo "Logging in to $REGISTRY as \$USER"
          echo "\$PASS" | docker login $REGISTRY -u "\$USER" --password-stdin

          echo "Pushing image: $IMAGE_FULL"
          docker push $IMAGE_FULL

          echo "Tagging image as latest"
          docker tag $IMAGE_FULL $IMAGE_LATEST

          echo "Pushing image: $IMAGE_LATEST"
          docker push $IMAGE_LATEST

          docker logout $REGISTRY
        """
      }
    }
  }
}
