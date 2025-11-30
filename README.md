# Sistema de Gestión de Menú Distribuido 🍽️

**Versión:** 1.0.0
**Tecnologías:** Python, PyQt6, Flask, MySQL, VirtualBox (Fedora Linux).

## 📋 Descripción General
Este sistema es una aplicación de escritorio distribuida bajo la arquitectura **Cliente-Servidor** diseñada para la gestión de menús en restaurantes. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los platos, sincronización en tiempo real entre múltiples terminales y generación de reportes impresos de alta fidelidad.

El sistema ha sido diseñado para operar en un entorno híbrido heterogéneo, conectando exitosamente clientes en **Windows** y **Linux (Fedora)** a un servidor centralizado.

---

## 🏗️ Arquitectura del Sistema

El sistema se divide en dos componentes lógicos principales que se comunican vía HTTP (REST API):

### 1. Backend (Servidor) 🖥️
*   **Ubicación:** `Backend/`
*   **Tecnología:** Python (Flask) + MySQL.
*   **Función:** Actúa como la fuente única de verdad. Gestiona la base de datos, procesa las reglas de negocio y sirve la API REST.
*   **Características Clave:**
    *   **API RESTful:** Endpoints estandarizados para gestión de platos.
    *   **Cloudinary:** Integración para almacenamiento de imágenes en la nube.
    *   **Concurrencia:** Servidor configurado (`threaded=True`) para manejar múltiples clientes simultáneamente.
    *   **Resiliencia:** Manejo inteligente de actualizaciones (detecta "0 cambios" como éxito).

### 2. Frontend (Cliente) 💻
*   **Ubicación:** `Frontend/`
*   **Tecnología:** Python (PyQt6).
*   **Función:** Interfaz gráfica de usuario (GUI) para interactuar con el sistema.
*   **Características Clave:**
    *   **Multi-plataforma:** Código único compatible con Windows y Linux.
    *   **Sincronización en Tiempo Real:** Implementa un sistema de *polling* (hilo secundario `QThread`) que consulta cambios cada 3 segundos.
    *   **Actualización Inteligente:** Solo refresca la UI si detecta diferencias en los datos, preservando la selección y el estado del usuario.
    *   **Módulo de Impresión Avanzado:** Renderizado de alta precisión independiente del dispositivo.

---

## 🚀 Instalación y Configuración

### Prerrequisitos
*   Python 3.10 o superior.
*   MySQL Server (para el Backend).
*   Conexión a Internet (para Cloudinary).

### 1. Configuración del Backend (Servidor)
1.  Navegue a la carpeta `Backend`.
2.  Instale las dependencias: `pip install -r requirements.txt`
3.  Configure el archivo `.env` con sus credenciales de base de datos y Cloudinary.
4.  Importe la base de datos ejecutando el script SQL en `database/restaurante.sql`.
5.  **Firewall:** Ejecute `configure_firewall.bat` (como Administrador) para permitir conexiones externas en el puerto 5000.
6.  Inicie el servidor: `python run.py`

### 2. Configuración del Frontend (Cliente)
1.  Navegue a la carpeta `Frontend`.
2.  Instale las dependencias: `pip install -r requirements.txt`
3.  Configure el archivo `.env`:
    *   Si está en la misma PC que el servidor: `BACKEND_URL=http://localhost:5000`
    *   Si está en otra PC: `BACKEND_URL=http://<IP_DEL_SERVIDOR>:5000` (Ej. `192.168.0.7:5000`)
4.  Inicie la aplicación: `python main.py`

---

## 📄 Informe Técnico: Módulo de Impresión y Red

### El Desafío de la Impresión (DPI) 🖨️
Uno de los mayores retos fue lograr que el diseño impreso se viera idéntico en pantalla y en papel, dado que las impresoras tienen una densidad de píxeles (DPI) mucho mayor (600-1200 DPI) que las pantallas (96 DPI).

**Solución Implementada: Sistema de Coordenadas Lógico**
Se desarrolló un motor de renderizado en `utils/print_manager.py` que abstrae la resolución física:
1.  **Viewport Físico:** Detecta el tamaño real del papel en píxeles de la impresora.
2.  **Ventana Lógica:** Define un lienzo virtual fijo de **816 unidades** de ancho (equivalente a una hoja carta estándar).
3.  **Transformación Automática:** Utiliza `painter.setWindow()` y `painter.setViewport()` para que Qt escale automáticamente todos los gráficos y textos.
4.  **Resultado:** Un diseño profesional de dos columnas (datos a la izquierda, imagen a la derecha) que se adapta perfectamente a cualquier impresora sin deformarse ni pixelarse.

### Infraestructura de Red Híbrida 🌐
El sistema conecta exitosamente tres nodos en una red local:

1.  **Servidor (Host Windows):** Laptop principal. IP Fija `192.168.0.7`.
2.  **Cliente Windows (Desktop):** PC externa conectada vía Wi-Fi/Ethernet.
3.  **Cliente Linux (Fedora VM):** Máquina virtual ejecutándose sobre el Host.

**Configuración Clave:**
*   **Red Privada:** Se configuró el perfil de red de Windows como "Privado" para permitir el descubrimiento.
*   **Modo Puente (Bridged):** La VM de Fedora se configuró con adaptador de red en modo Puente, permitiéndole obtener su propia IP en el rango `192.168.0.x` y ver al servidor directamente.

### Impresión desde Linux (Virtualización de Hardware) 🐧
Para permitir que la VM de Fedora imprimiera en la impresora física (Canon MG3000) conectada al Host Windows, se evitó la compleja configuración de red SMB/IPP.

**Solución: USB Pass-Through**
1.  Se instaló el **VirtualBox Extension Pack**.
2.  Se configuró un **Filtro USB** en la VM para capturar el dispositivo Canon.
3.  Al conectar la impresora, VirtualBox la desconecta de Windows y la conecta directamente a Linux.
4.  Fedora detecta la impresora como un dispositivo local USB, permitiendo el uso de drivers nativos y eliminando problemas de permisos de red.

---

## 📂 Estructura del Proyecto

```
Semestral-OS/
├── Backend/                 # Código del Servidor
│   ├── controller/          # Lógica de control
│   ├── database/            # Scripts SQL
│   ├── model/               # Modelos de datos
│   ├── public/              # Entry point API
│   ├── utils/               # Utilidades (Cloudinary)
│   ├── run.py               # Script de inicio
│   └── ...
│
├── Frontend/                # Código del Cliente
│   ├── ui/                  # Interfaz Gráfica (Ventanas, Widgets)
│   ├── utils/               # Lógica cliente (API, Impresión)
│   ├── styles/              # Estilos y Temas
│   ├── main.py              # Script de inicio
│   └── ...
│
└── README.md                # Documentación principal
```

---
**Desarrollado para el Proyecto Semestral de Sistemas Operativos.**
