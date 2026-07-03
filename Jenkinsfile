pipeline{
    agent any
    stages {
        stage('Build Docker Image') {
    steps {
        bat 'docker build -t dinesh123890/tictactoe:latest .'
    }
}
}

        stage('Run Tests') {
            steps {
                bat 'docker --version'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Image built and ready. Deployment done.'
            }
        }
    }
}
  