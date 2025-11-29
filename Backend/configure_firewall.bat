@echo off
echo ========================================
echo   CONFIGURAR FIREWALL PARA ACCESO REMOTO
echo ========================================
echo.
echo Este script creara una regla en el firewall de Windows
echo para permitir conexiones entrantes al puerto 5000
echo.
echo IMPORTANTE: Debes ejecutar este script como Administrador
echo.
pause
echo.

echo Creando regla de firewall...
netsh advfirewall firewall add rule name="API Restaurante Backend - Puerto 5000" dir=in action=allow protocol=TCP localport=5000

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   FIREWALL CONFIGURADO CORRECTAMENTE
    echo ========================================
    echo.
    echo Ahora otros dispositivos en tu red pueden acceder a la API
    echo.
    echo Para obtener tu IP local, ejecuta: ipconfig
    echo Busca la linea "Direccion IPv4"
    echo.
    echo Ejemplo de acceso desde otro dispositivo:
    echo   http://192.168.1.100:5000/menu
    echo.
    echo Para eliminar la regla del firewall, ejecuta:
    echo   netsh advfirewall firewall delete rule name="API Restaurante Backend - Puerto 5000"
    echo.
) else (
    echo.
    echo ========================================
    echo   ERROR AL CONFIGURAR FIREWALL
    echo ========================================
    echo.
    echo Asegurate de ejecutar este script como Administrador:
    echo   1. Click derecho en el archivo
    echo   2. Selecciona "Ejecutar como administrador"
    echo.
)

pause
