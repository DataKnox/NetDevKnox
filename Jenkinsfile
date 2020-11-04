pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
          sh "printenv | sort"
          sh '$WORKSPACE/Build/startnodes.sh'
        
      }
    }

    stage('Test') {
      steps {
       
          sh '$WORKSPACE/Test/testscript.sh'
        
      }
    }

  }
}
