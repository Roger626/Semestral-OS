"""
Estilos CSS globales para la aplicación
"""

from styles.colors import Colors

class Theme:
    """Definición de estilos Qt StyleSheet"""
    
    @staticmethod
    def get_main_stylesheet():
        """Retorna el stylesheet principal de la aplicación"""
        return f"""
            QMainWindow {{
                background-color: {Colors.BACKGROUND};
            }}
            
            QLabel {{
                color: {Colors.DARK_TEXT};
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }}
            
            QLabel#titleLabel {{
                font-size: 28px;
                font-weight: bold;
                color: {Colors.PRIMARY};
                padding: 20px;
            }}
            
            QLabel#subtitleLabel {{
                font-size: 13px;
                color: {Colors.CREAM};
                font-style: italic;
                padding-bottom: 10px;
            }}
            
            QLabel#fieldLabel {{
                font-size: 13px;
                font-weight: 600;
                color: {Colors.DARK_TEXT};
                margin-bottom: 5px;
            }}
            
            QLineEdit, QTextEdit {{
                background-color: {Colors.INPUT_BACKGROUND};
                border: 1px solid {Colors.BORDER};
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 13px;
                color: {Colors.DARK_TEXT};
                min-height: 26px;
            }}
            
            QLineEdit:focus, QTextEdit:focus {{
                border: 2px solid {Colors.PRIMARY};
                background-color: {Colors.WHITE};
            }}
            
            QLineEdit:disabled {{
                background-color: {Colors.BEIGE};
                color: {Colors.DARK_TEXT};
            }}
            
            QPushButton {{
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                font-weight: 600;
                border: none;
                color: {Colors.DARK_TEXT};
                min-height: 34px;
                max-height: 40px;
                background-color: transparent;
            }}
            
            QPushButton#addButton {{
                background-color: {Colors.SUCCESS};
                color: white;
                border-radius: 6px;
                min-height: 34px;
                max-height: 40px;
            }}
            QPushButton#addButton:hover {{
                background-color: {Colors.HOVER_SUCCESS};
                color: white;
            }}
            
            QPushButton#editButton {{
                background-color: {Colors.WARNING};
                color: {Colors.DARK_TEXT};
                border-radius: 6px;
                min-height: 34px;
                max-height: 40px;
            }}
            QPushButton#editButton:hover {{
                background-color: {Colors.HOVER_WARNING};
                color: {Colors.DARK_TEXT};
            }}
            
            QPushButton#deleteButton {{
                background-color: {Colors.DANGER};
                color: white;
                border-radius: 6px;
                min-height: 34px;
                max-height: 40px;
            }}
            QPushButton#deleteButton:hover {{
                background-color: {Colors.HOVER_DANGER};
                color: white;
            }}
            
            QPushButton#navigationButton {{
                background-color: {Colors.PRIMARY};
                color: white;
                min-width: 120px;
                border-radius: 6px;
                min-height: 32px;
                max-height: 38px;
            }}
            QPushButton#navigationButton:hover {{
                background-color: {Colors.HOVER_PRIMARY};
                color: white;
            }}
            
            QPushButton#printButton {{
                background-color: {Colors.INFO};
                color: white;
                min-width: 250px;
                border-radius: 6px;
                min-height: 34px;
                max-height: 40px;
            }}
            QPushButton#printButton:hover {{
                background-color: #42A5F5;
                color: white;
            }}
            
            QPushButton#uploadButton {{
                background-color: {Colors.CREAM};
                color: {Colors.DARK_TEXT};
                border: 2px dashed {Colors.PRIMARY};
                border-radius: 6px;
                min-height: 34px;
            }}
            QPushButton#uploadButton:hover {{
                background-color: {Colors.PRIMARY};
                color: white;
            }}
            
            QFrame#card {{
                background-color: {Colors.CARD_BACKGROUND};
                border-radius: 12px;
                border: 1px solid {Colors.BORDER};
                padding: 6px;
            }}
            
            QFrame#imagePreview {{
                background-color: {Colors.BEIGE};
                border: 2px solid {Colors.BORDER};
                border-radius: 10px;
                min-height: 200px;
                max-height: 320px;
            }}
            
            QDateEdit {{
                background-color: {Colors.INPUT_BACKGROUND};
                border: 1px solid {Colors.BORDER};
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 13px;
                color: {Colors.DARK_TEXT};
                min-height: 26px;
            }}
            
            QDateEdit:focus {{
                border: 2px solid {Colors.PRIMARY};
                background-color: {Colors.WHITE};
            }}
            
            QDateEdit::drop-down {{
                border: none;
                padding-right: 10px;
            }}
            
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
            
            /* Estilos para QMessageBox y diálogos */
            QMessageBox {{
                background-color: {Colors.BACKGROUND};
                border: 2px solid {Colors.PRIMARY};
                border-radius: 10px;
            }}
            
            QMessageBox QLabel {{
                color: {Colors.DARK_TEXT};
                font-size: 14px;
                min-width: 250px;
                max-width: 450px;
                padding: 15px;
            }}
            
            QMessageBox QPushButton {{
                background-color: {Colors.PRIMARY};
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 25px;
                min-width: 90px;
                min-height: 32px;
                font-size: 13px;
                font-weight: 600;
            }}
            
            QMessageBox QPushButton:hover {{
                background-color: {Colors.PRIMARY_DARK};
            }}
            
            QMessageBox QPushButton:pressed {{
                background-color: #6D3A28;
            }}
            
            QDialog {{
                background-color: {Colors.BACKGROUND};
                border: 2px solid {Colors.PRIMARY};
                border-radius: 10px;
            }}
            
            QDialog QLabel {{
                color: {Colors.DARK_TEXT};
                font-size: 13px;
                padding: 10px;
            }}
            
            QDialog QPushButton {{
                background-color: {Colors.PRIMARY};
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 20px;
                font-size: 12px;
                font-weight: 600;
            }}
            
            QDialog QPushButton:hover {{
                background-color: {Colors.PRIMARY_DARK};
            }}
        """
