pipeline {
    agent any

    environment {
        PYTHON = '"C:\\Users\\LENOVO 520 PENTIUM\\AppData\\Local\\Python\\bin\\python.exe"'
    }

    stages {

        stage('Clonar Repositorio') {
            steps {
                echo 'Clonando repositorio desde GitHub...'
                checkout scm
            }
        }

        stage('Verificar Python') {
            steps {
                bat "%PYTHON% --version"
            }
        }

        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando dependencias...'
                bat "%PYTHON% -m pip install pytest"
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat "%PYTHON% -m unittest tests.py -v"
            }
        }

        stage('Empaquetar') {
            steps {
                echo 'Empaquetando aplicacion...'
                bat "%PYTHON% -m zipfile -c RestauranteApp.zip main.py modulos/"
                echo 'Artefacto generado: RestauranteApp.zip'
            }
        }

       stage('Despliegue Staging') {
            steps {
               echo 'Iniciando despliegue en staging...'
               bat 'deploy.bat'
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