# 📘 Guía Completa de Instalación y Ejecución

Este documento detalla paso a paso cómo configurar, instalar y ejecutar el **Sistema de Gestión de Menú Distribuido** en un entorno híbrido (Windows y Linux).

---

## 🛠️ Prerrequisitos Globales

Antes de comenzar, asegúrese de tener instalado lo siguiente:

1.  **Python 3.10 o superior**: [Descargar aquí](https://www.python.org/downloads/).
    *   *Nota:* En Windows, asegúrese de marcar "Add Python to PATH" durante la instalación.
2.  **MySQL Server**: Para la base de datos del backend.
3.  **VirtualBox + Extension Pack 7.2.4**: Requerido si va a ejecutar el cliente Linux en una máquina virtual e imprimir.
    *   Es **CRUCIAL** descargar e instalar el "Oracle VM VirtualBox Extension Pack" versión **7.2.4** (o la que coincida exactamente con su versión de VirtualBox) desde la [web oficial](https://www.virtualbox.org/wiki/Downloads).
    *   Esto habilita el soporte para controladores USB 2.0 y 3.0 necesarios para la impresora.

---

## 🖥️ PARTE 1: Servidor (Backend) - Windows

El servidor debe ejecutarse en la máquina principal (Host) que alojará la base de datos.

### 1. Instalación
1.  Abra una terminal (PowerShell o CMD) y navegue a la carpeta `Backend`.
2.  Ejecute el script de instalación automática:
    ```cmd
    install.bat
    ```
    *Esto creará el entorno virtual e instalará las dependencias.*

### 2. Base de Datos
1.  Asegúrese de que el servicio MySQL esté corriendo.
2.  Importe el esquema de la base de datos:
    ```cmd
    mysql -u root -p < database/restaurante.sql
    ```
3.  Configure las credenciales en el archivo `.env` (se crea automáticamente tras ejecutar `install.bat`, si no, copie `.env.example` a `.env`).

### 3. Configuración de Red y Firewall
Para permitir que otros clientes (Linux o Windows) se conecten:

1.  **Perfil de Red (IMPORTANTE):**
    *   Asegúrese de que su conexión Wi-Fi o Ethernet esté configurada como **Red Privada** y no Pública.
    *   *Configuración > Red e Internet > Wi-Fi > (Su Red) > Tipo de perfil de red > Privada.*
    *   *Si está en "Pública", Windows bloqueará las conexiones entrantes de la VM aunque configure el firewall.*

2.  Ejecute el script de configuración del firewall **como Administrador**:
    ```cmd
    configure_firewall.bat
    ```
    *Esto abre el puerto 5000 (TCP) en el Firewall de Windows.*

### 4. Ejecución
Inicie el servidor:
```cmd
start_server.bat
```
*Debe ver un mensaje indicando que el servidor corre en `http://0.0.0.0:5000`.*

---

## 💻 PARTE 2: Cliente Windows (Frontend)

Para ejecutar la aplicación cliente en una PC con Windows (puede ser la misma del servidor u otra en la red).

### 1. Instalación
1.  Navegue a la carpeta `Frontend`.
2.  Ejecute el instalador:
    ```cmd
    install.bat
    ```

### 2. Configuración
1.  Abra el archivo `Frontend/.env` con un editor de texto.
2.  Configure la URL del backend segun sus circunstancias:
    *   **Misma PC:** `BACKEND_URL=http://localhost:5000`
    *   **Otra PC:** `BACKEND_URL=http://192.168.X.X:5000` (Reemplace con la IP del servidor (ipconfig IPv4 address)).

### 3. Ejecución
Inicie la aplicación:
```cmd
run_app.bat
```

---

## 🐧 PARTE 3: Cliente Linux (Frontend en VirtualBox)

Pasos específicos para ejecutar el cliente en una Máquina Virtual (Fedora/Ubuntu) y habilitar la impresión física.

### 1. Configuración de VirtualBox (Antes de iniciar la VM)
1.  **Red (Networking):**
    *   Vaya a *Configuración > Red*.
    *   Conectado a: **Adaptador Puente (Bridged Adapter)**.
    *   *Esto permite que la VM tenga su propia IP en la red local y vea al servidor Windows.*
2.  **USB (Impresión):**
    *   Asegúrese de haber instalado el **Extension Pack 7.2.4**.
    *   Vaya a *Configuración > USB*.
    *   Marque la casilla **"Habilitar controlador USB"**.
    *   Seleccione **Controlador USB 2.0 (EHCI)** o **Controlador USB 3.0 (xHCI)** (Recomendado si su puerto es azul).
    *   Agregue un filtro (+) y seleccione su impresora física (ej. Canon, HP).
    *   *Esto desconectará la impresora de Windows y la conectará directamente a Linux cuando la VM esté activa.*


### 2. Instalación en Linux
Abra una terminal en Linux y navegue a la carpeta del proyecto `Frontend`.

1.  Dé permisos de ejecución a los scripts:
    ```bash
    chmod +x install.sh run_app.sh
    ```
2.  Ejecute el instalador:
    ```bash
    ./install.sh
    ```

### 3. Configuración
1.  Edite el archivo `.env`:
    ```bash
    nano .env
    ```
2.  Establezca la IP del servidor Windows (Host):
    ```env
    BACKEND_URL=http://192.168.X.X:5000
    ```
    *(Use `ipconfig` en Windows para averiguar esta IP).*

### 4. Ejecución
Inicie la aplicación:
```bash
./run_app.sh
```

---

## ❓ Solución de Problemas Comunes

### 🔴 No se conecta al Backend
1.  **Verifique la IP:** Asegúrese de que la IP en `.env` sea correcta.
2.  **Ping:** Desde el cliente, intente hacer ping al servidor: `ping 192.168.X.X`.
    *   Si falla, revise que ambos dispositivos estén en la misma red (o que la VM esté en modo Puente).
3.  **Firewall:** Verifique que el puerto 5000 esté abierto en el servidor Windows. Puede desactivar temporalmente el firewall para probar.

### 🖨️ La impresora no aparece en Linux
1.  **Extension Pack:** Verifique que esté instalado en VirtualBox (Archivo > Herramientas > Paquetes de extensión).
2.  **Usuario:** En Linux, su usuario debe pertenecer al grupo `lp` o `vboxusers`.
    ```bash
    sudo usermod -aG lp $USER
    ```
3.  **Captura:** Asegúrese de que VirtualBox haya capturado el dispositivo USB (icono de USB en la barra inferior de la ventana de la VM).

### 📄 La impresión sale cortada o pequeña
*   El sistema usa un escalado lógico automático. Asegúrese de que el tamaño de papel en la configuración de impresión del sistema operativo (CUPS en Linux o Dispositivos en Windows) coincida con el papel físico (Carta/A4).
