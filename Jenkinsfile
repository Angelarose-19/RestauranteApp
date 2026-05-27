pipeline {
    agent any

    stages {

        stage('Clonar Repositorio') {
            steps {
                echo 'Clonando repositorio desde GitHub...'
                checkout scm
            }
        }

        stage('Verificar Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando dependencias...'
                bat 'pip install pytest'
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat 'python -m unittest tests.py -v'
            }
        }

        stage('Empaquetar') {
            steps {
                echo 'Empaquetando aplicacion...'
                bat 'python -m zipfile -c RestauranteApp.zip main.py modulos/'
                echo 'Artefacto generado: RestauranteApp.zip'
            }
        }

        stage('Despliegue Simulado') {
            steps {
                echo 'Desplegando en ambiente de staging...'
                echo 'Aplicacion desplegada exitosamente en staging!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado exitosamente!'
            archiveArtifacts artifacts: 'RestauranteApp.zip'
        }
        failure {
            echo 'Pipeline fallido. Revisar logs.'
        }
    }
}