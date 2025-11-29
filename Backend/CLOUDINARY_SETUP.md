# 📸 Guía de Configuración de Cloudinary

## ¿Qué es Cloudinary?

Cloudinary es un servicio en la nube para almacenar, transformar y optimizar imágenes y videos. Lo usamos en este proyecto para guardar las imágenes de los platos del menú.

## 🚀 Pasos para configurar Cloudinary

### 1. Crear cuenta gratuita

1. Ve a [https://cloudinary.com](https://cloudinary.com)
2. Haz clic en "Sign Up" (Registrarse)
3. Puedes registrarte con:
   - Email y contraseña
   - Cuenta de Google
   - Cuenta de GitHub

### 2. Obtener credenciales

Una vez registrado:

1. Serás redirigido al **Dashboard**
2. En la parte superior verás un cuadro con tus credenciales:
   ```
   Cloud name: tu_cloud_name
   API Key: 123456789012345
   API Secret: abcdefghijklmnopqrstuvwxyz
   ```

3. Copia estos valores

### 3. Configurar en el archivo `.env`

Abre el archivo `.env` en el Backend y reemplaza:

```env
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret
```

Con tus valores reales:

```env
CLOUDINARY_CLOUD_NAME=dxyz123abc
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcdefghijklmnopqrstuvwxyz
```

### 4. Verificar configuración

Para verificar que Cloudinary está configurado correctamente:

1. Inicia el servidor: `start_server.bat`
2. Prueba subir una imagen usando el endpoint POST /menu con un archivo
3. Revisa en el Dashboard de Cloudinary que la imagen aparezca en la carpeta `menu_images`

## 📋 Características del plan gratuito

El plan gratuito de Cloudinary incluye:

- ✅ 25 créditos mensuales
- ✅ 25GB de almacenamiento
- ✅ 25GB de ancho de banda mensual
- ✅ Todas las transformaciones de imagen
- ✅ API completa

**¡Es más que suficiente para un proyecto de aprendizaje!**

## 🔒 Seguridad

**IMPORTANTE:**

- ❌ **NUNCA** compartas tu API Secret públicamente
- ❌ **NUNCA** subas el archivo `.env` a GitHub o repositorios públicos
- ✅ Mantén tus credenciales en el archivo `.env` (ya está en `.gitignore`)
- ✅ Solo comparte el archivo `.env.example` que no contiene credenciales reales

## 🌐 Acceder al Dashboard de Cloudinary

1. Inicia sesión en [https://cloudinary.com](https://cloudinary.com)
2. Desde el Dashboard puedes:
   - Ver todas tus imágenes subidas
   - Ver estadísticas de uso
   - Gestionar transformaciones
   - Acceder a la documentación de la API

## 📁 Estructura en Cloudinary

Las imágenes se guardarán en:
```
cloudinary.com/
└── tu_cloud_name/
    └── menu_images/
        ├── imagen1.jpg
        ├── imagen2.png
        └── ...
```

## 🛠️ Pruebas locales

Si quieres probar localmente sin Cloudinary:

1. En el controlador, comenta la parte de Cloudinary
2. Usa URLs de imágenes públicas (ejemplo: Unsplash, Imgur)
3. Luego configura Cloudinary cuando estés listo

## ❓ Problemas comunes

### Error: "Invalid API credentials"
- Verifica que copiaste correctamente las credenciales
- Asegúrate de no tener espacios antes o después de los valores
- Reinicia el servidor después de cambiar el `.env`

### Error: "Failed to upload image"
- Verifica tu conexión a internet
- Comprueba que el archivo sea una imagen válida (PNG, JPG, GIF, WEBP)
- Revisa que el tamaño del archivo sea menor a 16MB

### Las imágenes no aparecen en el Dashboard
- Espera unos segundos, pueden tardar en aparecer
- Verifica que estés en la cuenta correcta
- Revisa la carpeta "Media Library" en el menú lateral

## 📚 Recursos adicionales

- [Documentación oficial de Cloudinary](https://cloudinary.com/documentation)
- [Guía de inicio rápido](https://cloudinary.com/documentation/python_quickstart)
- [API Reference Python](https://cloudinary.com/documentation/python_integration)

---

Si necesitas ayuda, revisa la [documentación oficial](https://cloudinary.com/documentation) o contacta al soporte de Cloudinary.
