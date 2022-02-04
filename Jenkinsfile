pipeline {
    agent any

    stages {
        stage('Checkout Source') {
            steps {
                git url: 'https://github.com/ronaldofreitas/webapiflask.git', branch: 'main'
            }
        }

        stage('Build Image Docker') {
            steps {
                script {
                    dockerapp = docker.build("ronafreitasweb/webapiflask:v${env.BUILD_ID}",
                    '-f ./src/Dockerfile .')
                }
            }
        }

        stage('Push Image Docker') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                    dockerapp.push('latest')
                    dockerapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }

        stage('Deploy to GKE') {
            environment {
                tag_version = "${env.BUILD_ID}"
            }

            steps{
                sh 'sed -i "s/{{tag}}/$tag_version/g" ./deployment.yaml'
                //sh "sed -i 's/hello:latest/hello:${env.BUILD_ID}/g' deployment.yaml"
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
            }
        }

    }
}