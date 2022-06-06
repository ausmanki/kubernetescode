node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
       
      customImage = docker.build("my-image:${env.BUILD_ID}")
       app = docker.build("ausmanki/test")
        }

    stage('SonarQube') {
    
    def scannerHome = tool 'SonarScanner 4.0';
    withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=demo -Dsonar.sources=.-Dsonar.login=admin -Dsonar.password=demo123"     
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
