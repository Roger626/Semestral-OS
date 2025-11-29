# 🍽️ Frontend - Gestor de Menú Restaurante

Aplicación de escritorio para gestionar el menú de un restaurante con interfaz gráfica PyQt6 conectada a backend REST API.

## ✨ Características

- 📋 **CRUD completo** de platos del menú (conectado a backend)
- 🖼️ **Carga de imágenes** con drag & drop
- ☁️ **Almacenamiento en Cloudinary** (vía backend)
- 🔄 **Navegación** entre registros
- 🖨️ **Impresión** de fichas de platos
- 🌐 **Conexión con backend REST API**
- 💻 **Compatible con Windows y Linux**
- 🎨 **Interfaz moderna** tipo restaurante

## 🎨 Paleta de Colores

- **Primario**: `#8C4A33` (marrón gastronómico)
- **Crema**: `#D9B38C` (suave y cálido)
- **Beige**: `#F7E7CE` (elegante)
- **Texto oscuro**: `#3A2E2A` (legible)
- **Acento**: `#FFFFFF` (neutro)

---

## 🚀 Instalación Rápida

### Requisitos previos

- Python 3.8 o superior
- Backend REST API corriendo (ver `../Backend/README.md`)

### Windows

```bash
install.bat
```

### Linux (Fedora/Ubuntu/Debian)

```bash
chmod +x install.sh run_app.sh
./install.sh
```

---

## ⚙️ Configuración

### Configurar URL del Backend

Edita el archivo `.env`:

```env
# Misma computadora
BACKEND_URL=http://localhost:5000

# Otra computadora en la red
BACKEND_URL=http://192.168.1.100:5000  # Cambia por la IP del servidor
```

### Verificar conexión

```bash
python -m utils.api_client
```

Debe mostrar: `✓ Conexión exitosa con el backend`

---

## 🎮 Uso de la Aplicación

### Iniciar

**Windows:** `run_app.bat`
**Linux:** `./run_app.sh`

### Operaciones

1. **Agregar plato**: Llenar formulario → Arrastrar imagen → Clic "Agregar"
2. **Modificar**: Editar campos → Clic "Modificar"
3. **Eliminar**: Navegar al plato → Clic "Eliminar"
4. **Navegar**: Botones "◀ Anterior" y "Siguiente ▶"
5. **Imprimir**: Clic "🖨️ Imprimir" → Vista previa → Imprimir/PDF

### Impresión de Fichas

La aplicación incluye **funcionalidad completa de impresión** con:

- ✅ **Vista previa** del documento antes de imprimir
- ✅ **Detección automática** de impresoras (Windows/Linux)
- ✅ **Impresión con imágenes** (local o desde Cloudinary)
- ✅ **Formato profesional** en alta resolución
- ✅ **Exportar a PDF** (sin impresora física)

**Cómo usar:**
1. Selecciona un plato
2. Clic en **🖨️ Imprimir**
3. Se abrirá la **vista previa**
4. Desde ahí puedes:
   - Ver cómo se imprimirá
   - Imprimir en impresora física
   - Guardar como PDF
   - Configurar impresora/copias

📖 **Ver guía completa:** [PRINTING.md](PRINTING.md)

---

## 🔌 Conexión desde Otra Computadora

### Servidor (Backend)

1. Obtener IP: `ipconfig` (Windows) o `ip addr` (Linux)
2. Iniciar backend: `start_server.bat`
3. Configurar firewall: `configure_firewall.bat`

### Cliente (Frontend)

1. Editar `.env`:
   ```env
   BACKEND_URL=http://192.168.1.100:5000
   ```
2. Ejecutar `run_app.bat`

**Requisito:** Misma red WiFi/LAN

---

## 📁 Estructura

```
Frontent/
├── main.py                    # Punto de entrada
├── ui/                        # Componentes UI
│   ├── main_window.py         # Ventana principal
│   ├── form_fields.py         # Formulario
│   ├── image_viewer.py        # Visor de imágenes
│   └── toolbar_actions.py     # Acciones CRUD
├── utils/                     # Utilidades
│   ├── api_client.py          # Cliente REST API ⭐
│   ├── print_manager.py       # Gestor de impresión 🖨️
│   └── config.py              # Configuración
├── styles/                    # Estilos visuales
│   ├── theme.py
│   └── colors.py
├── .env                       # Configuración (crear desde .env.example)
├── requirements.txt           # Dependencias Python
├── README.md                  # Este archivo
├── PRINTING.md                # Guía de impresión 🖨️
└── QUICK_START.md             # Inicio rápido
│   ├── config.py              # Configuración
│   ├── validators.py          # Validadores
│   ├── cloudinary_uploader.py # Placeholder UI
│   └── print_manager.py       # Impresión
├── styles/                    # Estilos
│   ├── colors.py
│   └── theme.py
├── .env                       # Config (NO SUBIR A GIT)
├── .env.example               # Plantilla
├── requirements.txt           # Dependencias
├── install.bat / .sh          # Instalación
├── run_app.bat / .sh          # Ejecución
└── README.md                  # Este archivo
```

---

## 🐛 Solución de Problemas

### "No se pudo conectar con el servidor"

- ✅ Verificar que el backend esté corriendo
- ✅ Comprobar URL en `.env`
- ✅ Probar: `curl http://192.168.1.100:5000/health`

### "ModuleNotFoundError: PyQt6"

```bash
pip install -r requirements.txt
```

### No se conecta desde otra computadora

Checklist:
- [ ] Backend corriendo
- [ ] Firewall configurado
- [ ] Misma red
- [ ] IP correcta en `.env`
- [ ] Ping exitoso

---

## 🔐 Seguridad

- ❌ NO subir `.env` a repositorios
- ✅ Usar `.env.example` como plantilla

---

## 📚 Dependencias

- PyQt6 - Framework GUI
- requests - Cliente HTTP
- python-dotenv - Variables de entorno

---

## 🔗 Integración con Backend

Ver documentación completa:
- `../Backend/README.md` - Instalación backend
- `../Backend/API_DOCUMENTATION.md` - Endpoints
- `../Backend/FRONTEND_INTEGRATION.md` - Integración

---

**¡Listo para usar! 🎉**

## 📋 Características

- ✨ **Interfaz moderna y elegante** con tema gastronómico
- 📝 **CRUD completo** para platos del menú
- 🖼️ **Vista previa de imágenes** en tiempo real
- 📅 **Selector de fechas** con calendario
- 🔄 **Navegación** entre registros (anterior/siguiente)
- 🖨️ **Impresión** de fichas de platos
- ☁️ **Preparado para Cloudinary** (backend pendiente)
- 🎨 **Paleta de colores profesional** tipo restaurante

## 🎨 Paleta de Colores

- **Primario**: `#8C4A33` (marrón gastronómico)
- **Crema**: `#D9B38C` (suave y cálido)
- **Beige**: `#F7E7CE` (elegante)
- **Texto oscuro**: `#3A2E2A` (legible)
- **Acento**: `#FFFFFF` (neutro)

## 🏗️ Estructura del Proyecto

\`\`\`
gestor-menu-restaurante/
│
├── main.py                      # Punto de entrada
│
├── ui/                          # Interfaz de usuario
│   ├── main_window.py          # Ventana principal
│   ├── form_fields.py          # Campos del formulario
│   ├── image_viewer.py         # Vista previa de imágenes
│   └── toolbar_actions.py      # Botones CRUD y navegación
│
├── styles/                      # Estilos y temas
│   ├── colors.py               # Paleta de colores
│   └── theme.py                # Hojas de estilo Qt
│
├── utils/                       # Utilidades
│   ├── print_manager.py        # Gestor de impresión
│   ├── cloudinary_uploader.py  # Subida a Cloudinary (placeholder)
│   └── validators.py           # Validadores de datos
│
├── requirements.txt             # Dependencias Python
└── README.md                    # Este archivo
\`\`\`

## 🚀 Instalación

### Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. **Ejecutar la aplicación**

\`\`\`bash
python main.py
\`\`\`

## 💻 Uso

### Flujo de Trabajo

1. **Visualizar platos**: Al abrir la app, verás el primer plato registrado
2. **Navegar**: Usa los botones "Anterior" y "Siguiente" para moverte entre registros
3. **Agregar**: Completa el formulario y presiona "Agregar Nuevo Plato"
4. **Modificar**: Edita los campos y presiona "Modificar Plato Actual"
5. **Eliminar**: Presiona "Eliminar Plato" para borrar el registro actual
6. **Subir imagen**: Haz clic en "Subir Imagen" para seleccionar una foto del plato
7. **Imprimir**: Genera una ficha impresa del plato con "Imprimir Registro"

### Campos del Formulario

- **Nombre del Plato**: Texto libre (obligatorio)
- **Precio**: Número con decimales (obligatorio)
- **Fecha en menú**: Selector de calendario (obligatorio)
- **URL de Imagen**: Se genera automáticamente al subir a Cloudinary

## 🔌 Integración Backend (Pendiente)

Este es el **frontend completo**. Para hacerlo funcional, necesitas implementar:

### 1. Base de Datos

Crea una tabla `platos` con:
- `id` (INT, PRIMARY KEY, AUTO_INCREMENT)
- `nombre` (VARCHAR)
- `precio` (DECIMAL)
- `fecha_menu` (DATE)
- `imagen_url` (VARCHAR)

### 2. Cloudinary

- Registrarse en [Cloudinary](https://cloudinary.com/)
- Obtener credenciales (cloud_name, api_key, api_secret)
- Implementar lógica en `utils/cloudinary_uploader.py`

### 3. API/Backend

Conectar los métodos de `main_window.py`:
- `handle_add_record()` → INSERT en BD
- `handle_edit_record()` → UPDATE en BD
- `handle_delete_record()` → DELETE en BD
- `load_sample_data()` → SELECT de BD
- `handle_upload_image()` → Upload a Cloudinary

## 🎯 Características Técnicas

- **Framework**: PyQt6 (moderno y profesional)
- **Arquitectura**: Modular y escalable
- **Diseño**: Responsivo (1024x768 mínimo)
- **Compatibilidad**: Windows y Linux
- **Estilo**: Material Design adaptado a gastronomía

## 📝 Notas de Desarrollo

### Modificar Estilos

Edita `styles/colors.py` y `styles/theme.py` para personalizar la apariencia.

### Agregar Validaciones

Usa `utils/validators.py` para validar datos antes de enviarlos al backend.

### Debugging

Los botones imprimen mensajes en consola para facilitar el desarrollo:
- `🟢 ACCIÓN: Agregar nuevo plato`
- `🟡 ACCIÓN: Modificar plato actual`
- `🔴 ACCIÓN: Eliminar plato actual`
- `🖨️ ACCIÓN: Imprimir registro actual`

## 🤝 Contribuciones

Este es un proyecto de frontend standalone. Para añadir funcionalidades:

1. Implementa el backend de tu elección (FastAPI, Flask, Django, etc.)
2. Conecta con una base de datos (PostgreSQL, MySQL, SQLite)
3. Integra Cloudinary para almacenamiento de imágenes
4. Añade autenticación si es necesario

## 📄 Licencia

Este proyecto es de código abierto. Úsalo libremente para tus proyectos.

## 🆘 Soporte

Si necesitas ayuda:
1. Revisa los comentarios en el código
2. Verifica que las dependencias estén instaladas
3. Comprueba la versión de Python (>= 3.10)

---

**Desarrollado con ❤️ para restaurantes modernos**
