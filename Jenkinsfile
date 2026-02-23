pipeline {
    agent any

    environment {
        DOCKER_CREDS = credentials('docker-creds')
        EMAIL_CREDS  = credentials('email-creds')
        IMAGE        = "gajendra1/cloud-native:latest"
    }

    stages {

        stage('Cleanup') {
            steps {
                sh '''
                    docker stop cloud-native || true
                    docker rm   cloud-native || true
                    docker rmi  $IMAGE       || true
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh '''
                    echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin
                    docker push $IMAGE
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run --name cloud-native -d -p 5000:5000 \
                      -v ~/.kube/config:/root/.kube/config \
                      -e EMAIL_USER=$EMAIL_CREDS_USR \
                      -e EMAIL_PASS=$EMAIL_CREDS_PSW \
                      $IMAGE
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl create namespace gajendra || true
                    kubectl apply -f deployment.yaml
                    kubectl rollout status deployment/cloud-native -n gajendra
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    echo "=== Docker Container ==="
                    docker ps | grep cloud-native

                    echo "=== Kubernetes Pods ==="
                    kubectl get pods -n gajendra

                    echo "=== Kubernetes Service ==="
                    kubectl get service -n gajendra

                    echo "Docker  --> http://EC2-IP:5000"
                    echo "Kubernetes --> http://EC2-IP:30500"
                '''
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed - check logs above'
        }
    }
}
```

