@echo off
echo === INICIANDO DESPLIEGUE ===
echo Verificando artefacto...
if not exist RestauranteApp.zip (
    echo ERROR - No se encontro RestauranteApp.zip
    exit /b 1
)
echo Copiando artefacto a servidor staging...
copy /Y RestauranteApp.zip C:\staging\
echo Verificando despliegue...
if exist C:\staging\RestauranteApp.zip (
    echo DESPLIEGUE EXITOSO - Aplicacion disponible en staging
) else (
    echo ERROR - Despliegue fallido
    exit /b 1
)
echo === DESPLIEGUE COMPLETADO ===