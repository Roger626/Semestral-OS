@echo off
echo ========================================
echo   GESTOR DE MENU - RESTAURANTE
echo ========================================
echo.

echo Activando entorno virtual...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo ADVERTENCIA: No se encontro el entorno virtual
    echo Ejecuta install.bat primero
    pause
    exit /b 1
)
echo.

echo Iniciando aplicacion...
python main.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: La aplicacion termino con errores
    pause
)
