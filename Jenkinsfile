pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-app"  
        IMAGE_TAG = "latest" 
        DOCKERHUB_ID = "cathalina" 
        REGISTRY_CREDENTIALS = "docker-hub-credentials"  
        APP_EXPOSED_PORT = "5002"                        // Port exposé de l'application
        INTERNAL_PORT = "8180"                           // Port interne du conteneur
    }

    stages {
        // Étape de récupération du code depuis Git
        stage('Checkout Code') {
            steps {
                git credentialsId: 'git-credentials', url: 'https://github.com/CathalinaRanaivoarison/Jenkins.git', branch: 'main' 
            }
        }

        // Étape de construction de l'image Docker
        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        // Construit l'image Docker en utilisant le Dockerfile du répertoire courant
                        docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                    } catch (Exception e) {
                        error "Échec de la construction de l'image Docker: ${e.getMessage()}"
                    }
                }
            }
        }

        // Étape de linting du code avec Flake8
        //stage('Lint Code') {
        //    steps {
        //        sh 'flake8 .'  // Exécute Flake8 pour vérifier le code
        //    }
        // }

        // Étape d'exécution du conteneur basé sur l'image construite
        stage('Run container based on built image') {
            agent any
            steps {
                script {
                    sh '''
                        echo "Cleaning existing container if it exists"
                        docker ps -a | grep -i $IMAGE_NAME && docker rm -f $IMAGE_NAME
                        docker run --name $IMAGE_NAME -d -p $APP_EXPOSED_PORT:$INTERNAL_PORT $IMAGE_NAME:$IMAGE_TAG
                        sleep 5
                    '''
                }
            }
        }

        // Étape de test de l'image Docker
        stage('Test image') {
            agent any
            steps {
                script {
                    sh '''
                        curl -v http://host.docker.internal:$APP_EXPOSED_PORT
                    '''
                }
            }
        }
        // curl -v http://localhost:$APP_EXPOSED_PORT

        // Étape de nettoyage du conteneur après les tests
        stage('Clean container') {
            agent any
            steps {
                script {
                    sh '''
                        docker stop $IMAGE_NAME
                        docker rm $IMAGE_NAME
                    '''
                }
            }
        }

        // Étape de push de l'image sur Docker Hub
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${REGISTRY_CREDENTIALS}") {
                        def appImage = docker.image("${DOCKERHUB_ID}/${IMAGE_NAME}:${IMAGE_TAG}")
                        appImage.push()
                        appImage.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        
    }
}
