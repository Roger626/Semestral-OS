import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class CloudinaryConfig:
    _instance = None
    _is_initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if CloudinaryConfig._is_initialized:
            return
        
        # Configurar Cloudinary con las credenciales
        cloudinary.config(
            cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
            api_key=os.getenv('CLOUDINARY_API_KEY'),
            api_secret=os.getenv('CLOUDINARY_API_SECRET'),
            secure=True
        )
        
        CloudinaryConfig._is_initialized = True
    
    @staticmethod
    def upload_image(file, folder="menu_images"):
        """
        Sube una imagen a Cloudinary
        
        Args:
            file: Archivo de imagen (puede ser path, bytes, o file object)
            folder: Carpeta en Cloudinary donde se guardará la imagen
            
        Returns:
            dict: Diccionario con información de la imagen subida
        """
        try:
            # Subir imagen con transformaciones optimizadas
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type="image",
                transformation=[
                    {'width': 800, 'height': 600, 'crop': 'limit'},
                    {'quality': 'auto'},
                    {'fetch_format': 'auto'}
                ]
            )
            
            return {
                "success": True,
                "url": result['secure_url'],
                "public_id": result['public_id'],
                "format": result['format'],
                "width": result['width'],
                "height": result['height']
            }
            
        except cloudinary.exceptions.Error as e:
            return {
                "success": False,
                "error": f"Error de Cloudinary: {str(e)}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al subir imagen: {str(e)}"
            }
    
    @staticmethod
    def delete_image(public_id):
        """
        Elimina una imagen de Cloudinary
        
        Args:
            public_id: ID público de la imagen en Cloudinary
            
        Returns:
            dict: Resultado de la operación
        """
        try:
            result = cloudinary.uploader.destroy(public_id)
            
            return {
                "success": result.get('result') == 'ok',
                "message": "Imagen eliminada exitosamente" if result.get('result') == 'ok' else "No se pudo eliminar la imagen"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al eliminar imagen: {str(e)}"
            }
    
    @staticmethod
    def extract_public_id(cloudinary_url):
        """
        Extrae el public_id de una URL de Cloudinary
        
        Args:
            cloudinary_url: URL completa de la imagen en Cloudinary
            
        Returns:
            str: Public ID de la imagen
        """
        try:
            # Formato típico: https://res.cloudinary.com/{cloud_name}/image/upload/v{version}/{folder}/{public_id}.{format}
            if not cloudinary_url or 'cloudinary.com' not in cloudinary_url:
                return None
            
            # Dividir por '/' y obtener las partes después de 'upload/'
            parts = cloudinary_url.split('/upload/')
            if len(parts) < 2:
                return None
            
            # Obtener la segunda parte y remover la versión si existe
            path = parts[1]
            if path.startswith('v'):
                path = '/'.join(path.split('/')[1:])
            
            # Remover la extensión del archivo
            public_id = path.rsplit('.', 1)[0]
            
            return public_id
            
        except Exception as e:
            print(f"Error al extraer public_id: {e}")
            return None
