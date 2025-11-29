#!/bin/bash

echo "========================================"
echo "  INICIANDO SERVIDOR - RESTAURANTE API"
echo "========================================"
echo ""

# Activar entorno virtual
echo "Activando entorno virtual..."
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
else
    echo "ADVERTENCIA: No se encontro el entorno virtual"
    echo "El servidor se iniciara con Python global"
    echo ""
fi

# Obtener IP local
echo "Obteniendo IP local..."
if command -v ip &> /dev/null; then
    # Linux con comando ip
    IP=$(ip -4 addr show | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v 127.0.0.1 | head -1)
elif command -v hostname &> /dev/null; then
    # Alternativa con hostname
    IP=$(hostname -I | awk '{print $1}')
else
    IP="IP_NO_DETECTADA"
fi

echo ""
echo "========================================"
echo "  SERVIDOR INICIADO"
echo "========================================"
echo ""
echo "Acceso local:  http://localhost:5000"
echo "Acceso remoto: http://$IP:5000"
echo ""
echo "Health Check:  http://localhost:5000/health"
echo "Endpoints:     http://localhost:5000/menu"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo "========================================"
echo ""

# Cambiar al directorio del script
cd "$(dirname "$0")"

# Iniciar servidor
python3 public/api.py
