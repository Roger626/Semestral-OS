# 📄 Ejemplo de Documento Impreso

Este es un ejemplo visual de cómo se verá el documento impreso cuando uses el botón **🖨️ Imprimir**.

## Vista del Documento

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                  🍽️ Menú del Restaurante                   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Nombre del Plato:                                          │
│    Pizza Margherita                                         │
│                                                             │
│  Precio:                                                    │
│    $12.99                                                   │
│                                                             │
│  En menú desde:                                             │
│    2024-01-15                                               │
│                                                             │
│  Imagen del Plato:                                          │
│                                                             │
│    ┌───────────────────────────────────────┐               │
│    │                                       │               │
│    │         [IMAGEN DEL PLATO]            │               │
│    │         400x400 píxeles               │               │
│    │      Centrada, alta calidad           │               │
│    │                                       │               │
│    └───────────────────────────────────────┘               │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│     Gestor de Menú - Restaurante                           │
│     Documento generado automáticamente                     │
└─────────────────────────────────────────────────────────────┘
```

## Características del Documento

### Formato
- **Tamaño:** Letter (8.5" x 11" / 21.59 cm x 27.94 cm)
- **Orientación:** Vertical (Portrait)
- **Márgenes:** 50 puntos en todos los lados
- **Resolución:** Alta (HighResolution)

### Tipografía
- **Título principal:** Arial 24pt Bold
- **Etiquetas de campos:** Arial 12pt Bold
- **Nombre del plato:** Arial 18pt Normal
- **Precio:** Arial 16pt Bold (color verde oscuro)
- **Otros datos:** Arial 12pt Normal
- **Pie de página:** Arial 9pt Normal (color gris)

### Imagen
- **Tamaño máximo:** 400x400 píxeles
- **Posición:** Centrada
- **Borde:** 2px gris
- **Proporción:** Se mantiene el aspect ratio original
- **Calidad:** Alta resolución
- **Fuente:** Primero intenta cargar desde archivo local, luego desde Cloudinary

### Colores
- **Texto principal:** Negro
- **Precio:** Verde oscuro (#006400)
- **Borde imagen:** Gris (#808080)
- **Pie de página:** Gris (#808080)
- **Línea separadora:** Negro

## Flujo de Impresión

```
Usuario hace clic en 🖨️ Imprimir
           ↓
Sistema detecta impresoras disponibles
           ↓
Muestra en consola lista de impresoras
           ↓
Se abre ventana de Vista Previa
           ↓
Usuario puede ver el documento completo
           ↓
        Opciones:
    ┌────────┴────────┐
    ↓                 ↓
Imprimir          Cancelar
    ↓
Diálogo de impresión
(seleccionar impresora/copias)
    ↓
Documento enviado a impresora
```

## Información en Consola

Cuando haces clic en **Imprimir**, verás algo como esto en la consola:

```
====================================================
📄 PREPARANDO DOCUMENTO PARA IMPRESIÓN
====================================================
Nombre del Plato: Pizza Margherita
Precio: $12.99
Fecha en menú: 2024-01-15
Imagen local: C:\Users\...\pizza.jpg

🖨️  Impresoras disponibles: 6
   1. Microsoft Print to PDF (Predeterminada)
   2. HP LaserJet 1020
   3. Canon Pixma
   4. OneNote (Desktop)
   5. Wondershare PDFelement
   6. Fax

====================================================
📷 Cargando imagen desde: C:\Users\...\pizza.jpg
✅ Imagen cargada desde Cloudinary
📄 Documento renderizado correctamente
✅ Vista previa cerrada - El usuario pudo imprimir desde la vista previa
```

## Casos de Uso

### 1. Imprimir en Papel (Impresora Física)

```
Vista Previa → Toolbar: Icono Impresora → Seleccionar impresora física → OK
```

Resultado: Documento físico impreso en papel

### 2. Guardar como PDF

```
Vista Previa → Toolbar: Icono Impresora → Seleccionar "Microsoft Print to PDF" → OK → Elegir ubicación
```

Resultado: Archivo PDF guardado en disco

### 3. Solo Vista Previa (No Imprimir)

```
Vista Previa → Ver documento → Cerrar (X)
```

Resultado: No se imprime nada, solo se visualizó

## Controles de la Vista Previa

La ventana de vista previa incluye una **barra de herramientas** con:

- 🖨️ **Imprimir**: Abre diálogo para seleccionar impresora
- 📄 **Página**: Navegar entre páginas (si hay múltiples)
- 🔍 **Zoom**: Acercar/alejar vista previa
- 🖼️ **Ajustar**: Ajustar a página/ancho
- ⚙️ **Configurar**: Configuración de página
- ❌ **Cerrar**: Cancelar impresión

## Escenarios Especiales

### Sin Imagen

Si el plato no tiene imagen asignada:

```
┌─────────────────────────────────────────┐
│   🍽️ Menú del Restaurante              │
├─────────────────────────────────────────┤
│ Nombre del Plato:                       │
│   Pizza Margherita                      │
│                                         │
│ Precio:                                 │
│   $12.99                                │
│                                         │
│ En menú desde:                          │
│   2024-01-15                            │
│                                         │
│ [No se incluye sección de imagen]      │
├─────────────────────────────────────────┤
│ Gestor de Menú - Restaurante           │
└─────────────────────────────────────────┘
```

### Imagen Desde Cloudinary

Si la imagen está en Cloudinary (no local):

1. Sistema intenta cargar desde `image_path` (local) → Falla
2. Sistema descarga desde `image_url` (Cloudinary) → Éxito
3. Imagen se incluye en el documento

**Consola:**
```
📷 Descargando imagen desde: https://res.cloudinary.com/...
✅ Imagen cargada desde Cloudinary
```

### Sin Conexión a Internet

Si la imagen está en Cloudinary pero no hay internet:

1. Sistema intenta descargar → Falla
2. Documento se imprime **sin imagen**
3. Resto del contenido se mantiene

**Consola:**
```
❌ Error al descargar imagen desde URL: ConnectionError
⚠️  No se pudo cargar la imagen
```

## Consejos de Uso

1. **Antes de imprimir**, usa la vista previa para verificar que todo se vea correcto
2. **Para pruebas**, usa "Microsoft Print to PDF" en lugar de desperdiciar papel
3. **Si la imagen no aparece**, verifica la conexión a internet (si es URL de Cloudinary)
4. **Para mejor calidad**, usa imágenes de al menos 400x400 píxeles
5. **Ajusta el zoom** en la vista previa para ver detalles

## Solución de Problemas

| Problema | Solución |
|----------|----------|
| Imagen no aparece | Verifica `image_path` o conexión a internet |
| Vista previa en blanco | Verifica que el plato tenga datos (nombre, precio) |
| No se detectan impresoras | Instala al menos "Microsoft Print to PDF" |
| Error al imprimir | Verifica que la impresora esté encendida y en línea |
| Texto cortado | La impresora puede tener márgenes más grandes, ajusta en config |

---

**Nota:** Este es un documento de referencia. El documento real impreso tendrá mejor calidad y formato exacto según la configuración de tu impresora.
