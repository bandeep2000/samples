node {
    stage('Example') {
        if (env.BRANCH_NAME == 'master') {
            echo 'I only execute on the master branch'
            sh 'echo $GIT_COMMIT'
            
        } else {
            echo 'I execute elsewhere'
            sh 'echo $GIT_COMMIT'
            sh 'echo $env.GIT_COMMIT'
            sh 'echo $BRANCH_NAME'
            sh 'printenv'
        }
    }
}
