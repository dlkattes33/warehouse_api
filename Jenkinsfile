pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = "docker-compose.yml".toString()
        PATH = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests - warehouse_api') {
            steps {
                sh '''
                    export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    export PYTHONPATH=$WORKSPACE
                    pytest -q --maxfail=1 --disable-warnings --junitxml=warehouse_api-tests.xml .
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
                        export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        export PYTHONPATH=$(pwd)
                        pytest -q --maxfail=1 --disable-warnings --junitxml=temp_service-tests.xml .
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
                    export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                    docker compose -f docker-compose.yml build
                '''
            }
        }

        stage('Integration - Up') {
            steps {
                sh '''
                    export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                    docker compose -f docker-compose.yml up -d
                '''
                sh 'sleep 10'
            }
        }

        stage('Integration Tests') {
            steps {
                sh '''
                    export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                    curl -f http://localhost:8000/ || exit 1
                    curl -f http://localhost:8001/temperatures/freezer || exit 1
                '''
            }
        }

    } // <-- this closes the stages block

    post {
        always {
            sh '''
                export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                docker compose -f docker-compose.yml down || true
            '''
        }
    }
}