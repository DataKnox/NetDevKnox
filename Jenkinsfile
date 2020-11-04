pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        script{
          sh ./Build/startnodes.sh
        }
      }
    }

    stage('Test') {
      steps {
        script {
          sh ./Test/testscript.sh
        }
      }
    }

  }
}
