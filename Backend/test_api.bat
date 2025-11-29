@echo off
echo ========================================
echo   PROBANDO API - RESTAURANTE
echo ========================================
echo.

echo Activando entorno virtual...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: No se pudo activar el entorno virtual
    echo Ejecuta install.bat primero
    pause
    exit /b 1
)
echo.

echo IMPORTANTE: Asegurate de que el servidor este corriendo
echo Ejecuta start_server.bat en otra ventana si no lo has hecho
echo.
pause
echo.

echo Ejecutando pruebas...
python test_api.py

echo.
pause
