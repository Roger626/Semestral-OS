# 🎯 GUÍA PASO A PASO - Sistema de Impresión

Esta guía te llevará desde cero hasta tener la funcionalidad de impresión completamente operativa.

## 📋 Requisitos Previos

- ✅ Python 3.8 o superior instalado
- ✅ Frontend instalado (dependencias de PyQt6)
- ✅ Al menos una impresora instalada (física o virtual como "Microsoft Print to PDF")

---

## 🚀 PASO 1: Verificar Instalación

### Windows

```bash
cd d:\Proyects\Semestral-OS\Frontent
python --version
```

Deberías ver: `Python 3.8.x` o superior

### Linux

```bash
cd /path/to/Frontent
python3 --version
```

---

## 🔧 PASO 2: Verificar Dependencias

```bash
# Windows
pip show PyQt6

# Linux
pip3 show PyQt6
```

Si no está instalado:

```bash
# Windows
pip install -r requirements.txt

# Linux
pip3 install -r requirements.txt
```

---

## 🖨️ PASO 3: Verificar Impresoras

### Ejecutar script de prueba

```bash
# Windows
python test_printers.py

# Linux
python3 test_printers.py
```

### Resultado esperado

```
============================================================
🖨️  PRUEBA DE DETECCIÓN DE IMPRESORAS
============================================================

✅ Se detectaron X impresora(s):

1. Microsoft Print to PDF (Predeterminada)
   Estado: ✅ Disponible
   Descripción: Microsoft Print to PDF
   Ubicación: No especificada
   Tipo: 📄 Impresora virtual (PDF)

...
```

### Si NO se detectan impresoras

#### Windows:

1. Abre **Configuración** → **Dispositivos** → **Impresoras y escáneres**
2. Verifica que al menos aparezca **Microsoft Print to PDF**
3. Si no está, habilítala:
   - **Configuración** → **Aplicaciones** → **Características opcionales**
   - **Agregar una característica** → Buscar "Microsoft Print to PDF"
   - Instalar

#### Linux (Fedora):

```bash
# Instalar CUPS (sistema de impresión)
sudo dnf install cups cups-client

# Iniciar servicio
sudo systemctl start cups
sudo systemctl enable cups

# Verificar estado
sudo systemctl status cups

# Para imprimir a PDF
sudo dnf install cups-pdf
```

#### Linux (Ubuntu/Debian):

```bash
# Instalar CUPS
sudo apt install cups cups-client cups-pdf

# Iniciar servicio
sudo systemctl start cups
sudo systemctl enable cups
```

---

## 🎬 PASO 4: Probar Demo de Impresión

Esta demo muestra la vista previa de impresión sin necesidad de ejecutar toda la aplicación.

```bash
# Windows
python demo_print.py

# Linux
python3 demo_print.py
```

### Qué esperar:

1. Mensaje de bienvenida
2. Lista de impresoras detectadas
3. Se abre **ventana de vista previa**
4. Puedes ver el documento formateado
5. Puedes imprimir o cerrar

### Controles de la vista previa:

- **🖨️ Imprimir**: Abre diálogo para seleccionar impresora
- **🔍 Zoom**: Acercar/alejar
- **📄 Página**: Navegar si hay múltiples páginas
- **⚙️ Configurar**: Cambiar orientación, tamaño de página
- **❌ Cerrar**: Salir sin imprimir

---

## 🍽️ PASO 5: Usar en la Aplicación Real

### Iniciar aplicación

```bash
# Windows
python main.py
# o
run_app.bat

# Linux
python3 main.py
# o
./run_app.sh
```

### Imprimir un plato

1. **Navegar** a un plato usando los botones **◀ Anterior** / **Siguiente ▶**

2. **Clic en 🖨️ Imprimir**

3. **Ver vista previa**:
   - Verifica que los datos se vean correctos
   - Verifica que la imagen aparezca (si el plato tiene imagen)

4. **Opciones desde vista previa**:

   **a) Imprimir en papel:**
   - Clic en icono **🖨️** en la barra de herramientas
   - Selecciona tu impresora física
   - Configura número de copias
   - Clic **OK**

   **b) Guardar como PDF:**
   - Clic en icono **🖨️** en la barra de herramientas
   - Selecciona **Microsoft Print to PDF** (Windows) o **CUPS-PDF** (Linux)
   - Clic **OK**
   - Elige ubicación y nombre del archivo
   - Clic **Guardar**

   **c) Solo ver (no imprimir):**
   - Revisa el documento
   - Clic en **X** o **Cerrar**

---

## 📊 PASO 6: Verificar Salida en Consola

Cuando haces clic en **🖨️ Imprimir**, deberías ver en la consola:

```
====================================================
📄 PREPARANDO DOCUMENTO PARA IMPRESIÓN
====================================================
Nombre del Plato: Paella Valenciana
Precio: $24.50
Fecha en menú: 2024-01-15
Imagen local: C:\path\to\image.jpg

🖨️  Impresoras disponibles: 3
   1. HP LaserJet (Predeterminada)
   2. Microsoft Print to PDF
   3. Canon Pixma
====================================================
📷 Cargando imagen desde: C:\path\to\image.jpg
✅ Imagen cargada correctamente
📄 Documento renderizado correctamente
✅ Vista previa cerrada - El usuario pudo imprimir desde la vista previa
```

---

## 🧪 PASO 7: Casos de Prueba

### Caso 1: Imprimir plato CON imagen local

1. Agrega un plato con imagen arrastrando un archivo
2. Clic **🖨️ Imprimir**
3. **Resultado esperado**: Documento con imagen incluida

### Caso 2: Imprimir plato CON imagen en Cloudinary

1. Plato que tenga `image_url` de Cloudinary
2. Verifica conexión a internet
3. Clic **🖨️ Imprimir**
4. **Resultado esperado**: Imagen se descarga y aparece en documento

### Caso 3: Imprimir plato SIN imagen

1. Plato sin imagen asignada
2. Clic **🖨️ Imprimir**
3. **Resultado esperado**: Documento solo con texto (nombre, precio, fecha)

### Caso 4: Guardar como PDF

1. Cualquier plato
2. Clic **🖨️ Imprimir**
3. En vista previa → **🖨️** → Seleccionar impresora PDF
4. Guardar en ubicación deseada
5. **Resultado esperado**: Archivo PDF creado

---

## 🔍 PASO 8: Troubleshooting

### Problema 1: "No se detectaron impresoras"

**Síntoma:** `test_printers.py` muestra `❌ No se detectaron impresoras`

**Solución:**
1. Instala al menos "Microsoft Print to PDF" (Windows)
2. Instala CUPS (Linux)
3. Reinicia la aplicación

### Problema 2: "Vista previa en blanco"

**Síntoma:** Se abre la vista previa pero está vacía

**Solución:**
1. Verifica que el plato tenga datos (nombre, precio)
2. Cierra y vuelve a intentar
3. Verifica logs en consola

### Problema 3: "Imagen no aparece en documento"

**Síntoma:** El documento se imprime pero sin imagen

**Posibles causas:**
- No hay imagen asignada al plato → **Normal**
- Ruta de imagen incorrecta → Verifica `image_path`
- Sin conexión a internet (URL Cloudinary) → Verifica conexión
- URL de Cloudinary inválida → Verifica `image_url`

**Solución:**
- Verifica en consola si se muestra: `❌ Error al descargar imagen`
- Si es local, verifica que el archivo exista
- Si es Cloudinary, verifica URL en navegador

### Problema 4: "Error al imprimir en impresora física"

**Síntoma:** Diálogo de error al intentar imprimir

**Solución:**
1. Verifica que la impresora esté **encendida**
2. Verifica que esté **en línea** (no pausada)
3. Verifica que tenga **papel** y **tinta/tóner**
4. Prueba imprimir desde otra aplicación (Word, Notepad)
5. Reinstala el driver de la impresora

### Problema 5: "La aplicación se congela al imprimir"

**Solución:**
1. Cierra la aplicación (Ctrl+C o Cerrar ventana)
2. Verifica impresoras en el sistema
3. Reinicia servicio de impresión:
   - Windows: `services.msc` → "Spooler de impresión" → Reiniciar
   - Linux: `sudo systemctl restart cups`
4. Vuelve a ejecutar la aplicación

---

## ✅ Checklist Final

Verifica que puedas hacer lo siguiente:

- [ ] **Detectar impresoras**: `python test_printers.py` muestra al menos 1 impresora
- [ ] **Ver demo**: `python demo_print.py` muestra vista previa
- [ ] **Abrir aplicación**: `python main.py` se ejecuta sin errores
- [ ] **Navegar platos**: Botones Anterior/Siguiente funcionan
- [ ] **Abrir vista previa**: Botón **🖨️ Imprimir** abre vista previa
- [ ] **Ver documento**: Vista previa muestra datos formateados
- [ ] **Guardar PDF**: Puedes guardar documento como PDF
- [ ] **Imprimir (opcional)**: Si tienes impresora física, puedes imprimir

---

## 🎯 Flujo Completo de Uso

```
1. Ejecutar aplicación
   python main.py
         ↓
2. Navegar a un plato
   (Botones ◀ ▶)
         ↓
3. Clic en 🖨️ Imprimir
         ↓
4. Se abre vista previa
   (ventana modal)
         ↓
5. Revisar documento
   (zoom, navegar)
         ↓
6. Decidir acción:
   ┌──────────┴──────────┐
   ↓                     ↓
Imprimir             Cancelar
   ↓
7. Diálogo impresión
   (seleccionar impresora)
   ↓
8. Configurar:
   - Impresora
   - Copias
   - Orientación
   ↓
9. Clic OK
   ↓
10. ✅ Documento impreso/guardado
```

---

## 📚 Documentación Adicional

- **Guía completa:** [PRINTING.md](PRINTING.md)
- **Ejemplo visual:** [PRINT_EXAMPLE.md](PRINT_EXAMPLE.md)
- **Resumen técnico:** [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
- **README principal:** [README.md](README.md)

---

## 🆘 Soporte

Si tienes problemas:

1. Lee la sección **Troubleshooting** arriba
2. Revisa los logs en la consola
3. Ejecuta `python test_printers.py` para diagnóstico
4. Verifica que CUPS esté corriendo (Linux)
5. Verifica que Spooler de impresión esté activo (Windows)

---

## 🎉 ¡Éxito!

Si completaste todos los pasos, ahora puedes:

✅ Imprimir fichas de platos con vista previa  
✅ Guardar documentos como PDF  
✅ Incluir imágenes en los documentos  
✅ Funciona en Windows y Linux  

**¡Disfruta de tu nuevo sistema de impresión!** 🍽️🖨️
