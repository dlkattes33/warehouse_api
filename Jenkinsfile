pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = "docker-compose.yml".toString()
        PATH = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
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
            post {
                always {
                    junit 'warehouse_api-tests.xml'
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
                        export PYTHONPATH=$(pwd)
                        pytest tests --junitxml=temp_service-tests.xml
                    '''
                }
            }
            post {
                always {
                    junit 'temperature_service/temp_service-tests.xml'
                }
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
                    docker compose -f docker-compose.yml up -d --build
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                sh '''
                    python3 -m venv venv                
                    .venv/bin/activate
                    pytest tests_integration \
                        --maxfail=1 \
                        --disable-warnings \
                        --junitxml=integration-tests.xml
                '''
            }
            post {
                always {
                    junit 'integration-tests.xml'
                }
            }
        }

    }   // <-- THIS closes the stages block

    post {
        always {
            sh '''
                docker compose -f docker-compose.yml down || true
            '''
        }
    }
}
