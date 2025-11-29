# 🚀 GUÍA DE INICIO RÁPIDO - Backend Restaurante

## ✅ ¿Qué se ha implementado?

Tu backend está **100% completo** con las siguientes características:

### 🎯 Funcionalidades principales
- ✅ API REST completa con Flask
- ✅ CRUD completo de platos del menú
- ✅ Integración con Cloudinary para imágenes
- ✅ Conexión a MySQL con patrón Singleton
- ✅ CORS habilitado para acceso desde frontend remoto
- ✅ Validaciones de seguridad robustas
- ✅ Inyección de dependencias
- ✅ Manejo de errores completo

### 🔒 Seguridad implementada
- ✅ Sanitización de strings (prevención XSS)
- ✅ Validación de tipos de datos
- ✅ Protección contra inyección SQL
- ✅ Validación de URLs
- ✅ Límite de tamaño de archivos (16MB)
- ✅ Validación de extensiones de imagen
- ✅ Validación de rangos (precios, IDs)

---

## 📦 Pasos para poner en marcha el backend

### Paso 1: Instalar dependencias
```bash
# Opción A: Usar el script automático
install.bat

# Opción B: Manual
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Paso 2: Configurar base de datos
1. Asegúrate de tener MySQL corriendo
2. Importa el archivo `database/restaurante.sql`
   ```bash
   mysql -u root -p < database/restaurante.sql
   ```
   O usa phpMyAdmin / MySQL Workbench para importar

### Paso 3: Configurar variables de entorno
1. Edita el archivo `.env` con tus credenciales:
   ```env
   # Base de datos
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=tu_password
   DB_PORT=3306
   DB_NAME=restaurante
   
   # Cloudinary (ver CLOUDINARY_SETUP.md)
   CLOUDINARY_CLOUD_NAME=tu_cloud_name
   CLOUDINARY_API_KEY=tu_api_key
   CLOUDINARY_API_SECRET=tu_api_secret
   
   # Servidor
   API_HOST=0.0.0.0
   API_PORT=5000
   API_DEBUG=False
   ```

### Paso 4: Configurar Cloudinary
1. Crea una cuenta gratuita en [cloudinary.com](https://cloudinary.com)
2. Obtén tus credenciales del Dashboard
3. Actualiza el archivo `.env`
4. **Lee `CLOUDINARY_SETUP.md` para más detalles**

### Paso 5: Iniciar el servidor
```bash
# Opción A: Usar el script
start_server.bat

# Opción B: Manual
venv\Scripts\activate
python public/api.py
```

### Paso 6: Probar la API
```bash
# En otra terminal
test_api.bat

# O accede a http://localhost:5000/health en tu navegador
```

---

## 🌐 Acceso desde otra computadora (Frontend remoto)

### 1. Configurar firewall (Windows)
```bash
# Ejecutar como Administrador
configure_firewall.bat
```

Esto creará una regla para permitir conexiones entrantes al puerto 5000.

### 2. Obtener tu IP local
```bash
ipconfig
```
Busca la línea "Dirección IPv4" (ejemplo: 192.168.1.100)

### 3. Conectar desde el frontend
En tu aplicación frontend, usa la IP del servidor:
```javascript
const API_URL = "http://192.168.1.100:5000";

// Ejemplo
fetch(`${API_URL}/menu`)
  .then(response => response.json())
  .then(data => console.log(data));
```

### 4. Verificar conectividad
Desde la computadora del frontend, abre el navegador:
```
http://192.168.1.100:5000/health
```

Si ves el mensaje "API de Restaurante funcionando correctamente", ¡todo está bien!

---

## 📁 Estructura de archivos

```
Backend/
├── controller/
│   └── menuController.py          # Controlador con validaciones
├── database/
│   └── restaurante.sql            # Script de base de datos
├── model/
│   └── menuModel.py               # Modelo de datos
├── public/
│   └── api.py                     # Aplicación Flask y endpoints
├── utils/
│   ├── conexion.py                # Conexión a base de datos
│   └── cloudinary_config.py       # Configuración de Cloudinary
├── .env                           # Variables de entorno (NO SUBIR A GIT)
├── .env.example                   # Ejemplo de variables
├── .gitignore                     # Archivos ignorados
├── requirements.txt               # Dependencias Python
├── README.md                      # Documentación principal
├── API_DOCUMENTATION.md           # Documentación de la API
├── CLOUDINARY_SETUP.md            # Guía de Cloudinary
├── QUICK_START.md                 # Esta guía
├── install.bat                    # Script de instalación
├── start_server.bat               # Script para iniciar servidor
├── test_api.bat                   # Script para probar API
├── configure_firewall.bat         # Script para configurar firewall
└── test_api.py                    # Tests de la API
```

---

## 📡 Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Verifica estado del servidor |
| GET | `/menu` | Obtiene todos los platos |
| GET | `/menu/{id}` | Obtiene un plato por ID |
| POST | `/menu` | Crea un nuevo plato |
| PUT | `/menu/{id}` | Actualiza un plato |
| DELETE | `/menu/{id}` | Elimina un plato |

**Ver `API_DOCUMENTATION.md` para detalles completos de cada endpoint**

---

## 🧪 Pruebas rápidas

### Usando el navegador
1. Health check: `http://localhost:5000/health`
2. Ver menú: `http://localhost:5000/menu`

### Usando cURL
```bash
# Obtener todos los platos
curl http://localhost:5000/menu

# Crear un plato
curl -X POST http://localhost:5000/menu \
  -H "Content-Type: application/json" \
  -d "{\"nombre\":\"Pizza\",\"precio\":12.99,\"imagen_url\":\"https://example.com/pizza.jpg\"}"
```

### Usando el script de pruebas
```bash
test_api.bat
```

---

## 📚 Documentación

- **README.md** - Guía completa de instalación y uso
- **API_DOCUMENTATION.md** - Documentación detallada de todos los endpoints
- **CLOUDINARY_SETUP.md** - Guía paso a paso para configurar Cloudinary
- **QUICK_START.md** - Esta guía de inicio rápido

---

## ⚠️ Checklist antes de usar

- [ ] MySQL está corriendo
- [ ] Base de datos `restaurante` existe (importar `database/restaurante.sql`)
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Archivo `.env` configurado con credenciales correctas
- [ ] Cuenta de Cloudinary creada y credenciales en `.env`
- [ ] Firewall configurado (si necesitas acceso remoto)
- [ ] Servidor iniciado (`start_server.bat`)
- [ ] API responde correctamente (`http://localhost:5000/health`)

---

## 🔧 Solución de problemas

### Error: "Conexión a base de datos fallida"
- ✅ Verifica que MySQL esté corriendo
- ✅ Comprueba las credenciales en `.env`
- ✅ Asegúrate de que la base de datos `restaurante` existe

### Error: "Invalid Cloudinary credentials"
- ✅ Verifica las credenciales en `.env`
- ✅ No debe haber espacios antes/después de los valores
- ✅ Reinicia el servidor después de cambiar `.env`

### Error: "Address already in use"
- ✅ El puerto 5000 ya está en uso
- ✅ Cambia `API_PORT` en `.env` (ejemplo: 5001)
- ✅ O cierra la aplicación que usa el puerto 5000

### No puedo conectar desde otra computadora
- ✅ Verifica que el firewall permita el puerto 5000
- ✅ Ejecuta `configure_firewall.bat` como Administrador
- ✅ Asegúrate de usar la IP correcta del servidor
- ✅ Ambas computadoras deben estar en la misma red

### Imágenes no se suben a Cloudinary
- ✅ Verifica conexión a internet
- ✅ Comprueba las credenciales de Cloudinary
- ✅ Asegúrate de que el archivo sea menor a 16MB
- ✅ Formato de imagen válido (PNG, JPG, JPEG, GIF, WEBP)

---

## 🎉 ¡Listo!

Tu backend está completo y listo para conectarse con tu frontend. 

**Próximos pasos:**
1. Inicia el servidor: `start_server.bat`
2. Prueba los endpoints: `test_api.bat`
3. Conecta tu frontend usando la IP del servidor
4. ¡Comienza a desarrollar! 🚀

---

## 📞 Recursos adicionales

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [CORS Explanation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

**¡Éxito con tu proyecto! 🎊**
