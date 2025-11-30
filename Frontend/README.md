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

- Python 3.10 o superior
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
Frontend/
├── main.py                    # Punto de entrada
├── ui/                        # Componentes UI
│   ├── main_window.py         # Ventana principal
│   ├── form_fields.py         # Formulario
│   ├── image_viewer.py        # Visor de imágenes
│   └── toolbar_actions.py     # Acciones CRUD
├── utils/                     # Utilidades
│   ├── api_client.py          # Cliente REST API ⭐
│   ├── print_manager.py       # Gestor de impresión 🖨️
│   ├── config.py              # Configuración
│   ├── validators.py          # Validadores
│   └── cloudinary_uploader.py # Subida de imágenes
├── styles/                    # Estilos visuales
│   ├── theme.py
│   └── colors.py
├── .env                       # Configuración (crear desde .env.example)
├── requirements.txt           # Dependencias Python
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

## 📚 Dependencias

- PyQt6 - Framework GUI
- requests - Cliente HTTP
- python-dotenv - Variables de entorno

---

**Desarrollado para el Proyecto Semestral de Sistemas Operativos.**
