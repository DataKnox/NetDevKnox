pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        
          sh './Build/startnodes.sh'
        
      }
    }

    stage('Test') {
      steps {
       
          sh './Test/testscript.sh'
        
      }
    }

  }
}
