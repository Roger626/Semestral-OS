# 📚 Índice de Documentación - Backend Restaurante

Bienvenido al backend de la aplicación de restaurante. Aquí encontrarás toda la documentación necesaria para usar, configurar y mantener el proyecto.

---

## 🚀 Inicio rápido

**¿Primera vez aquí? Comienza con estos pasos:**

1. **[QUICK_START.md](QUICK_START.md)** ⭐
   - Guía paso a paso para poner en marcha el backend
   - Checklist completo de configuración
   - Solución de problemas comunes

---

## 📖 Documentación principal

### Para desarrolladores

- **[README.md](README.md)**
  - Descripción general del proyecto
  - Características implementadas
  - Instalación detallada
  - Estructura del proyecto
  - Tecnologías utilizadas

- **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)**
  - Documentación completa de todos los endpoints
  - Ejemplos de uso con cURL, JavaScript y Python
  - Códigos de estado HTTP
  - Esquemas de request/response

- **[FRONTEND_INTEGRATION.md](FRONTEND_INTEGRATION.md)**
  - Ejemplos de integración con frontend
  - Código para React, Vue, Vanilla JS
  - Servicio completo reutilizable
  - Manejo de errores robusto

### Para configuración

- **[CLOUDINARY_SETUP.md](CLOUDINARY_SETUP.md)**
  - Guía paso a paso para configurar Cloudinary
  - Cómo obtener credenciales
  - Características del plan gratuito
  - Solución de problemas

- **[.env.example](.env.example)**
  - Plantilla de variables de entorno
  - Todas las configuraciones necesarias

---

## 🛠️ Scripts útiles

### Windows Batch Scripts

| Script | Descripción | Uso |
|--------|-------------|-----|
| `install.bat` | Instalación automática completa | Ejecutar una vez al inicio |
| `start_server.bat` | Inicia el servidor backend | Ejecutar cada vez que quieras usar la API |
| `test_api.bat` | Prueba todos los endpoints | Ejecutar para verificar funcionamiento |
| `configure_firewall.bat` | Configura firewall para acceso remoto | Ejecutar como administrador |

### Python Scripts

| Script | Descripción |
|--------|-------------|
| `test_api.py` | Suite completa de pruebas de la API |
| `public/api.py` | Aplicación principal Flask |

---

## 📁 Estructura de archivos

```
Backend/
├── 📂 controller/           # Lógica de negocio y validaciones
│   └── menuController.py
├── 📂 database/             # Scripts SQL
│   └── restaurante.sql
├── 📂 model/                # Modelos de datos
│   └── menuModel.py
├── 📂 public/               # Punto de entrada de la API
│   └── api.py
├── 📂 utils/                # Utilidades y configuraciones
│   ├── conexion.py
│   └── cloudinary_config.py
│
├── 📄 .env                  # Variables de entorno (NO SUBIR A GIT)
├── 📄 .env.example          # Ejemplo de variables de entorno
├── 📄 .gitignore            # Archivos ignorados por Git
│
├── 📘 README.md             # Documentación principal
├── 📘 QUICK_START.md        # Guía de inicio rápido
├── 📘 API_DOCUMENTATION.md  # Documentación de la API
├── 📘 CLOUDINARY_SETUP.md   # Configuración de Cloudinary
├── 📘 FRONTEND_INTEGRATION.md # Integración con frontend
├── 📘 INDEX.md              # Este archivo
│
├── 📜 requirements.txt      # Dependencias Python
├── 📜 test_api.py           # Script de pruebas
│
├── ⚙️ install.bat           # Script de instalación
├── ⚙️ start_server.bat      # Script para iniciar servidor
├── ⚙️ test_api.bat          # Script para probar API
└── ⚙️ configure_firewall.bat # Script para configurar firewall
```

---

## 🎯 Guías por tarea

### Quiero instalar el proyecto
→ Lee **[QUICK_START.md](QUICK_START.md)** sección "Pasos para poner en marcha"
→ Ejecuta `install.bat`

### Quiero configurar Cloudinary
→ Lee **[CLOUDINARY_SETUP.md](CLOUDINARY_SETUP.md)**
→ Edita el archivo `.env` con tus credenciales

### Quiero iniciar el servidor
→ Ejecuta `start_server.bat`
→ Verifica en `http://localhost:5000/health`

### Quiero conectar desde otra computadora
→ Lee **[QUICK_START.md](QUICK_START.md)** sección "Acceso remoto"
→ Ejecuta `configure_firewall.bat` como Administrador
→ Obtén tu IP con `ipconfig`
→ Conecta desde el frontend usando `http://<TU_IP>:5000`

### Quiero integrar con mi frontend
→ Lee **[FRONTEND_INTEGRATION.md](FRONTEND_INTEGRATION.md)**
→ Usa los ejemplos de código según tu framework

### Quiero ver los endpoints disponibles
→ Lee **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)**
→ Ejecuta `test_api.bat` para ver ejemplos funcionando

### Tengo un error
→ Revisa **[QUICK_START.md](QUICK_START.md)** sección "Solución de problemas"
→ Verifica el checklist en la misma guía

---

## 🔍 Búsqueda rápida

### Por tema

- **Instalación**: QUICK_START.md, README.md, install.bat
- **Configuración**: QUICK_START.md, CLOUDINARY_SETUP.md, .env.example
- **API**: API_DOCUMENTATION.md
- **Frontend**: FRONTEND_INTEGRATION.md
- **Cloudinary**: CLOUDINARY_SETUP.md
- **Seguridad**: README.md (sección Seguridad), API_DOCUMENTATION.md
- **Errores**: QUICK_START.md (Solución de problemas)
- **Acceso remoto**: QUICK_START.md (Acceso desde otra computadora)

### Por archivo de código

- **Aplicación Flask**: `public/api.py`
- **Controlador**: `controller/menuController.py`
- **Modelo**: `model/menuModel.py`
- **Base de datos**: `utils/conexion.py`, `database/restaurante.sql`
- **Cloudinary**: `utils/cloudinary_config.py`
- **Pruebas**: `test_api.py`

---

## 📊 Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Estado del servidor |
| GET | `/menu` | Lista todos los platos |
| GET | `/menu/{id}` | Obtiene un plato |
| POST | `/menu` | Crea un plato |
| PUT | `/menu/{id}` | Actualiza un plato |
| DELETE | `/menu/{id}` | Elimina un plato |

Ver detalles completos en **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)**

---

## ✅ Checklist de configuración

Antes de usar el backend, asegúrate de:

- [ ] MySQL está corriendo
- [ ] Base de datos `restaurante` creada (importar `database/restaurante.sql`)
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Archivo `.env` configurado
- [ ] Credenciales de Cloudinary agregadas al `.env`
- [ ] Firewall configurado (si necesitas acceso remoto)
- [ ] Servidor iniciado (`start_server.bat`)
- [ ] API responde (`http://localhost:5000/health`)

---

## 🆘 ¿Necesitas ayuda?

### Orden recomendado de lectura

1. **QUICK_START.md** - Para configurar rápidamente
2. **API_DOCUMENTATION.md** - Para entender los endpoints
3. **FRONTEND_INTEGRATION.md** - Para conectar con tu frontend
4. **CLOUDINARY_SETUP.md** - Para configurar imágenes

### Recursos adicionales

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

## 📝 Notas importantes

⚠️ **Seguridad:**
- NUNCA subas el archivo `.env` a Git (ya está en `.gitignore`)
- Cambia `API_DEBUG=False` en producción
- Restringe CORS a dominios específicos en producción

⚠️ **Cloudinary:**
- Plan gratuito: 25GB de almacenamiento
- Obtén credenciales en [cloudinary.com](https://cloudinary.com)

⚠️ **Acceso remoto:**
- Asegúrate de que ambas computadoras estén en la misma red
- Configura el firewall para permitir el puerto 5000

---

## 🎉 ¡Listo!

Todo lo que necesitas saber está en esta documentación. Si tienes dudas, revisa primero **[QUICK_START.md](QUICK_START.md)**.

**¡Éxito con tu proyecto! 🚀**

---

_Última actualización: 28 de noviembre de 2025_
