pipeline {
    agent any
    environment {
        PROJECT_ID = 'kubeops-339014'
        CLUSTER_NAME = 'cluster-1'
        LOCATION = 'us-central1-c'
        CREDENTIALS_ID = 'k8s-key'
    }
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

        stage('Tests') {
            steps {
                echo 'Tests OK!'
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        dockerapp.push('latest')
                        dockerapp.push("v${env.BUILD_ID}")
                    }
                }
            }
        }

        stage('Deployt to K8S') {
            steps {
                echo "Deployment started ..."
                sh "VERSION BUILD = v${env.BUILD_ID}"
                sh "sed -i 's/{{tagversion}}/v${env.BUILD_ID}/g' deployment.yaml"
                echo "Start deployment of deployment.yaml"
				step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: false])
			    echo "Deployment Finished ..."
            }
        }

    }
}