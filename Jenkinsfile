pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = "docker-compose.yml"
    }

    stages {

        stage('Unit Tests - warehouse_api') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest tests --junitxml=warehouse_api-tests.xml
                '''
            }
            post { always { junit 'warehouse_api-tests.xml' } }
        }

        stage('Unit Tests - temperature_service') {
            steps {
                dir('temperature_service') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest tests --junitxml=temp_service-tests.xml
                    '''
                }
            }
            post { always { junit 'temperature_service/temp_service-tests.xml' } }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose -f docker-compose.yml build'
            }
        }

        stage('Cleanup Containers') {
            steps {
                sh '''
                    docker rm -f temperature_service || true
                    docker rm -f warehouse_api || true
                    docker compose -f docker-compose.yml down || true
                '''
            }
        }

        stage('Integration - Up') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d'
            }
        }

        stage('Wait for temperature_service') {
            steps {
                sh '''
                    echo "Waiting for temperature_service on localhost:8001..."
                    for i in {1..20}; do
                        if curl -s http://temperature_service:8001/temperatures/freezer > /dev/null; then
                            echo "temperature_service is UP!"
                            exit 0
                        fi
                        echo "Not ready yet... retrying"
                        sleep 1
                    done
                    echo "temperature_service did not become ready in time"
                    exit 1
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                sh '''
                    docker compose -f docker-compose.yml run --rm integration_tests
            '''
       }
         post {
             always {
                 junit 'integration-tests.xml'
                 }
             }
         }

    }

    post {
        always {
            sh 'docker compose -f docker-compose.yml down || true'
        }
    }
}
