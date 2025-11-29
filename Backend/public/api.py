from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
import sys

# Agregar el directorio raíz del Backend al path de Python
# Esto permite importar módulos desde cualquier subdirectorio
backend_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_root)

# Importar dependencias
from utils.conexion import DatabaseConnection
from model.menuModel import MenuModel
from controller.menuController import MenuController

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask app
app = Flask(__name__)

# Configuración de CORS para permitir acceso desde cualquier origen
# Esto es importante para que el frontend en otra computadora pueda conectarse
CORS(app, resources={
    r"/*": {
        "origins": "*",  # Permitir todos los orígenes (puedes restringirlo a IPs específicas)
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type"],
        "supports_credentials": True,
        "max_age": 3600
    }
})

# Configuración de la aplicación
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Límite de 16MB para archivos
app.config['JSON_AS_ASCII'] = False  # Soporte para caracteres UTF-8

# Configuración de la base de datos desde variables de entorno
DB_CONFIG = {
    "host": os.getenv('DB_HOST', 'localhost'),
    "user": os.getenv('DB_USER', 'root'),
    "password": os.getenv('DB_PASSWORD', ''),
    "port": int(os.getenv('DB_PORT', 3306)),
    "database": os.getenv('DB_NAME', 'restaurante')
}

# Inicializar conexión a la base de datos (Singleton)
try:
    db_connection = DatabaseConnection(**DB_CONFIG)
    print("✓ Conexión a base de datos establecida")
except Exception as e:
    print(f"✗ Error al conectar con la base de datos: {e}")
    db_connection = None

# Inyección de dependencias
menu_model = MenuModel(db_connection) if db_connection else None
menu_controller = MenuController(menu_model) if menu_model else None


# ==================== ENDPOINTS DE LA API ====================

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificar el estado del servidor
    GET /health
    """
    db_status = "connected" if db_connection and db_connection.connection and db_connection.connection.is_connected() else "disconnected"
    
    return {
        "status": "online",
        "database": db_status,
        "message": "API de Restaurante funcionando correctamente"
    }, 200


@app.route('/menu', methods=['GET'])
def get_all_dishes():
    """
    Obtiene todos los platos del menú
    GET /menu
    """
    if not menu_controller:
        return {"code": 503, "message": "Servicio no disponible. Error de conexión a la base de datos"}, 503
    
    return menu_controller.get_all_dishes()


@app.route('/menu/<int:dish_id>', methods=['GET'])
def get_dish_by_id(dish_id):
    """
    Obtiene un plato específico por ID
    GET /menu/<id>
    """
    if not menu_controller:
        return {"code": 503, "message": "Servicio no disponible. Error de conexión a la base de datos"}, 503
    
    return menu_controller.get_dish_by_id(dish_id)


@app.route('/menu', methods=['POST'])
def create_dish():
    """
    Crea un nuevo plato en el menú
    POST /menu
    
    Content-Type: application/json
    Body: {
        "nombre": "string",
        "precio": number,
        "imagen_url": "string"
    }
    
    O
    
    Content-Type: multipart/form-data
    Body:
        nombre: string
        precio: number
        imagen: file
    """
    if not menu_controller:
        return {"code": 503, "message": "Servicio no disponible. Error de conexión a la base de datos"}, 503
    
    return menu_controller.create_dish()


@app.route('/menu/<int:dish_id>', methods=['PUT'])
def update_dish(dish_id):
    """
    Actualiza un plato existente
    PUT /menu/<id>
    
    Content-Type: application/json
    Body: {
        "nombre": "string",
        "precio": number,
        "imagen_url": "string"
    }
    
    O
    
    Content-Type: multipart/form-data
    Body:
        nombre: string
        precio: number
        imagen: file (opcional)
    """
    if not menu_controller:
        return {"code": 503, "message": "Servicio no disponible. Error de conexión a la base de datos"}, 503
    
    return menu_controller.update_dish(dish_id)


@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    """
    Elimina un plato del menú
    DELETE /menu/<id>
    """
    if not menu_controller:
        return {"code": 503, "message": "Servicio no disponible. Error de conexión a la base de datos"}, 503
    
    return menu_controller.delete_dish(dish_id)


# ==================== MANEJO DE ERRORES ====================

@app.errorhandler(404)
def not_found(error):
    """Maneja errores 404 - Ruta no encontrada"""
    return {
        "code": 404,
        "message": "Ruta no encontrada. Verifica el endpoint solicitado."
    }, 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Maneja errores 405 - Método no permitido"""
    return {
        "code": 405,
        "message": "Método HTTP no permitido para esta ruta."
    }, 405


@app.errorhandler(413)
def request_entity_too_large(error):
    """Maneja errores 413 - Archivo muy grande"""
    return {
        "code": 413,
        "message": "El archivo es demasiado grande. Tamaño máximo: 16MB"
    }, 413


@app.errorhandler(500)
def internal_server_error(error):
    """Maneja errores 500 - Error interno del servidor"""
    return {
        "code": 500,
        "message": "Error interno del servidor. Intenta de nuevo más tarde."
    }, 500


@app.errorhandler(Exception)
def handle_exception(error):
    """Maneja cualquier excepción no capturada"""
    print(f"Error no manejado: {error}")
    return {
        "code": 500,
        "message": f"Error inesperado: {str(error)}"
    }, 500


# ==================== INICIALIZACIÓN DEL SERVIDOR ====================

if __name__ == '__main__':
    # Obtener configuración del servidor desde variables de entorno
    host = os.getenv('API_HOST', '0.0.0.0')  # 0.0.0.0 permite conexiones desde cualquier IP
    port = int(os.getenv('API_PORT', 5000))
    debug = os.getenv('API_DEBUG', 'False').lower() == 'true'
    
    print("\n" + "="*50)
    print("🚀 Iniciando API de Restaurante")
    print("="*50)
    print(f"📍 Host: {host}")
    print(f"🔌 Puerto: {port}")
    print(f"🐛 Debug: {debug}")
    print(f"🗄️  Base de datos: {DB_CONFIG['database']} @ {DB_CONFIG['host']}")
    print("="*50 + "\n")
    
    # Iniciar servidor
    # threaded=True permite manejar múltiples peticiones simultáneas
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )
