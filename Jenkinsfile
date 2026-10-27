pipeline {
    agent any

    environment {
        IMAGE = "devops-lab-app:jenkins-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Info') {
            steps {
                sh 'env | sort'
            }
        }
        
        stage('Lint') {
            steps {
                sh 'docker run --rm --volumes-from jenkins -w "$WORKSPACE" --user "$(id -u):$(id -g)" ghcr.io/astral-sh/ruff check'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build --pull -t "$IMAGE" .'
            }
        }

        stage('Security scan') {
            steps {
                sh '''
                    docker run --rm \
                      -v /var/run/docker.sock:/var/run/docker.sock \
                      aquasec/trivy image \
                      --exit-code 1 \
                      --severity HIGH,CRITICAL \
                      --ignore-unfixed \
                      "$IMAGE"
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rmi "$IMAGE" || true'
        }
    }
}