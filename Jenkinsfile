pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
          sh "printenv | sort"
          sh '$WORKSPACE/startnodes.sh'
        
      }
    }

    stage('Test') {
      steps {
       
          sh '$WORKSPACE/testscript.sh'
        
      }
    }

  }
}
