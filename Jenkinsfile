pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Deploy') {
            when {
                anyOf {
                    branch 'main'
                    branch pattern: 'release/.*', comparator: 'REGEXP'
                }
            }
            steps {
                echo "Simulating deploy from branch ${env.BRANCH_NAME}"
            }
        }
    }

    post {
        success {
            def payload = [
                content: "✅ Build SUCCESS on `${env.BRANCH_NAME}` \nURL: ${env.BUILD_URL}"
            ]
            httpRequest(
                httpMode: 'POST',
                contentType: 'APPLICATION_JSON',
                requestBody: groovy.json.JsonOutput.toJson(payload),
                url: 'https://discord.com/api/webhooks/1369194606712983612/Antgz7vjrCkz0R6LJNzEWKrjiJ3Y8-ZMzr1eWVu-5tF8kEQI86dvFh9l1oomMWgvZlzG'
            )
        }

        failure {
            def payload = [
                content: "❌ Build FAILED on `${env.BRANCH_NAME}` \nURL: ${env.BUILD_URL}"
            ]
            httpRequest(
                httpMode: 'POST',
                contentType: 'APPLICATION_JSON',
                requestBody: groovy.json.JsonOutput.toJson(payload),
                url: 'https://discord.com/api/webhooks/1369194606712983612/Antgz7vjrCkz0R6LJNzEWKrjiJ3Y8-ZMzr1eWVu-5tF8kEQI86dvFh9l1oomMWgvZlzG'
            )
        }
    }
}