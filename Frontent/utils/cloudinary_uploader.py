"""
Módulo para subir imágenes a Cloudinary
NOTA: Este es solo el esqueleto UI, el backend implementará la lógica real
"""


class CloudinaryUploader:
    """Clase para gestionar la subida de imágenes a Cloudinary"""
    
    @staticmethod
    def upload(image_path):
        """
        Sube una imagen a Cloudinary y retorna la URL
        
        Args:
            image_path: Ruta local de la imagen
            
        Returns:
            Dict con:
                - success: bool
                - url: str (URL de Cloudinary)
                - error: str (mensaje de error si falla)
        
        NOTA: Esta es una función placeholder.
        El backend debe implementar la lógica real usando la librería cloudinary.
        """
        print("\n" + "="*50)
        print("☁️ CLOUDINARY UPLOADER - PLACEHOLDER")
        print("="*50)
        print(f"📁 Imagen local: {image_path}")
        print("⚠️ BACKEND PENDIENTE:")
        print("   1. Configurar credenciales de Cloudinary")
        print("   2. Implementar cloudinary.uploader.upload()")
        print("   3. Retornar URL pública de la imagen")
        print("="*50)
        
        # Simulación de respuesta
        return {
            "success": False,
            "url": "",
            "error": "Backend no implementado - solo UI"
        }
    
    @staticmethod
    def delete(public_id):
        """
        Elimina una imagen de Cloudinary
        
        Args:
            public_id: ID público de la imagen en Cloudinary
            
        Returns:
            Dict con success y error
        """
        print(f"🗑️ Eliminar imagen de Cloudinary: {public_id}")
        print("⚠️ Backend no implementado - solo UI")
        
        return {
            "success": False,
            "error": "Backend no implementado"
        }
