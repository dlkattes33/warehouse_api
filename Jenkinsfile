pipeline {
    agent {
        docker{
            image 'dkattes/warehouse-agent:latest'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

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
                    junit 'warehouse_api-tests.xml'
                    archiveArtifacts artifacts: 'warehouse_api-tests.xml', fingerprint: true
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
                    junit 'temperature_service/temp_service-tests.xml'
                    archiveArtifacts artifacts: 'temperature_service/temp_service-tests.xml', fingerprint: true
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose -f docker-compose.yml build'
            }
        }

        stage('Run Services') {
            steps {
                sh '''
                    docker compose up -d
                    sleep 5
                    curl -f http://host.docker.internal:8000/ || exit 1
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                sh '''
                    # Run tests WITHOUT --rm so we can copy the XML file
                    docker compose run integration_tests

                    # Find the actual container name created by docker compose
                    CONTAINER_ID=$(docker compose ps -q integration_tests)

                    # Copy the XML file out of the container
                    docker cp $CONTAINER_ID:/app/integration-tests.xml .

                    # Remove the container
                    docker rm -f $CONTAINER_ID
                '''
            }
            post {
                always {
                    junit 'integration-tests.xml'
                    archiveArtifacts artifacts: 'integration-tests.xml', fingerprint: true
                }
            }
        }

        stage('Cleanup Containers') {
            steps {
                sh '''
                    docker compose down --remove-orphans || true
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose down || true'
            junit '**/*.xml'
            archiveArtifacts artifacts: '**/*.xml', fingerprint: true
        }
    }
}
