# 🖨️ Guía de Impresión

Esta guía explica cómo usar la funcionalidad de impresión del Gestor de Menú para imprimir fichas de platos con vista previa.

## 📋 Características

- ✅ **Vista previa antes de imprimir** - Ve exactamente cómo se verá el documento
- ✅ **Detección automática de impresoras** - Detecta todas las impresoras conectadas
- ✅ **Impresión con imágenes** - Incluye la imagen del plato (local o desde Cloudinary)
- ✅ **Formato profesional** - Documento bien diseñado con encabezado, datos y pie de página
- ✅ **Multiplataforma** - Funciona en Windows y Linux
- ✅ **Alta calidad** - Impresión en alta resolución

## 🚀 Cómo Usar

### 1. Abrir la aplicación

Ejecuta el frontend:

**Windows:**
```bash
.\run_app.bat
```

**Linux:**
```bash
./run_app.sh
```

### 2. Seleccionar un plato

Navega por los platos usando los botones **Anterior** y **Siguiente**.

### 3. Imprimir

1. Haz clic en el botón **🖨️ Imprimir**
2. Se abrirá la **Vista Previa** del documento
3. Desde la vista previa puedes:
   - **Ver** cómo se imprimirá el documento
   - **Imprimir** usando el botón de la barra de herramientas
   - **Configurar** la impresora (elegir otra impresora, orientación, etc.)
   - **Cancelar** si no quieres imprimir

### 4. Configurar impresión

Desde la vista previa, haz clic en el icono de impresora o **Archivo → Imprimir** para:
- Seleccionar otra impresora
- Cambiar el número de copias
- Ajustar la orientación (Portrait/Landscape)
- Configurar calidad de impresión

## 📄 Contenido del Documento

El documento impreso incluye:

```
┌─────────────────────────────────────┐
│   🍽️ Menú del Restaurante          │
├─────────────────────────────────────┤
│                                     │
│ Nombre del Plato:                   │
│   Pizza Margherita                  │
│                                     │
│ Precio:                             │
│   $12.99                            │
│                                     │
│ En menú desde:                      │
│   2024-01-15                        │
│                                     │
│ Imagen del Plato:                   │
│   [IMAGEN 400x400]                  │
│                                     │
├─────────────────────────────────────┤
│ Gestor de Menú - Restaurante        │
│ Documento generado automáticamente  │
└─────────────────────────────────────┘
```

## 🖨️ Configuración de Impresoras

### Windows

#### Verificar impresoras instaladas

1. Abre **Configuración** → **Dispositivos** → **Impresoras y escáneres**
2. Verifica que tu impresora aparezca en la lista
3. Asegúrate de que esté **En línea** y no **Pausada**

#### Establecer impresora predeterminada

1. En **Impresoras y escáneres**, selecciona tu impresora
2. Clic en **Administrar**
3. Clic en **Establecer como predeterminada**

#### Imprimir a PDF (sin impresora física)

Windows incluye **Microsoft Print to PDF**:
1. En la vista previa, clic en **Imprimir**
2. Selecciona **Microsoft Print to PDF**
3. Elige la ubicación donde guardar el PDF

### Linux (Fedora/Ubuntu)

#### Verificar impresoras instaladas

**Fedora:**
```bash
lpstat -p -d
```

**Ubuntu/Debian:**
```bash
lpstat -p -d
```

#### Instalar CUPS (sistema de impresión)

**Fedora:**
```bash
sudo dnf install cups cups-client
sudo systemctl start cups
sudo systemctl enable cups
```

**Ubuntu/Debian:**
```bash
sudo apt install cups cups-client
sudo systemctl start cups
sudo systemctl enable cups
```

#### Configurar impresora

1. Abre el navegador: http://localhost:631
2. Ve a **Administration** → **Add Printer**
3. Sigue el asistente para agregar tu impresora

#### Imprimir a PDF (sin impresora física)

**Opción 1: CUPS-PDF**
```bash
# Fedora
sudo dnf install cups-pdf

# Ubuntu/Debian
sudo apt install cups-pdf
```

Después, selecciona **CUPS-PDF** como impresora. Los PDF se guardan en `~/PDF/`

**Opción 2: Print to File**
En el diálogo de impresión, selecciona **Print to File** y elige formato PDF.

## 🔍 Detección de Impresoras

La aplicación detecta automáticamente:

1. **Todas las impresoras instaladas** en el sistema
2. **Impresora predeterminada** (se selecciona automáticamente)
3. **Estado de las impresoras** (disponibles/no disponibles)

En la consola verás algo como:

```
====================================================
📄 PREPARANDO DOCUMENTO PARA IMPRESIÓN
====================================================
Nombre del Plato: Pizza Margherita
Precio: $12.99
Fecha en menú: 2024-01-15
Imagen local: C:\Users\...\pizza.jpg

🖨️  Impresoras disponibles: 3
   1. HP LaserJet (Predeterminada)
   2. Canon Pixma
   3. Microsoft Print to PDF
====================================================
```

## 📝 Formato del Documento

### Especificaciones técnicas

- **Tamaño de página:** Letter (8.5" x 11")
- **Orientación:** Vertical (Portrait)
- **Resolución:** Alta resolución (HighResolution mode)
- **Márgenes:** 50 puntos en todos los lados
- **Imagen:** Máximo 400x400 px, centrada, mantiene proporción

### Fuentes utilizadas

- **Título:** Arial 24pt Bold
- **Etiquetas:** Arial 12pt Bold
- **Datos:** Arial 11-18pt Normal
- **Pie de página:** Arial 9pt Normal

## 🐛 Solución de Problemas

### ❌ "No se detectaron impresoras"

**Windows:**
1. Verifica que tengas al menos una impresora instalada
2. Revisa que el servicio **Spooler de impresión** esté corriendo:
   - `services.msc` → Buscar "Spooler de impresión" → Iniciar
3. Instala **Microsoft Print to PDF** si no tienes impresora física

**Linux:**
1. Verifica que CUPS esté corriendo:
   ```bash
   sudo systemctl status cups
   ```
2. Instala CUPS si no está:
   ```bash
   # Fedora
   sudo dnf install cups
   
   # Ubuntu
   sudo apt install cups
   ```
3. Instala cups-pdf para imprimir a PDF:
   ```bash
   sudo dnf install cups-pdf  # Fedora
   sudo apt install cups-pdf  # Ubuntu
   ```

### ❌ "No se pudo inicializar la impresión"

**Causas comunes:**
- Impresora apagada o sin conexión
- Impresora en estado "Pausada"
- Problemas con el driver de la impresora

**Solución:**
1. Enciende la impresora
2. Verifica la conexión (USB o red)
3. Ve a configuración de impresoras y selecciona **Reanudar** si está pausada
4. Reinstala el driver de la impresora si es necesario

### ❌ "La imagen no aparece en el documento"

**Causas:**
- Ruta de imagen incorrecta
- URL de Cloudinary no válida
- Sin conexión a internet (para imágenes de Cloudinary)

**Solución:**
1. Verifica que el campo `image_path` o `image_url` tenga datos válidos
2. Si es URL de Cloudinary, verifica tu conexión a internet
3. La imagen se imprimirá si está disponible localmente primero

### ❌ "La vista previa está en blanco"

**Solución:**
1. Cierra la vista previa
2. Vuelve a hacer clic en **Imprimir**
3. Si persiste, verifica los datos del plato (nombre, precio, fecha)

## 🔧 Configuración Avanzada

### Cambiar tamaño de página

Edita `utils/print_manager.py`, línea ~48:

```python
# Cambiar de Letter a A4
printer.setPageSize(QPrinter.PageSize.A4)
```

Opciones: `Letter`, `A4`, `Legal`, `A5`, etc.

### Cambiar orientación

```python
# Cambiar a horizontal
printer.setPageOrientation(QPrinter.Orientation.Landscape)
```

### Ajustar tamaño de imagen

Edita `utils/print_manager.py`, línea ~170:

```python
# Cambiar tamaño máximo de imagen
max_image_size = 500  # Aumentar de 400 a 500
```

## 📚 Recursos Adicionales

### Documentación de PyQt6

- [QPrinter](https://doc.qt.io/qt-6/qprinter.html)
- [QPrintPreviewDialog](https://doc.qt.io/qt-6/qprintpreviewdialog.html)
- [QPainter](https://doc.qt.io/qt-6/qpainter.html)

### Sistemas de impresión

- **Windows:** [Microsoft Print Documentation](https://learn.microsoft.com/en-us/windows/win32/printdocs/printing-and-print-spooler)
- **Linux:** [CUPS Documentation](https://www.cups.org/documentation.html)

## 📊 Características Técnicas

| Característica | Soporte |
|----------------|---------|
| Vista previa | ✅ Sí |
| Impresoras físicas | ✅ Sí |
| Imprimir a PDF | ✅ Sí |
| Imágenes locales | ✅ Sí |
| Imágenes Cloudinary | ✅ Sí |
| Múltiples copias | ✅ Sí |
| Windows | ✅ Sí |
| Linux | ✅ Sí |
| macOS | ✅ Sí* |

*macOS debería funcionar pero no está probado.

## 💡 Consejos

1. **Siempre usa la vista previa** para verificar antes de imprimir
2. **Guarda como PDF** si solo necesitas el documento digital
3. **Verifica la impresora predeterminada** antes de imprimir
4. **Para imágenes grandes**, el sistema las escala automáticamente
5. **Sin conexión a internet** puedes imprimir si la imagen está guardada localmente

## 🎯 Flujo Recomendado

```
1. Seleccionar plato → 2. Clic en Imprimir → 3. Ver vista previa
                                                       ↓
                                            4. ¿Se ve bien?
                                                 ↙         ↘
                                            Sí             No
                                             ↓              ↓
                                    5. Imprimir    Cancelar/Ajustar
```

---

**¿Necesitas ayuda?** Revisa la sección de **Solución de Problemas** o consulta los logs en la consola.
