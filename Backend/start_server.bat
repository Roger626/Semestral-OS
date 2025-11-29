@echo off
echo ========================================
echo   INICIANDO SERVIDOR - RESTAURANTE API
echo ========================================
echo.

echo Activando entorno virtual...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo ADVERTENCIA: No se encontro el entorno virtual
    echo El servidor se iniciara con Python global
    echo.
)

echo Obteniendo IP local...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do set IP=%%a
set IP=%IP:~1%
echo.
echo ========================================
echo   SERVIDOR INICIADO
echo ========================================
echo.
echo Acceso local:  http://localhost:5000
echo Acceso remoto: http://%IP%:5000
echo.
echo Health Check:  http://localhost:5000/health
echo Endpoints:     http://localhost:5000/menu
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

cd /d "%~dp0"
python public\api.py