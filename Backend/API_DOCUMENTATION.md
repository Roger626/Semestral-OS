# 📡 Documentación de la API - Restaurante Backend

## URL Base

```
http://localhost:5000
```

Para acceso remoto:
```
http://<IP_DEL_SERVIDOR>:5000
```

---

## Endpoints

### 1. Health Check

Verifica el estado del servidor y la conexión a la base de datos.

**Endpoint:** `GET /health`

**Respuesta exitosa (200):**
```json
{
  "status": "online",
  "database": "connected",
  "message": "API de Restaurante funcionando correctamente"
}
```

---

### 2. Obtener todos los platos

Obtiene la lista completa de platos del menú.

**Endpoint:** `GET /menu`

**Respuesta exitosa (200):**
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "nombre": "Pizza Margherita",
      "precio": 12.99,
      "imagen_url": "https://res.cloudinary.com/.../menu_images/pizza.jpg",
      "fecha_creacion": "2025-11-28"
    },
    {
      "id": 2,
      "nombre": "Hamburguesa Clásica",
      "precio": 9.50,
      "imagen_url": "https://res.cloudinary.com/.../menu_images/burger.jpg",
      "fecha_creacion": "2025-11-28"
    }
  ],
  "message": "OK"
}
```

**Respuesta con error (500):**
```json
{
  "code": 500,
  "message": "Error al obtener los datos del menú: [mensaje de error]"
}
```

---

### 3. Obtener plato por ID

Obtiene un plato específico mediante su ID.

**Endpoint:** `GET /menu/{id}`

**Parámetros:**
- `id` (path): ID del plato (número entero positivo)

**Ejemplo:** `GET /menu/1`

**Respuesta exitosa (200):**
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "nombre": "Pizza Margherita",
    "precio": 12.99,
    "imagen_url": "https://res.cloudinary.com/.../menu_images/pizza.jpg",
    "fecha_creacion": "2025-11-28"
  },
  "message": "OK"
}
```

**Respuesta - Plato no encontrado (404):**
```json
{
  "code": 404,
  "message": "Elemento no encontrado"
}
```

**Respuesta - ID inválido (400):**
```json
{
  "code": 400,
  "message": "El ID debe ser un número entero válido"
}
```

---

### 4. Crear nuevo plato

Crea un nuevo plato en el menú.

**Endpoint:** `POST /menu`

**Opción 1: Con URL de imagen**

**Content-Type:** `application/json`

**Body:**
```json
{
  "nombre": "Pizza Margherita",
  "precio": 12.99,
  "imagen_url": "https://example.com/imagen.jpg"
}
```

**Opción 2: Con archivo de imagen**

**Content-Type:** `multipart/form-data`

**Form Data:**
```
nombre: Pizza Margherita
precio: 12.99
imagen: [archivo de imagen]
```

**Validaciones:**
- `nombre`: Requerido, string, máximo 100 caracteres
- `precio`: Requerido, número positivo, máximo 999999.99
- `imagen_url` o `imagen`: Requerido (uno de los dos)
- Formatos de imagen permitidos: PNG, JPG, JPEG, GIF, WEBP
- Tamaño máximo de archivo: 16MB

**Respuesta exitosa (201):**
```json
{
  "code": 201,
  "message": "Plato creado exitosamente"
}
```

**Respuesta - Validación fallida (400):**
```json
{
  "code": 400,
  "message": "El nombre del plato es requerido"
}
```

```json
{
  "code": 400,
  "message": "El precio no puede ser negativo"
}
```

```json
{
  "code": 400,
  "message": "Formato de imagen no permitido. Use: png, jpg, jpeg, gif, webp"
}
```

---

### 5. Actualizar plato

Actualiza un plato existente.

**Endpoint:** `PUT /menu/{id}`

**Parámetros:**
- `id` (path): ID del plato a actualizar

**Opción 1: Con URL de imagen**

**Content-Type:** `application/json`

**Body:**
```json
{
  "nombre": "Pizza Margherita Premium",
  "precio": 15.99,
  "imagen_url": "https://example.com/nueva-imagen.jpg"
}
```

**Opción 2: Con archivo de imagen nuevo**

**Content-Type:** `multipart/form-data`

**Form Data:**
```
nombre: Pizza Margherita Premium
precio: 15.99
imagen: [nuevo archivo de imagen]
```

**Nota:** Si proporcionas un nuevo archivo de imagen, la imagen anterior en Cloudinary será eliminada automáticamente.

**Validaciones:**
- Mismas validaciones que en crear plato
- El ID debe existir en la base de datos

**Respuesta exitosa (200):**
```json
{
  "code": 200,
  "message": "Plato actualizado exitosamente"
}
```

**Respuesta - Plato no encontrado (404):**
```json
{
  "code": 404,
  "message": "Elemento no encontrado"
}
```

**Respuesta - Validación fallida (400):**
```json
{
  "code": 400,
  "message": "El precio debe ser un número válido"
}
```

---

### 6. Eliminar plato

Elimina un plato del menú.

**Endpoint:** `DELETE /menu/{id}`

**Parámetros:**
- `id` (path): ID del plato a eliminar

**Ejemplo:** `DELETE /menu/1`

**Nota:** Si el plato tiene una imagen en Cloudinary, también será eliminada.

**Respuesta exitosa (200):**
```json
{
  "code": 200,
  "message": "Plato eliminado exitosamente"
}
```

**Respuesta - Plato no encontrado (404):**
```json
{
  "code": 404,
  "message": "Elemento no encontrado"
}
```

**Respuesta - ID inválido (400):**
```json
{
  "code": 400,
  "message": "El ID debe ser un número positivo"
}
```

---

## Códigos de Estado HTTP

| Código | Significado | Descripción |
|--------|-------------|-------------|
| 200 | OK | Solicitud exitosa |
| 201 | Created | Recurso creado exitosamente |
| 400 | Bad Request | Datos inválidos o faltantes |
| 404 | Not Found | Recurso no encontrado |
| 405 | Method Not Allowed | Método HTTP no permitido |
| 413 | Payload Too Large | Archivo demasiado grande (>16MB) |
| 500 | Internal Server Error | Error del servidor |
| 503 | Service Unavailable | Servicio no disponible (BD desconectada) |

---

## Ejemplos de uso

### Usando cURL

**Obtener todos los platos:**
```bash
curl http://localhost:5000/menu
```

**Crear un plato con JSON:**
```bash
curl -X POST http://localhost:5000/menu \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Pizza Margherita",
    "precio": 12.99,
    "imagen_url": "https://example.com/pizza.jpg"
  }'
```

**Crear un plato con archivo:**
```bash
curl -X POST http://localhost:5000/menu \
  -F "nombre=Pizza Margherita" \
  -F "precio=12.99" \
  -F "imagen=@/ruta/a/imagen.jpg"
```

**Actualizar un plato:**
```bash
curl -X PUT http://localhost:5000/menu/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Pizza Margherita Premium",
    "precio": 15.99,
    "imagen_url": "https://example.com/pizza-premium.jpg"
  }'
```

**Eliminar un plato:**
```bash
curl -X DELETE http://localhost:5000/menu/1
```

---

### Usando JavaScript (Fetch API)

**Obtener todos los platos:**
```javascript
fetch('http://localhost:5000/menu')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Crear un plato:**
```javascript
fetch('http://localhost:5000/menu', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    nombre: 'Pizza Margherita',
    precio: 12.99,
    imagen_url: 'https://example.com/pizza.jpg'
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Crear un plato con archivo:**
```javascript
const formData = new FormData();
formData.append('nombre', 'Pizza Margherita');
formData.append('precio', '12.99');
formData.append('imagen', fileInput.files[0]);

fetch('http://localhost:5000/menu', {
  method: 'POST',
  body: formData
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Actualizar un plato:**
```javascript
fetch('http://localhost:5000/menu/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    nombre: 'Pizza Margherita Premium',
    precio: 15.99,
    imagen_url: 'https://example.com/pizza-premium.jpg'
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Eliminar un plato:**
```javascript
fetch('http://localhost:5000/menu/1', {
  method: 'DELETE'
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

---

### Usando Python (requests)

**Instalar biblioteca:**
```bash
pip install requests
```

**Código:**
```python
import requests

BASE_URL = "http://localhost:5000"

# Obtener todos los platos
response = requests.get(f"{BASE_URL}/menu")
print(response.json())

# Crear un plato
nuevo_plato = {
    "nombre": "Pizza Margherita",
    "precio": 12.99,
    "imagen_url": "https://example.com/pizza.jpg"
}
response = requests.post(f"{BASE_URL}/menu", json=nuevo_plato)
print(response.json())

# Actualizar un plato
plato_actualizado = {
    "nombre": "Pizza Margherita Premium",
    "precio": 15.99,
    "imagen_url": "https://example.com/pizza-premium.jpg"
}
response = requests.put(f"{BASE_URL}/menu/1", json=plato_actualizado)
print(response.json())

# Eliminar un plato
response = requests.delete(f"{BASE_URL}/menu/1")
print(response.json())
```

---

## Seguridad

La API implementa las siguientes medidas de seguridad:

✅ **Validación de datos:**
- Sanitización de strings para prevenir XSS
- Validación de tipos de datos
- Validación de rangos (precios, IDs)
- Validación de formatos (URLs, extensiones de archivo)

✅ **Protección contra ataques:**
- Prevención de inyección SQL (consultas parametrizadas)
- Prevención de XSS (sanitización HTML)
- Límite de tamaño de archivos (16MB)
- Validación de extensiones de archivos

✅ **CORS configurado:**
- Permite solicitudes desde cualquier origen
- Métodos permitidos: GET, POST, PUT, DELETE, OPTIONS
- Headers permitidos: Content-Type, Authorization

⚠️ **Notas de seguridad:**
- En producción, configura CORS para permitir solo orígenes específicos
- Considera agregar autenticación (JWT, OAuth)
- Usa HTTPS en producción
- Implementa rate limiting para prevenir abuso

---

## Errores comunes

### 503 Service Unavailable
**Causa:** No hay conexión a la base de datos

**Solución:**
- Verifica que MySQL esté corriendo
- Comprueba las credenciales en el archivo `.env`
- Asegúrate de que la base de datos `restaurante` existe

### 413 Payload Too Large
**Causa:** El archivo de imagen es mayor a 16MB

**Solución:**
- Reduce el tamaño de la imagen
- Usa herramientas de compresión de imágenes

### 400 Bad Request - Campos faltantes
**Causa:** No se enviaron todos los campos requeridos

**Solución:**
- Verifica que estés enviando: nombre, precio e imagen_url/imagen
- Comprueba el formato del JSON

### CORS Error
**Causa:** El navegador bloquea la solicitud por política CORS

**Solución:**
- Verifica que el servidor esté corriendo
- Comprueba que estés usando la URL correcta
- Asegúrate de que CORS esté habilitado en el servidor

---

## Soporte

Para más información, consulta:
- [README.md](README.md) - Guía de instalación
- [CLOUDINARY_SETUP.md](CLOUDINARY_SETUP.md) - Configuración de Cloudinary
