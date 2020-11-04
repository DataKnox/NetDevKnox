pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo $(whoami)
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
