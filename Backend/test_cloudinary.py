"""
Script de prueba para verificar la configuración de Cloudinary
"""

from utils.cloudinary_config import CloudinaryConfig
import os

def test_cloudinary():
    print("\n" + "="*50)
    print("🧪 TEST DE CLOUDINARY")
    print("="*50)
    
    # Inicializar configuración
    config = CloudinaryConfig()
    
    # Verificar variables de entorno
    print(f"\n📋 Variables de entorno:")
    print(f"   CLOUD_NAME: {os.getenv('CLOUDINARY_CLOUD_NAME')}")
    print(f"   API_KEY: {os.getenv('CLOUDINARY_API_KEY')}")
    print(f"   API_SECRET: {'*' * len(os.getenv('CLOUDINARY_API_SECRET', ''))}")
    
    # Probar subida de imagen (necesitas tener una imagen de prueba)
    test_image_path = "test_image.jpg"
    
    if os.path.exists(test_image_path):
        print(f"\n📤 Subiendo imagen de prueba: {test_image_path}")
        result = CloudinaryConfig.upload_image(test_image_path, folder="test")
        
        if result.get('success'):
            print("✅ Imagen subida exitosamente!")
            print(f"   URL: {result.get('url')}")
            print(f"   Public ID: {result.get('public_id')}")
            
            # Probar eliminación
            print(f"\n🗑️ Eliminando imagen de prueba...")
            delete_result = CloudinaryConfig.delete_image(result.get('public_id'))
            
            if delete_result.get('success'):
                print("✅ Imagen eliminada exitosamente!")
            else:
                print(f"❌ Error al eliminar: {delete_result.get('error')}")
        else:
            print(f"❌ Error al subir imagen: {result.get('error')}")
    else:
        print(f"\n⚠️ No se encontró imagen de prueba en {test_image_path}")
        print("   Crea un archivo test_image.jpg para probar la subida")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    test_cloudinary()
