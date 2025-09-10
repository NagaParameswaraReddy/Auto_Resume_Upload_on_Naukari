
pipeline {
    agent any

    environment {
        NAUKRI_USERNAME = credentials('na_param')
        NAUKRI_PASSWORD = credentials('na_pass')
        RESUME_PATH = r'C:\Users\india\Desktop\Devops\Resume\NAGA_PARAMESWARA_REDDY.pdf'

        EMAIL_RECIPIENT = 'snagaparameswarareddy@gmail.com'
        EMAIL_SUBJECT_SUCCESS = 'Naukri Resume Upload SUCCESS'
        EMAIL_SUBJECT_FAIL = 'Naukri Resume Upload FAILED'
    }

    triggers {
        cron('*/2 * * * *') // Every 2 minutes for testing
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/NagaParameswaraReddy/Auto_Resume_Upload_on_Naukari.git'
            }
        }

        stage('Run Selenium Script') {
            steps {
                echo "Starting Naukri resume update..."
                bat 'python "%WORKSPACE%\\naukri_resume_update.py"'
            }
        }
    }

    post {
        success {
            echo "✅ Jenkins pipeline completed successfully."
            mail bcc: '', body: "Resume upload script executed successfully.", 
                 subject: "${EMAIL_SUBJECT_SUCCESS}", to: "${EMAIL_RECIPIENT}"
        }
        failure {
            echo "❌ Jenkins pipeline failed. Check logs for errors."
            mail bcc: '', body: "Resume upload script failed. Check Jenkins logs.", 
                 subject: "${EMAIL_SUBJECT_FAIL}", to: "${EMAIL_RECIPIENT}"
        }
    }
}
