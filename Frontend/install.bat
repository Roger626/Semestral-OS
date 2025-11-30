@echo off
echo ========================================
echo   INSTALACION DEL FRONTEND - RESTAURANTE
echo ========================================
echo.

echo [1/4] Creando entorno virtual...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: No se pudo crear el entorno virtual
    echo Asegurate de tener Python 3.8 o superior instalado
    pause
    exit /b 1
)
echo OK - Entorno virtual creado
echo.

echo [2/4] Activando entorno virtual...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)
echo OK - Entorno virtual activado
echo.

echo [3/4] Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo OK - Dependencias instaladas
echo.

echo [4/4] Verificando archivo .env...
if not exist .env (
    echo Creando archivo .env desde .env.example...
    copy .env.example .env
    echo.
    echo IMPORTANTE: Edita el archivo .env para configurar:
    echo   - BACKEND_URL: URL del servidor backend
    echo   - Si el backend esta en otra computadora, usa: http://IP_SERVIDOR:5000
    echo.
) else (
    echo OK - Archivo .env encontrado
)
echo.

echo ========================================
echo   INSTALACION COMPLETADA
echo ========================================
echo.
echo CONFIGURACION:
echo   1. Edita .env para configurar la URL del backend
echo   2. Asegurate de que el backend este corriendo
echo.
echo Para iniciar la aplicacion ejecuta:
echo   run_app.bat
echo.
pause
