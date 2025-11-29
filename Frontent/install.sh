#!/bin/bash

echo "========================================"
echo "  INSTALACION DEL FRONTEND - RESTAURANTE"
echo "========================================"
echo ""

echo "[1/4] Creando entorno virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo crear el entorno virtual"
    echo "Asegurate de tener Python 3.8 o superior instalado"
    exit 1
fi
echo "OK - Entorno virtual creado"
echo ""

echo "[2/4] Activando entorno virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo activar el entorno virtual"
    exit 1
fi
echo "OK - Entorno virtual activado"
echo ""

echo "[3/4] Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi
echo "OK - Dependencias instaladas"
echo ""

echo "[4/4] Verificando archivo .env..."
if [ ! -f .env ]; then
    echo "Creando archivo .env desde .env.example..."
    cp .env.example .env
    echo ""
    echo "IMPORTANTE: Edita el archivo .env para configurar:"
    echo "  - BACKEND_URL: URL del servidor backend"
    echo "  - Si el backend esta en otra computadora, usa: http://IP_SERVIDOR:5000"
    echo ""
else
    echo "OK - Archivo .env encontrado"
fi
echo ""

echo "========================================"
echo "  INSTALACION COMPLETADA"
echo "========================================"
echo ""
echo "CONFIGURACION:"
echo "  1. Edita .env para configurar la URL del backend"
echo "  2. Asegurate de que el backend este corriendo"
echo ""
echo "Para iniciar la aplicacion ejecuta:"
echo "  ./run_app.sh"
echo ""
