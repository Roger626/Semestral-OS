#!/bin/bash

echo "========================================"
echo "  CONFIGURAR FIREWALL PARA ACCESO REMOTO"
echo "========================================"
echo ""
echo "Este script configurara el firewall para permitir"
echo "conexiones entrantes al puerto 5000"
echo ""
echo "IMPORTANTE: Requiere permisos de root/sudo"
echo ""

# Detectar el sistema de firewall
if command -v firewall-cmd &> /dev/null; then
    # Fedora/RHEL/CentOS con firewalld
    echo "Detectado: firewalld (Fedora/RHEL/CentOS)"
    echo ""
    
    read -p "¿Continuar? (s/n): " confirm
    if [ "$confirm" != "s" ] && [ "$confirm" != "S" ]; then
        echo "Operacion cancelada"
        exit 0
    fi
    
    echo ""
    echo "Agregando regla para el puerto 5000..."
    sudo firewall-cmd --permanent --add-port=5000/tcp
    
    if [ $? -eq 0 ]; then
        echo "Recargando firewall..."
        sudo firewall-cmd --reload
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "========================================"
            echo "  FIREWALL CONFIGURADO CORRECTAMENTE"
            echo "========================================"
            echo ""
            echo "Puerto 5000/tcp abierto para conexiones entrantes"
            echo ""
            echo "Verificar con:"
            echo "  sudo firewall-cmd --list-ports"
            echo ""
            echo "Para obtener tu IP local, ejecuta:"
            echo "  ip addr show"
            echo "  o"
            echo "  hostname -I"
            echo ""
            echo "Ejemplo de acceso desde otro dispositivo:"
            echo "  http://192.168.1.100:5000/menu"
            echo ""
            echo "Para eliminar la regla:"
            echo "  sudo firewall-cmd --permanent --remove-port=5000/tcp"
            echo "  sudo firewall-cmd --reload"
            echo ""
        else
            echo "ERROR: No se pudo recargar el firewall"
            exit 1
        fi
    else
        echo "ERROR: No se pudo agregar la regla al firewall"
        exit 1
    fi

elif command -v ufw &> /dev/null; then
    # Ubuntu/Debian con ufw
    echo "Detectado: ufw (Ubuntu/Debian)"
    echo ""
    
    read -p "¿Continuar? (s/n): " confirm
    if [ "$confirm" != "s" ] && [ "$confirm" != "S" ]; then
        echo "Operacion cancelada"
        exit 0
    fi
    
    echo ""
    echo "Agregando regla para el puerto 5000..."
    sudo ufw allow 5000/tcp
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "========================================"
        echo "  FIREWALL CONFIGURADO CORRECTAMENTE"
        echo "========================================"
        echo ""
        echo "Puerto 5000/tcp abierto para conexiones entrantes"
        echo ""
        echo "Verificar con:"
        echo "  sudo ufw status"
        echo ""
        echo "Para obtener tu IP local, ejecuta:"
        echo "  ip addr show"
        echo "  o"
        echo "  hostname -I"
        echo ""
        echo "Para eliminar la regla:"
        echo "  sudo ufw delete allow 5000/tcp"
        echo ""
    else
        echo "ERROR: No se pudo agregar la regla al firewall"
        exit 1
    fi

else
    echo "No se detecto firewalld ni ufw"
    echo ""
    echo "CONFIGURACION MANUAL:"
    echo ""
    echo "Fedora/RHEL/CentOS (firewalld):"
    echo "  sudo firewall-cmd --permanent --add-port=5000/tcp"
    echo "  sudo firewall-cmd --reload"
    echo ""
    echo "Ubuntu/Debian (ufw):"
    echo "  sudo ufw allow 5000/tcp"
    echo ""
    echo "Arch Linux (iptables):"
    echo "  sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT"
    echo "  sudo iptables-save > /etc/iptables/iptables.rules"
    echo ""
fi
