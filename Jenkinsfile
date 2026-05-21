pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = "docker-compose.yml"
        PATH = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    }

    stages {

        stage('Unit Tests - warehouse_api') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    export PYTHONPATH=$PYTHONPATH:$(pwd)/tests
                    pytest tests --junitxml=warehouse_api-tests.xml
                '''
            }
            post {
                always {
                    junit testResults: 'warehouse_api-tests.xml', skipMarkingBuildUnstable: true
                }
            }
        }

        stage('Unit Tests - temperature_service') {
            steps {
                dir('temperature_service') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest tests --junitxml=temp_service-tests.xml
                    '''
                }
            }
            post {
                always {
                    junit testResults: 'temperature_service/temp_service-tests.xml', skipMarkingBuildUnstable: true                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker compose -f docker-compose.yml build
                '''
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
                sh '''
                    docker compose -f docker-compose.yml up -d
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
                    junit testResults: 'integration-tests.xml', skipMarkingBuildUnstable: true
                }
            }
        }

    }

    post {
        always {
            sh '''
                docker compose -f docker-compose.yml down || true
            '''
            junit testResults: '**/*.xml', skipMarkingBuildUnstable: true
        }
    }
}
