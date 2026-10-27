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

        stage('Smoke test') {
            environment {
                DB_PASSWORD = credentials('db-password')
                COMPOSE = 'docker compose -p jenkins-ci -f compose.yaml -f compose.ci.yaml'
            }
            steps {
                sh '$COMPOSE up -d --build --wait'
                sh 'docker run --rm --network jenkins-ci_default curlimages/curl -f --retry 5 --retry-connrefused --retry-delay 2 http://app:8000/health'
                sh 'docker run --rm --network jenkins-ci_default curlimages/curl -f http://app:8000/visitas'
            }
            post {
                failure {
                    sh '$COMPOSE logs'
                }
                always {
                    sh '$COMPOSE down -v'
                }
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