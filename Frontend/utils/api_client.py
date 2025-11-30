"""
Cliente para comunicarse con el backend REST API
Gestiona todas las peticiones HTTP al servidor
"""

import requests
from typing import Dict, Optional, Any
from utils.config import Config


class APIClient:
    """Cliente para comunicación con el backend"""
    
    # URL del backend (se carga desde .env)
    BASE_URL = Config.get_backend_url()
    TIMEOUT = Config.REQUEST_TIMEOUT
    
    @classmethod
    def set_base_url(cls, url: str):
        """
        Configura la URL base del backend
        
        Args:
            url: URL completa del backend (ej: http://192.168.1.100:5000)
        """
        cls.BASE_URL = url.rstrip('/')
        print(f"✓ URL del backend configurada: {cls.BASE_URL}")
    
    @classmethod
    def health_check(cls) -> Dict[str, Any]:
        """
        Verifica que el backend esté disponible
        
        Returns:
            Dict con status del servidor
        """
        try:
            response = requests.get(
                f"{cls.BASE_URL}/health",
                timeout=cls.TIMEOUT
            )
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "data": response.json()
                }
            else:
                return {
                    "success": False,
                    "error": f"Error del servidor: {response.status_code}"
                }
                
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "No se pudo conectar con el servidor. Verifica que esté corriendo."
            }
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Tiempo de espera agotado al conectar con el servidor."
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error inesperado: {str(e)}"
            }
    
    @classmethod
    def get_all_dishes(cls) -> Dict[str, Any]:
        """
        Obtiene todos los platos del menú
        
        Returns:
            Dict con lista de platos o error
        """
        try:
            response = requests.get(
                f"{cls.BASE_URL}/menu",
                timeout=cls.TIMEOUT
            )
            
            data = response.json()
            
            if data.get('code') == 200:
                return {
                    "success": True,
                    "data": data.get('data', [])
                }
            else:
                return {
                    "success": False,
                    "error": data.get('message', 'Error desconocido')
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al obtener platos: {str(e)}"
            }
    
    @classmethod
    def get_dish_by_id(cls, dish_id: int) -> Dict[str, Any]:
        """
        Obtiene un plato específico por ID
        
        Args:
            dish_id: ID del plato
            
        Returns:
            Dict con datos del plato o error
        """
        try:
            response = requests.get(
                f"{cls.BASE_URL}/menu/{dish_id}",
                timeout=cls.TIMEOUT
            )
            
            data = response.json()
            
            if data.get('code') == 200:
                return {
                    "success": True,
                    "data": data.get('data')
                }
            else:
                return {
                    "success": False,
                    "error": data.get('message', 'Plato no encontrado')
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al obtener plato: {str(e)}"
            }
    
    @classmethod
    def create_dish(cls, nombre: str, precio: float, imagen_path: Optional[str] = None,
                    imagen_url: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea un nuevo plato en el menú
        
        Args:
            nombre: Nombre del plato
            precio: Precio del plato
            imagen_path: Ruta local de la imagen (para subir archivo)
            imagen_url: URL de la imagen (alternativa a imagen_path)
            
        Returns:
            Dict con resultado de la operación
        """
        try:
            # Si se proporciona una imagen local, usar multipart/form-data
            if imagen_path:
                with open(imagen_path, 'rb') as img_file:
                    files = {'imagen': img_file}
                    data = {
                        'nombre': nombre,
                        'precio': str(precio)
                    }
                    
                    response = requests.post(
                        f"{cls.BASE_URL}/menu",
                        files=files,
                        data=data,
                        timeout=30  # Más tiempo para subir imagen
                    )
            
            # Si solo hay URL, usar JSON
            elif imagen_url:
                json_data = {
                    'nombre': nombre,
                    'precio': precio,
                    'imagen_url': imagen_url
                }
                
                response = requests.post(
                    f"{cls.BASE_URL}/menu",
                    json=json_data,
                    timeout=cls.TIMEOUT
                )
            
            else:
                return {
                    "success": False,
                    "error": "Debe proporcionar una imagen (archivo o URL)"
                }
            
            result = response.json()
            
            if result.get('code') == 201:
                return {
                    "success": True,
                    "message": result.get('message', 'Plato creado exitosamente')
                }
            else:
                return {
                    "success": False,
                    "error": result.get('message', 'Error al crear plato')
                }
                
        except FileNotFoundError:
            return {
                "success": False,
                "error": f"No se encontró el archivo de imagen: {imagen_path}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al crear plato: {str(e)}"
            }
    
    @classmethod
    def update_dish(cls, dish_id: int, nombre: str, precio: float,
                    imagen_path: Optional[str] = None,
                    imagen_url: Optional[str] = None) -> Dict[str, Any]:
        """
        Actualiza un plato existente
        
        Args:
            dish_id: ID del plato a actualizar
            nombre: Nuevo nombre
            precio: Nuevo precio
            imagen_path: Nueva imagen local (opcional)
            imagen_url: Nueva URL de imagen (opcional)
            
        Returns:
            Dict con resultado de la operación
        """
        try:
            # Si se proporciona una imagen nueva, usar multipart/form-data
            if imagen_path:
                with open(imagen_path, 'rb') as img_file:
                    files = {'imagen': img_file}
                    data = {
                        'nombre': nombre,
                        'precio': str(precio)
                    }
                    
                    response = requests.put(
                        f"{cls.BASE_URL}/menu/{dish_id}",
                        files=files,
                        data=data,
                        timeout=30
                    )
            
            # Si hay URL o no hay imagen nueva, usar JSON
            else:
                json_data = {
                    'nombre': nombre,
                    'precio': precio
                }
                
                if imagen_url:
                    json_data['imagen_url'] = imagen_url
                
                response = requests.put(
                    f"{cls.BASE_URL}/menu/{dish_id}",
                    json=json_data,
                    timeout=cls.TIMEOUT
                )
            
            result = response.json()
            
            if result.get('code') == 200:
                return {
                    "success": True,
                    "message": result.get('message', 'Plato actualizado exitosamente')
                }
            else:
                return {
                    "success": False,
                    "error": result.get('message', 'Error al actualizar plato')
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al actualizar plato: {str(e)}"
            }
    
    @classmethod
    def delete_dish(cls, dish_id: int) -> Dict[str, Any]:
        """
        Elimina un plato del menú
        
        Args:
            dish_id: ID del plato a eliminar
            
        Returns:
            Dict con resultado de la operación
        """
        try:
            response = requests.delete(
                f"{cls.BASE_URL}/menu/{dish_id}",
                timeout=cls.TIMEOUT
            )
            
            result = response.json()
            
            if result.get('code') == 200:
                return {
                    "success": True,
                    "message": result.get('message', 'Plato eliminado exitosamente')
                }
            else:
                return {
                    "success": False,
                    "error": result.get('message', 'Error al eliminar plato')
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Error al eliminar plato: {str(e)}"
            }


# Configuración para pruebas
if __name__ == "__main__":
    # Probar conexión
    print("="*50)
    print("PRUEBA DE CONEXIÓN CON EL BACKEND")
    print("="*50)
    
    result = APIClient.health_check()
    
    if result['success']:
        print("✓ Conexión exitosa con el backend")
        print(f"  Datos: {result['data']}")
    else:
        print(f"✗ Error de conexión: {result['error']}")
        print("\nAsegúrate de:")
        print("  1. Tener el backend corriendo (Backend/start_server.bat)")
        print("  2. Configurar la URL correcta en APIClient.BASE_URL")
        print(f"     Actual: {APIClient.BASE_URL}")
