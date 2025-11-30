"""
Componente de formulario para los datos del plato
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                             QLineEdit, QDateEdit, QHBoxLayout, QFileDialog)
from PyQt6.QtCore import QDate
from styles.colors import Colors
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt


class FormFields(QWidget):
    """Widget que contiene todos los campos del formulario"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Inicializa los campos del formulario"""
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Campos: Nombre y Precio en una misma fila (más compacto)
        row = QHBoxLayout()
        row.setSpacing(8)

        name_col = QVBoxLayout()
        self.name_label = QLabel("Nombre del Plato")
        self.name_label.setObjectName("fieldLabel")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ej: Paella Valenciana")
        self.name_input.setMinimumHeight(30)
        name_col.addWidget(self.name_label)
        name_col.addWidget(self.name_input)

        price_col = QVBoxLayout()
        self.price_label = QLabel("Precio (€)")
        self.price_label.setObjectName("fieldLabel")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Ej: 24.50")
        self.price_input.setMinimumHeight(30)
        price_col.addWidget(self.price_label)
        price_col.addWidget(self.price_input)

        row.addLayout(name_col, stretch=3)
        row.addLayout(price_col, stretch=1)
        layout.addLayout(row)
        
        # Campo: Fecha
        self.date_label = QLabel("Fecha desde que está en el menú")
        self.date_label.setObjectName("fieldLabel")
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setDisplayFormat("dd/MM/yyyy")
        self.date_input.setMinimumHeight(30)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        
        # Nota: El campo URL y el botón de subida fueron eliminados.
        # La imagen se gestiona mediante arrastrar&soltar en la vista previa.
    
    def get_data(self):
        """Obtiene los datos del formulario"""
        return {
            "name": self.name_input.text(),
            "price": self.price_input.text(),
            "date": self.date_input.date().toString("yyyy-MM-dd")
        }
    
    def set_data(self, name="", price="", date="", image_url=""):
        """Establece los datos en el formulario"""
        self.name_input.setText(name)
        self.price_input.setText(price)
        
        if date:
            q_date = QDate.fromString(date, "yyyy-MM-dd")
            if q_date.isValid():
                self.date_input.setDate(q_date)
        
        # image_url ya no se usa en el formulario
    
    def clear_data(self):
        """Limpia todos los campos del formulario"""
        self.name_input.clear()
        self.price_input.clear()
        self.date_input.setDate(QDate.currentDate())
        # image_url_input fue eliminado; no hay campo para limpiar aquí
    
    def open_file_dialog(self):
        """Abre el explorador de archivos para seleccionar imagen"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        return file_path
