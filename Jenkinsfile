pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        /* -----------------------------
           UNIT TESTS: warehouse_api
        ------------------------------*/
        stage('Unit Tests - warehouse_api') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    export PYTHONPATH=$WORKSPACE
                    pytest -q --rootdir=. --junitxml=warehouse_api-tests.xml
                '''
            }
            post {
                always {
                    junit 'warehouse_api-tests.xml'
                }
            }
        }

        /* -----------------------------
           UNIT TESTS: temperature_service
        ------------------------------*/
        stage('Unit Tests - temperature_service') {
            steps {
                dir('temperature_service') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        export PYTHONPATH=$WORKSPACE
                        pytest -q --rootdir=. --junitxml=warehouse_api-tests.xml
                    '''
                }
            }
            post {
                always {
                    junit 'temperature_service/temp_service-tests.xml'
                }
            }
        }

        /* -----------------------------
           BUILD DOCKER IMAGES
        ------------------------------*/
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} build'
            }
        }

        /* -----------------------------
           INTEGRATION: Bring up stack
        ------------------------------*/
        stage('Integration - Up') {
            steps {
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                sh 'sleep 10'   // allow services to warm up
            }
        }

        /* -----------------------------
           INTEGRATION TESTS
        ------------------------------*/
        stage('Integration Tests') {
            steps {
                sh '''
                    curl -f http://localhost:8000/ || exit 1
                    curl -f http://localhost:8001/temperatures/freezer || exit 1
                '''
            }
        }
    }

    post {
        always {
            sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down || true'
        }
    }
}