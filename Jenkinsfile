pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
          sh "printenv | sort"
          sh 'bash $WORKSPACE/startnodes.sh'
        
      }
    }

    stage('Test') {
      steps {
       
          sh 'bash $WORKSPACE/testscript.sh'
        
      }
    }

  }
}
