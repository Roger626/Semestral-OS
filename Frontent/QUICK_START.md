# 🚀 GUÍA DE INICIO RÁPIDO - Frontend

## ⚡ Instalación en 3 pasos

### 1. Instalar dependencias

**Windows:**
```bash
pip install -r requirements.txt
```

**Linux:**
```bash
pip3 install -r requirements.txt
```

### 2. Configurar backend

Edita `.env`:
```env
# Misma computadora
BACKEND_URL=http://localhost:5000

# Otra computadora (cambia la IP)
BACKEND_URL=http://192.168.1.100:5000
```

### 3. Ejecutar

**Windows:**
```bash
python main.py
```

**Linux:**
```bash
python3 main.py
```

---

## 🔌 Conectar desde otra computadora

### En el SERVIDOR (Backend):

1. **Obtener IP:**
   ```bash
   # Windows
   ipconfig
   
   # Linux
   ip addr show
   ```
   Ejemplo de IP: `192.168.1.100`

2. **Configurar firewall:**
   ```bash
   # Windows (como Administrador)
   cd Backend
   configure_firewall.bat
   ```
   
   ```bash
   # Linux (Fedora)
   sudo firewall-cmd --permanent --add-port=5000/tcp
   sudo firewall-cmd --reload
   ```

3. **Iniciar backend:**
   ```bash
   cd Backend
   start_server.bat     # Windows
   ./start_server.sh    # Linux
   ```

### En el CLIENTE (Frontend):

1. **Configurar `.env`:**
   ```env
   BACKEND_URL=http://192.168.1.100:5000
   ```
   (Reemplaza `192.168.1.100` con la IP del servidor)

2. **Probar conexión:**
   ```bash
   python -m utils.api_client
   ```
   
   Debe mostrar: `✓ Conexión exitosa con el backend`

3. **Iniciar aplicación:**
   ```bash
   python main.py
   ```

---

## 🖨️ Funcionalidad de Impresión

### Probar detección de impresoras

Antes de usar la función de impresión, verifica que tu sistema detecta impresoras:

```bash
python test_printers.py
```

Deberías ver algo como:

```
✅ Se detectaron 3 impresora(s):

1. HP LaserJet (Predeterminada)
2. Microsoft Print to PDF
3. OneNote (Desktop)
```

### Configurar impresora (si no hay ninguna)

**Windows:**
- Ve a **Configuración** → **Dispositivos** → **Impresoras y escáneres**
- Al menos debería estar **Microsoft Print to PDF** (para guardar como PDF)

**Linux (Fedora):**
```bash
# Instalar CUPS (sistema de impresión)
sudo dnf install cups

# Iniciar servicio
sudo systemctl start cups
sudo systemctl enable cups

# Para imprimir a PDF
sudo dnf install cups-pdf
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install cups cups-pdf
sudo systemctl start cups
sudo systemctl enable cups
```

### Usar la impresión

1. Abre la aplicación
2. Selecciona un plato
3. Clic en **🖨️ Imprimir**
4. Se abrirá la **vista previa**
5. Desde ahí puedes:
   - Ver el documento
   - Imprimir en papel
   - Guardar como PDF

📖 **Guía completa:** [PRINTING.md](PRINTING.md)  
📄 **Ejemplo visual:** [PRINT_EXAMPLE.md](PRINT_EXAMPLE.md)

---

## ✅ Checklist

Antes de usar la aplicación:

- [ ] Backend corriendo en el servidor
- [ ] Firewall configurado (puerto 5000)
- [ ] Ambas computadoras en la misma red
- [ ] IP correcta en `.env`
- [ ] Dependencias instaladas
- [ ] Ping exitoso al servidor

---

## 🐛 Problemas comunes

### "No se pudo conectar con el servidor"

```bash
# 1. Verificar que el backend está corriendo
curl http://192.168.1.100:5000/health

# 2. Hacer ping al servidor
ping 192.168.1.100

# 3. Verificar firewall
# Windows: Panel de Control → Firewall → Permitir puerto 5000
# Linux: sudo firewall-cmd --list-ports
```

### "ModuleNotFoundError"

```bash
pip install -r requirements.txt
```

### Firewall en Linux (Fedora)

```bash
# Verificar estado
sudo firewall-cmd --state

# Permitir puerto 5000
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload

# Verificar
sudo firewall-cmd --list-ports
```

---

## 📝 URLs de prueba

Una vez configurado, prueba estos endpoints desde el navegador del cliente:

```
http://192.168.1.100:5000/health    # Estado del servidor
http://192.168.1.100:5000/menu      # Lista de platos
```

---

¡Listo! 🎉
