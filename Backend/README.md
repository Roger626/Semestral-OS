# API Backend - Restaurante

Backend API REST para gestión de menú de restaurante con integración a Cloudinary para manejo de imágenes.

## 📋 Características

- ✅ API REST completa con Flask
- ✅ CRUD de platos del menú
- ✅ Integración con Cloudinary para almacenamiento de imágenes
- ✅ Conexión a MySQL con patrón Singleton
- ✅ Validaciones de seguridad (sanitización, validación de tipos)
- ✅ CORS habilitado para acceso remoto
- ✅ Inyección de dependencias
- ✅ Manejo robusto de errores

## 🚀 Instalación

### 🪟 Windows (Instalación rápida)

**Opción 1: Script automático**
```bash
.\install.bat
```

**Opción 2: Manual**
1. Crear entorno virtual:
   ```bash
   python -m venv venv
   ```
2. Activar entorno virtual:
   ```bash
   .\venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Copiar archivo de configuración:
   ```bash
   copy .env.example .env
   ```
5. Editar `.env` con tus credenciales
6. Importar base de datos:
   ```bash
   mysql -u root -p < database\restaurante.sql
   ```
7. Iniciar servidor:
   ```bash
   .\start_server.bat
   ```

### 🐧 Linux (Fedora/Ubuntu/Debian)

**Opción 1: Script automático**
```bash
chmod +x install.sh
./install.sh
```

**Opción 2: Manual**
1. Instalar dependencias del sistema (si es necesario):
   
   **Fedora:**
   ```bash
   sudo dnf install python3 python3-pip python3-devel mysql-devel gcc
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt install python3 python3-pip python3-venv libmysqlclient-dev build-essential
   ```

2. Crear entorno virtual:
   ```bash
   python3 -m venv venv
   ```

3. Activar entorno virtual:
   ```bash
   source venv/bin/activate
   ```

4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Copiar archivo de configuración:
   ```bash
   cp .env.example .env
   ```

6. Editar `.env` con tus credenciales:
   ```bash
   nano .env
   ```

7. Importar base de datos:
   ```bash
   mysql -u root -p < database/restaurante.sql
   ```

8. Iniciar servidor:
   ```bash
   chmod +x start_server.sh
   ./start_server.sh
   ```

### ⚙️ Configuración del archivo .env

Edita el archivo `.env` con tus credenciales:

```env
# Base de datos
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_PORT=3306
DB_NAME=restaurante

# Cloudinary (obtén las credenciales en https://cloudinary.com)
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret

# Servidor
API_HOST=0.0.0.0
API_PORT=5000
API_DEBUG=False
```

El servidor estará disponible en `http://localhost:5000`

## 📡 Endpoints de la API

### Health Check
```http
GET /health
```
Verifica el estado del servidor y la conexión a la base de datos.

### Obtener todos los platos
```http
GET /menu
```

**Respuesta exitosa:**
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "nombre": "Pizza Margherita",
      "precio": 12.99,
      "imagen_url": "https://res.cloudinary.com/...",
      "fecha_creacion": "2025-11-28"
    }
  ],
  "message": "OK"
}
```

### Obtener un plato por ID
```http
GET /menu/{id}
```

### Crear un nuevo plato
```http
POST /menu
Content-Type: application/json

{
  "nombre": "Pizza Margherita",
  "precio": 12.99,
  "imagen_url": "https://example.com/imagen.jpg"
}
```

**O con archivo de imagen:**
```http
POST /menu
Content-Type: multipart/form-data

nombre: Pizza Margherita
precio: 12.99
imagen: [archivo de imagen]
```

### Actualizar un plato
```http
PUT /menu/{id}
Content-Type: application/json

{
  "nombre": "Pizza Margherita Actualizada",
  "precio": 13.99,
  "imagen_url": "https://example.com/nueva-imagen.jpg"
}
```

### Eliminar un plato
```http
DELETE /menu/{id}
```

## 🔒 Validaciones de Seguridad

El controlador implementa las siguientes validaciones:

- ✅ Sanitización de strings (prevención XSS)
- ✅ Validación de tipos de datos
- ✅ Validación de rangos (precios, IDs)
- ✅ Validación de formatos de URL
- ✅ Validación de extensiones de archivos de imagen
- ✅ Límite de tamaño de archivos (16MB)
- ✅ Protección contra inyección SQL (uso de consultas parametrizadas)

## 🌐 Acceso Remoto

El servidor está configurado con `host='0.0.0.0'` para permitir conexiones desde otras computadoras en la red.

### 🪟 Windows

**Configurar firewall:**
```bash
.\configure_firewall.bat
```

**Manual:**
```powershell
New-NetFirewallRule -DisplayName "Backend Restaurante" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow
```

**Obtener IP:**
```bash
ipconfig
```

### 🐧 Linux

**Configurar firewall (Fedora/RHEL/CentOS):**
```bash
chmod +x configure_firewall.sh
./configure_firewall.sh
```

**Manual - Fedora (firewalld):**
```bash
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload
```

**Manual - Ubuntu/Debian (ufw):**
```bash
sudo ufw allow 5000/tcp
```

**Obtener IP:**
```bash
ip addr show
# o
hostname -I
```

### 📱 Acceso desde frontend

Desde otra computadora, usa la IP del servidor:
```
http://<IP_DEL_SERVIDOR>:5000/menu
```

**Ejemplo:**
Si la IP del servidor es `192.168.1.100`:
```
http://192.168.1.100:5000/menu
```

### 📋 Scripts disponibles

**Windows:**
- `install.bat` - Instalación automática
- `start_server.bat` - Iniciar servidor
- `test_api.bat` - Probar API
- `configure_firewall.bat` - Configurar firewall

**Linux:**
- `install.sh` - Instalación automática
- `start_server.sh` - Iniciar servidor
- `test_api.sh` - Probar API
- `configure_firewall.sh` - Configurar firewall

## 🗂️ Estructura del Proyecto

```
Backend/
├── controller/
│   └── menuController.py    # Controlador con validaciones
├── database/
│   └── restaurante.sql      # Script de base de datos
├── model/
│   └── menuModel.py         # Modelo de datos
├── public/
│   └── api.py              # Aplicación Flask y endpoints
├── utils/
│   ├── conexion.py         # Conexión a base de datos (Singleton)
│   └── cloudinary_config.py # Configuración de Cloudinary
├── .env.example            # Ejemplo de variables de entorno
├── .gitignore             # Archivos ignorados por git
├── requirements.txt       # Dependencias Python
└── README.md             # Este archivo
```

## 🛠️ Tecnologías

- **Flask** - Framework web
- **Flask-CORS** - Manejo de CORS
- **MySQL** - Base de datos
- **Cloudinary** - Almacenamiento de imágenes en la nube
- **python-dotenv** - Gestión de variables de entorno

## 📝 Notas Importantes

1. **Cloudinary**: Debes crear una cuenta en [cloudinary.com](https://cloudinary.com) para obtener las credenciales
2. **Producción**: En producción, cambia `API_DEBUG=False` y restringe los orígenes CORS
3. **Seguridad**: No subas el archivo `.env` al repositorio (ya está en `.gitignore`)
4. **Puerto 5000**: Asegúrate de que el puerto 5000 esté disponible o cambia `API_PORT` en `.env`

## 🐛 Troubleshooting

**Error de conexión a MySQL:**
- Verifica las credenciales en `.env`
- Asegúrate de que MySQL esté corriendo
- Verifica que la base de datos `restaurante` existe

**Error de Cloudinary:**
- Verifica las credenciales en `.env`
- Asegúrate de tener conexión a internet

**Error CORS desde frontend:**
- Verifica que CORS esté habilitado
- Comprueba que la URL del backend sea correcta

## 📄 Licencia

Este proyecto es de código abierto.
