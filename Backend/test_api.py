"""
Script de prueba para verificar la API del restaurante
Ejecuta este script después de iniciar el servidor para probar todos los endpoints
"""

import requests
import json

# Configuración
BASE_URL = "http://localhost:5000"

def print_response(title, response):
    """Imprime la respuesta de forma legible"""
    print(f"\n{'='*60}")
    print(f"📋 {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except:
        print(f"Response: {response.text}")
    print(f"{'='*60}\n")

def test_api():
    """Ejecuta todas las pruebas de la API"""
    
    print("\n🚀 INICIANDO PRUEBAS DE LA API")
    print("="*60)
    
    # 1. Health Check
    try:
        response = requests.get(f"{BASE_URL}/health")
        print_response("1. Health Check", response)
    except Exception as e:
        print(f"❌ Error en Health Check: {e}")
        print("⚠️  Asegúrate de que el servidor esté corriendo (python public/api.py)")
        return
    
    # 2. Obtener todos los platos (debe estar vacío al inicio)
    try:
        response = requests.get(f"{BASE_URL}/menu")
        print_response("2. Obtener todos los platos", response)
    except Exception as e:
        print(f"❌ Error al obtener platos: {e}")
    
    # 3. Crear un nuevo plato con URL de imagen
    try:
        new_dish = {
            "nombre": "Pizza Margherita",
            "precio": 12.99,
            "imagen_url": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002"
        }
        response = requests.post(f"{BASE_URL}/menu", json=new_dish)
        print_response("3. Crear plato (Pizza Margherita)", response)
    except Exception as e:
        print(f"❌ Error al crear plato: {e}")
    
    # 4. Crear otro plato
    try:
        new_dish = {
            "nombre": "Hamburguesa Clásica",
            "precio": 9.50,
            "imagen_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
        }
        response = requests.post(f"{BASE_URL}/menu", json=new_dish)
        print_response("4. Crear plato (Hamburguesa)", response)
    except Exception as e:
        print(f"❌ Error al crear segundo plato: {e}")
    
    # 5. Obtener todos los platos nuevamente
    try:
        response = requests.get(f"{BASE_URL}/menu")
        print_response("5. Obtener todos los platos (actualizado)", response)
    except Exception as e:
        print(f"❌ Error al obtener platos: {e}")
    
    # 6. Obtener un plato específico por ID
    try:
        response = requests.get(f"{BASE_URL}/menu/1")
        print_response("6. Obtener plato por ID (1)", response)
    except Exception as e:
        print(f"❌ Error al obtener plato por ID: {e}")
    
    # 7. Actualizar un plato
    try:
        updated_dish = {
            "nombre": "Pizza Margherita Premium",
            "precio": 15.99,
            "imagen_url": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002"
        }
        response = requests.put(f"{BASE_URL}/menu/1", json=updated_dish)
        print_response("7. Actualizar plato (ID 1)", response)
    except Exception as e:
        print(f"❌ Error al actualizar plato: {e}")
    
    # 8. Verificar actualización
    try:
        response = requests.get(f"{BASE_URL}/menu/1")
        print_response("8. Verificar actualización (ID 1)", response)
    except Exception as e:
        print(f"❌ Error al verificar actualización: {e}")
    
    # 9. Probar validaciones - Precio negativo
    try:
        invalid_dish = {
            "nombre": "Plato Inválido",
            "precio": -5.00,
            "imagen_url": "https://example.com/imagen.jpg"
        }
        response = requests.post(f"{BASE_URL}/menu", json=invalid_dish)
        print_response("9. Prueba de validación (precio negativo)", response)
    except Exception as e:
        print(f"❌ Error en prueba de validación: {e}")
    
    # 10. Probar validaciones - Campo faltante
    try:
        invalid_dish = {
            "nombre": "Plato Incompleto",
            # falta precio
            "imagen_url": "https://example.com/imagen.jpg"
        }
        response = requests.post(f"{BASE_URL}/menu", json=invalid_dish)
        print_response("10. Prueba de validación (campo faltante)", response)
    except Exception as e:
        print(f"❌ Error en prueba de validación: {e}")
    
    # 11. Eliminar un plato
    try:
        response = requests.delete(f"{BASE_URL}/menu/2")
        print_response("11. Eliminar plato (ID 2)", response)
    except Exception as e:
        print(f"❌ Error al eliminar plato: {e}")
    
    # 12. Verificar eliminación
    try:
        response = requests.get(f"{BASE_URL}/menu")
        print_response("12. Verificar eliminación (listar todos)", response)
    except Exception as e:
        print(f"❌ Error al verificar eliminación: {e}")
    
    # 13. Intentar obtener plato eliminado
    try:
        response = requests.get(f"{BASE_URL}/menu/2")
        print_response("13. Intentar obtener plato eliminado (ID 2)", response)
    except Exception as e:
        print(f"❌ Error al intentar obtener plato eliminado: {e}")
    
    print("\n✅ PRUEBAS COMPLETADAS")
    print("="*60)
    print("\n📝 RESUMEN:")
    print("- Si todas las pruebas pasaron correctamente, tu backend está funcionando")
    print("- Revisa los códigos de respuesta HTTP (200, 201, 400, 404, etc.)")
    print("- Verifica que las validaciones estén funcionando correctamente")
    print("\n🌐 ACCESO REMOTO:")
    print("- Para acceder desde otra computadora, usa la IP de este servidor")
    print("- Ejemplo: http://<IP_DEL_SERVIDOR>:5000/menu")
    print("- Asegúrate de que el firewall permita conexiones al puerto 5000")
    print("="*60)

if __name__ == "__main__":
    test_api()
