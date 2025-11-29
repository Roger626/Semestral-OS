"""
Script de inicialización del servidor
Ejecutar este archivo desde el directorio Backend
"""

if __name__ == '__main__':
    # Importar y ejecutar la aplicación
    from public.api import app
    
    import os
    
    # Obtener configuración del servidor desde variables de entorno
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    debug = os.getenv('API_DEBUG', 'False').lower() == 'true'
    
    print("\n" + "="*50)
    print("🚀 Iniciando API de Restaurante")
    print("="*50)
    print(f"📍 Host: {host}")
    print(f"🔌 Puerto: {port}")
    print(f"🐛 Debug: {debug}")
    print("="*50 + "\n")
    
    # Iniciar servidor
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )
