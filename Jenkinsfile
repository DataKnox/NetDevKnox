pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
          sh "printenv | sort"
          sh 'bash $WORKSPACE/Build/startnodes.sh'
        
      }
    }

    stage('Test') {
      steps {
       
          sh 'bash $WORKSPACE/Test/testscript.sh'
        
      }
    }

  }
}
