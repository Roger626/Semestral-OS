#!/bin/bash

echo "========================================"
echo "  PROBANDO API - RESTAURANTE"
echo "========================================"
echo ""

# Activar entorno virtual
echo "Activando entorno virtual..."
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
else
    echo "ADVERTENCIA: No se encontro el entorno virtual"
    echo "Ejecuta ./install.sh primero"
    exit 1
fi
echo ""

echo "IMPORTANTE: Asegurate de que el servidor este corriendo"
echo "Ejecuta ./start_server.sh en otra terminal si no lo has hecho"
echo ""
read -p "Presiona Enter para continuar..."
echo ""

echo "Ejecutando pruebas..."
python3 test_api.py

echo ""
read -p "Presiona Enter para salir..."
