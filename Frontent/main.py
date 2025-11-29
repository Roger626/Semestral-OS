"""
Punto de entrada principal de la aplicación
Gestor de Menú - Restaurante
"""

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    """Inicializa y ejecuta la aplicación"""
    app = QApplication(sys.argv)
    
    # Configuración global de la aplicación
    app.setApplicationName("Gestor de Menú - Restaurante")
    app.setOrganizationName("Restaurant Manager")
    
    # Crear y mostrar ventana principal
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
