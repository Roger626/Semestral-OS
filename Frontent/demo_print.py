"""
Demo de funcionalidad de impresión
Muestra cómo usar PrintManager sin necesidad de la GUI completa
"""

import sys
from PyQt6.QtWidgets import QApplication
from utils.print_manager import PrintManager


def demo_print():
    """Demuestra la funcionalidad de impresión"""
    
    # Crear aplicación (necesario para PyQt6)
    app = QApplication(sys.argv)
    
    print("\n" + "="*60)
    print("🖨️  DEMO DE FUNCIONALIDAD DE IMPRESIÓN")
    print("="*60)
    print()
    print("Esta demo mostrará la vista previa de impresión de un plato")
    print("de ejemplo sin necesidad de ejecutar la aplicación completa.")
    print()
    print("Características que verás:")
    print("  • Detección automática de impresoras")
    print("  • Vista previa del documento")
    print("  • Documento formateado con datos del plato")
    print("  • Nota: La imagen no se mostrará (no hay imagen local)")
    print()
    print("Desde la vista previa podrás:")
    print("  • Ver el documento completo")
    print("  • Imprimir en papel")
    print("  • Guardar como PDF")
    print("  • Configurar impresora, copias, orientación")
    print()
    input("Presiona Enter para continuar...")
    print()
    
    # Datos de ejemplo de un plato
    document_data = {
        "name": "Paella Valenciana Premium",
        "price": "$28.99",
        "date": "2024-11-29",
        "image_path": "",  # Sin imagen local
        "image_url": "https://res.cloudinary.com/demo/image/upload/sample.jpg"  # URL de ejemplo
    }
    
    print("Datos del plato a imprimir:")
    print(f"  Nombre: {document_data['name']}")
    print(f"  Precio: {document_data['price']}")
    print(f"  Fecha: {document_data['date']}")
    print()
    
    # Llamar al gestor de impresión
    print("Abriendo vista previa de impresión...")
    print()
    
    PrintManager.print_document(document_data)
    
    print()
    print("="*60)
    print("Demo finalizada")
    print("="*60)
    print()


if __name__ == "__main__":
    demo_print()

