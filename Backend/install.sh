#!/bin/bash

echo "========================================"
echo "  INSTALACION DEL BACKEND - RESTAURANTE"
echo "========================================"
echo ""

echo "[1/5] Creando entorno virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo crear el entorno virtual"
    echo "Asegurate de tener Python 3.8 o superior instalado"
    echo ""
    echo "En Fedora ejecuta:"
    echo "  sudo dnf install python3 python3-pip python3-devel"
    exit 1
fi
echo "OK - Entorno virtual creado"
echo ""

echo "[2/5] Activando entorno virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo activar el entorno virtual"
    exit 1
fi
echo "OK - Entorno virtual activado"
echo ""

echo "[3/5] Actualizando pip..."
pip install --upgrade pip
echo ""

echo "[4/5] Instalando dependencias..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    echo ""
    echo "En Fedora, si hay errores con mysqlclient, ejecuta:"
    echo "  sudo dnf install mysql-devel gcc python3-devel"
    exit 1
fi
echo "OK - Dependencias instaladas"
echo ""

echo "[5/5] Verificando archivo .env..."
if [ ! -f .env ]; then
    echo "Creando archivo .env desde .env.example..."
    cp .env.example .env
    echo ""
    echo "IMPORTANTE: Edita el archivo .env con tus credenciales:"
    echo "  - Configuracion de base de datos (MySQL/MariaDB)"
    echo "  - Credenciales de Cloudinary"
    echo ""
else
    echo "OK - Archivo .env encontrado"
fi
echo ""

echo "========================================"
echo "  INSTALACION COMPLETADA"
echo "========================================"
echo ""
echo "SIGUIENTE PASO:"
echo "  1. Edita .env para configurar:"
echo "     - Base de datos (MySQL/MariaDB)"
echo "     - Cloudinary"
echo "  2. Importa la base de datos:"
echo "     mysql -u root -p < database/restaurante.sql"
echo ""
echo "Para iniciar el servidor ejecuta:"
echo "  ./start_server.sh"
echo ""
