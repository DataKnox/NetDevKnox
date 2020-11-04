pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        whoami
        sudo sh './Build/startnodes.sh'
      }
    }

    stage('Test') {
      steps {
        sudo sh './Test/testscript.sh'
      }
    }

  }
}
