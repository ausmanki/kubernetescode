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
    sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=2f1e31bb799cb73e3f476523b4e8d12740b766f8 -Dsonar.sources=. -Dsonar.password=demo123"     
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
