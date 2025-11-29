#!/bin/bash

echo "========================================"
echo "  GESTOR DE MENU - RESTAURANTE"
echo "========================================"
echo ""

echo "Activando entorno virtual..."
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
else
    echo "ADVERTENCIA: No se encontro el entorno virtual"
    echo "Ejecuta ./install.sh primero"
    exit 1
fi
echo ""

echo "Iniciando aplicacion..."
python main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: La aplicacion termino con errores"
fi
