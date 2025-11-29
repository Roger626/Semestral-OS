@echo off
echo ========================================
echo   INSTALACION DEL BACKEND - RESTAURANTE
echo ========================================
echo.

echo [1/5] Creando entorno virtual...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: No se pudo crear el entorno virtual
    pause
    exit /b 1
)
echo OK - Entorno virtual creado
echo.

echo [2/5] Activando entorno virtual...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)
echo OK - Entorno virtual activado
echo.

echo [3/5] Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo OK - Dependencias instaladas
echo.

echo [4/5] Verificando archivo .env...
if not exist .env (
    echo ADVERTENCIA: No existe el archivo .env
    echo Copiando .env.example a .env...
    copy .env.example .env
    echo.
    echo IMPORTANTE: Edita el archivo .env con tus credenciales:
    echo   - Configuracion de base de datos
    echo   - Credenciales de Cloudinary
    echo.
) else (
    echo OK - Archivo .env encontrado
)
echo.

echo [5/5] Verificando base de datos...
echo IMPORTANTE: Asegurate de:
echo   1. Tener MySQL corriendo
echo   2. Crear la base de datos ejecutando: database\restaurante.sql
echo   3. Configurar las credenciales en el archivo .env
echo.

echo ========================================
echo   INSTALACION COMPLETADA
echo ========================================
echo.
echo Para iniciar el servidor ejecuta:
echo   start_server.bat
echo.
echo Para probar la API ejecuta:
echo   test_api.bat
echo.
pause
