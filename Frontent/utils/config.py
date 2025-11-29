"""
Módulo de configuración para el frontend
Carga variables de entorno y configuraciones
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)


class Config:
    """Configuración de la aplicación"""
    
    # URL del backend
    BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:5000')
    
    # Timeout para peticiones
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))
    
    # Configuración de la aplicación
    APP_NAME = "Gestor de Menú - Restaurante"
    APP_VERSION = "1.0.0"
    
    @classmethod
    def get_backend_url(cls):
        """Retorna la URL del backend configurada"""
        return cls.BACKEND_URL
    
    @classmethod
    def set_backend_url(cls, url: str):
        """
        Configura la URL del backend
        
        Args:
            url: Nueva URL del backend
        """
        cls.BACKEND_URL = url.rstrip('/')
        print(f"✓ Backend URL configurada: {cls.BACKEND_URL}")
    
    @classmethod
    def show_config(cls):
        """Muestra la configuración actual"""
        print("\n" + "="*50)
        print("CONFIGURACIÓN DEL FRONTEND")
        print("="*50)
        print(f"Aplicación: {cls.APP_NAME} v{cls.APP_VERSION}")
        print(f"Backend URL: {cls.BACKEND_URL}")
        print(f"Timeout: {cls.REQUEST_TIMEOUT}s")
        print("="*50 + "\n")
