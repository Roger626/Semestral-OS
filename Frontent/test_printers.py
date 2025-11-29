"""
Script de prueba para verificar la detección de impresoras
Funciona tanto en Windows como en Linux
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtPrintSupport import QPrinterInfo

def test_printer_detection():
    """Prueba la detección de impresoras en el sistema"""
    
    # Crear aplicación (necesario para PyQt6)
    app = QApplication(sys.argv)
    
    print("\n" + "="*60)
    print("🖨️  PRUEBA DE DETECCIÓN DE IMPRESORAS")
    print("="*60)
    print()
    
    # Obtener todas las impresoras disponibles
    printers = QPrinterInfo.availablePrinters()
    
    if not printers:
        print("❌ No se detectaron impresoras en el sistema")
        print()
        print("SOLUCIONES:")
        print()
        print("Windows:")
        print("  1. Ve a Configuración → Dispositivos → Impresoras")
        print("  2. Agrega una impresora (física o 'Microsoft Print to PDF')")
        print("  3. Verifica que el servicio 'Spooler de impresión' esté activo")
        print()
        print("Linux:")
        print("  1. Instala CUPS: sudo dnf install cups (Fedora)")
        print("                   sudo apt install cups (Ubuntu)")
        print("  2. Inicia CUPS: sudo systemctl start cups")
        print("  3. Configura impresora: http://localhost:631")
        print("  4. Para PDF: sudo dnf install cups-pdf (Fedora)")
        print("               sudo apt install cups-pdf (Ubuntu)")
        print()
        return False
    
    print(f"✅ Se detectaron {len(printers)} impresora(s):")
    print()
    
    # Obtener impresora predeterminada
    default_printer = QPrinterInfo.defaultPrinter()
    default_name = default_printer.printerName() if not default_printer.isNull() else None
    
    # Mostrar detalles de cada impresora
    for i, printer in enumerate(printers, 1):
        is_default = printer.printerName() == default_name
        default_mark = " ⭐ PREDETERMINADA" if is_default else ""
        
        print(f"{i}. {printer.printerName()}{default_mark}")
        print(f"   Estado: {'✅ Disponible' if not printer.isNull() else '❌ No disponible'}")
        print(f"   Descripción: {printer.description()}")
        print(f"   Ubicación: {printer.location() if printer.location() else 'No especificada'}")
        
        # Verificar si soporta PDF
        if "pdf" in printer.printerName().lower():
            print(f"   Tipo: 📄 Impresora virtual (PDF)")
        else:
            print(f"   Tipo: 🖨️ Impresora física")
        
        print()
    
    print("="*60)
    print("✅ DETECCIÓN EXITOSA")
    print("="*60)
    print()
    print("SIGUIENTE PASO:")
    print("  Ejecuta la aplicación principal y prueba el botón 'Imprimir'")
    print()
    
    return True


if __name__ == "__main__":
    test_printer_detection()

