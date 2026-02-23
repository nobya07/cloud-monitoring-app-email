pipeline {
    agent any

    environment {
        DOCKER_USER = credentials('docker-user')
        DOCKER_PASS = credentials('docker-pass')
        IMAGE       = "gajendra1/cloud-native:latest"
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

        stage('Push') {
            steps {
                sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run --name cloud-native -d -p 5000:5000 \
                      -v ~/.kube/config:/root/.kube/config \
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
                    kubectl get pods    -n gajendra
                    kubectl get service -n gajendra
                    echo "App running at http://$(curl -s ifconfig.me):5000"
                '''
            }
        }

    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed — check logs above'
        }
    }
}
```

