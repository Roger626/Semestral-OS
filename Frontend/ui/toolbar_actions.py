"""
Barra de herramientas con acciones CRUD y navegación
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                             QLabel, QHBoxLayout, QFrame, QSizePolicy)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from styles.colors import Colors


class ToolbarActions(QWidget):
    """Widget con botones de acciones CRUD y navegación"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Inicializa los botones de acción"""
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Sección: Acciones CRUD
        crud_label = QLabel("Gestión de Registros")
        crud_label.setStyleSheet(f"""
            font-size: 14px;
            font-weight: 600;
            color: {Colors.DARK_TEXT};
            padding: 3px 0;
        """)
        layout.addWidget(crud_label)
        
        # Botón: Agregar
        self.add_button = QPushButton("➕ Agregar Nuevo Plato")
        self.add_button.setObjectName("addButton")
        self.add_button.setMinimumHeight(30)
        self.add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(self.add_button)
        
        # Botón: Modificar
        self.edit_button = QPushButton("✏️ Modificar Plato Actual")
        self.edit_button.setObjectName("editButton")
        self.edit_button.setMinimumHeight(30)
        self.edit_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(self.edit_button)
        
        # Botón: Eliminar
        self.delete_button = QPushButton("🗑️ Eliminar Plato")
        self.delete_button.setObjectName("deleteButton")
        self.delete_button.setMinimumHeight(30)
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(self.delete_button)
        
        # Separador
        separator1 = self.create_separator()
        layout.addWidget(separator1)
        
        # Sección: Navegación
        nav_label = QLabel("Navegación")
        nav_label.setStyleSheet(f"""
            font-size: 14px;
            font-weight: 600;
            color: {Colors.DARK_TEXT};
            padding: 3px 0;
        """)
        layout.addWidget(nav_label)
        
        # Contador de registros
        self.record_counter = QLabel("Registro 1 de 3")
        self.record_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.record_counter.setStyleSheet(f"""
            font-size: 13px;
            color: {Colors.PRIMARY};
            font-weight: 600;
            padding: 6px;
            background-color: {Colors.BEIGE};
            border-radius: 6px;
        """)
        layout.addWidget(self.record_counter)
        
        # Botones de navegación
        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(10)
        
        self.prev_button = QPushButton("⬅️ Anterior")
        self.prev_button.setObjectName("navigationButton")
        self.prev_button.setMinimumHeight(30)
        self.prev_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        nav_layout.addWidget(self.prev_button)
        
        self.next_button = QPushButton("Siguiente ➡️")
        self.next_button.setObjectName("navigationButton")
        self.next_button.setMinimumHeight(30)
        self.next_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        nav_layout.addWidget(self.next_button)
        
        layout.addLayout(nav_layout)
        
        # Separador
        separator2 = self.create_separator()
        layout.addWidget(separator2)
        
        # Sección: Otras acciones
        other_label = QLabel("Otras Acciones")
        other_label.setStyleSheet(f"""
            font-size: 14px;
            font-weight: 600;
            color: {Colors.DARK_TEXT};
            padding: 3px 0;
        """)
        layout.addWidget(other_label)
        
        # Botón: Imprimir
        self.print_button = QPushButton("🖨️ Imprimir Registro")
        self.print_button.setObjectName("printButton")
        self.print_button.setMinimumHeight(30)
        self.print_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.print_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(self.print_button)
    
    def create_separator(self):
        """Crea una línea separadora"""
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet(f"""
            background-color: {Colors.BORDER};
            max-height: 1px;
            margin: 10px 0;
        """)
        return separator
    
    def update_navigation_label(self, current, total):
        """Actualiza el contador de registros"""
        self.record_counter.setText(f"Registro {current} de {total}")
