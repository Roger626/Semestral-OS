"""
Ventana principal de la aplicación
Contiene el layout principal con dos columnas
"""

from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QFrame, QScrollArea, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCursor

from styles.theme import Theme
from styles.colors import Colors
from ui.form_fields import FormFields
from ui.toolbar_actions import ToolbarActions
from ui.image_viewer import ImageViewer
from utils.print_manager import PrintManager
from utils.api_client import APIClient


class MainWindow(QMainWindow):
    """Ventana principal del Gestor de Menú"""
    
    def __init__(self):
        super().__init__()
        self.current_record_index = 0  # Índice del registro actual
        self.records_data = []  # Aquí se cargarán los datos del backend
        self.api_client = APIClient()  # Cliente API para backend
        
        # Configuración de la ventana
        self.setWindowTitle("Gestor de Menú - Restaurante")
        self.setMinimumSize(1024, 768)
        self.resize(1280, 800)
        
        # Aplicar stylesheet
        self.setStyleSheet(Theme.get_main_stylesheet())
        
        # Barra de estado
        self.statusBar().showMessage("Listo")
        
        # Inicializar UI
        self.init_ui()
        
        # Cargar datos del backend
        self.load_data_from_backend()
    
    def init_ui(self):
        """Inicializa la interfaz de usuario"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal vertical
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(18, 12, 18, 18)
        main_layout.setSpacing(14)
        
        # Encabezado
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Contenedor principal con dos columnas
        content_layout = QHBoxLayout()
        content_layout.setSpacing(14)

        # COLUMNA IZQUIERDA - Formulario (compacta)
        left_column = self.create_left_column()
        content_layout.addWidget(left_column, stretch=3)

        # COLUMNA DERECHA - Acciones
        right_column = self.create_right_column()
        content_layout.addWidget(right_column, stretch=2)

        main_layout.addLayout(content_layout)
    
    def create_header(self):
        """Crea el encabezado de la aplicación"""
        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 10)
        header_layout.setSpacing(5)
        
        # Título principal
        title = QLabel("Gestor de Menú – Restaurante")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(title)
        
        # Línea divisoria (más sutil)
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet(f"background-color: {Colors.BORDER}; max-height: 1px;")
        header_layout.addWidget(line)
        
        return header_widget
    
    def create_left_column(self):
        """Crea la columna izquierda con el formulario"""
        # Frame contenedor (card)
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(12, 12, 12, 12)
        card_layout.setSpacing(8)

        # Título de la sección
        section_title = QLabel("📋 Datos del Plato")
        section_title.setStyleSheet(f"""
            font-size: 18px;
            font-weight: bold;
            color: {Colors.PRIMARY};
            padding-bottom: 8px;
        """)
        card_layout.addWidget(section_title)

        # Formulario de campos
        self.form_fields = FormFields()
        card_layout.addWidget(self.form_fields)

        # Visor de imagen
        self.image_viewer = ImageViewer()
        card_layout.addWidget(self.image_viewer)

        # Nota: la carga de imagen ahora se maneja mediante drag & drop

        card_layout.addStretch()

        # Retornar el card directamente (compacto, sin scroll)
        return card
    
    def create_right_column(self):
        """Crea la columna derecha con las acciones CRUD"""
        # Frame contenedor (card)
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(12, 12, 12, 12)
        card_layout.setSpacing(10)
        
        # Título de la sección
        section_title = QLabel("⚙️ Acciones")
        section_title.setStyleSheet(f"""
            font-size: 20px;
            font-weight: bold;
            color: {Colors.PRIMARY};
            padding-bottom: 10px;
        """)
        card_layout.addWidget(section_title)
        
        # Toolbar de acciones CRUD
        self.toolbar = ToolbarActions()
        card_layout.addWidget(self.toolbar)
        
        # Conectar señales de los botones
        self.toolbar.add_button.clicked.connect(self.handle_add_record)
        self.toolbar.edit_button.clicked.connect(self.handle_edit_record)
        self.toolbar.delete_button.clicked.connect(self.handle_delete_record)
        self.toolbar.prev_button.clicked.connect(self.handle_previous_record)
        self.toolbar.next_button.clicked.connect(self.handle_next_record)
        self.toolbar.print_button.clicked.connect(self.print_record_ui)
        
        card_layout.addStretch()
        # Retornar el card directamente para evitar scroll en la columna derecha
        # y mantener la estructura compacta
        return card
    
    def load_data_from_backend(self):
        """Carga datos desde el backend"""
        try:
            self.setCursor(QCursor(Qt.CursorShape.WaitCursor))
            self.statusBar().showMessage("⏳ Cargando datos del servidor...")
            
            # Obtener todos los platos del backend
            result = self.api_client.get_all_dishes()
            
            # Verificar si result es un dict con estructura correcta
            if isinstance(result, dict) and result.get('success'):
                dishes = result.get('data', [])
                
                if dishes:
                    self.records_data = [
                        {
                            "id": dish.get("id"),
                            "name": dish.get("nombre"),
                            "price": str(dish.get("precio", "0.00")),
                            "date": str(dish.get("fecha_creacion", "")) if dish.get("fecha_creacion") else "",
                            "image_url": dish.get("imagen_url", ""),
                            "image_path": ""  # No hay path local inicialmente
                        }
                        for dish in dishes
                    ]
                    
                    # Cargar primer registro
                    if self.records_data:
                        self.current_record_index = 0
                        self.load_record(0)
                        self.statusBar().showMessage(f"✅ {len(self.records_data)} platos cargados", 3000)
                else:
                    self.records_data = []
                    self.current_record_index = -1
                    self.form_fields.clear_data()
                    self.image_viewer.clear_image()
                    self.toolbar.update_navigation_label(0, 0)
                    self.statusBar().showMessage("⚠️ No hay platos en el menú", 5000)
            else:
                error_msg = result.get('error', 'El backend no está disponible') if isinstance(result, dict) else 'Respuesta inválida del servidor'
                self.statusBar().showMessage(f"❌ {error_msg}", 5000)
                QMessageBox.warning(
                    self,
                    "Error de Conexión",
                    f"No se pudo conectar con el servidor.\n\n{error_msg}"
                )
                
        except Exception as e:
            self.statusBar().showMessage(f"❌ Error: {str(e)}", 5000)
            QMessageBox.warning(
                self,
                "Sin Conexión",
                "El backend no está ejecutándose.\n\nInicia el servidor primero."
            )
        finally:
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
    
    def load_record(self, index):
        """Carga un registro en el formulario"""
        if 0 <= index < len(self.records_data):
            self.current_record_index = index
            record = self.records_data[index]
            
            # Cargar datos en el formulario
            self.form_fields.set_data(
                name=record.get("name", ""),
                price=record.get("price", ""),
                date=record.get("date", "")
            )
            
            # Cargar imagen desde URL o path local
            image_url = record.get("image_url", "")
            image_path = record.get("image_path", "")
            
            if image_path:
                # Si hay path local, usar ese
                self.image_viewer.load_image(image_path)
            elif image_url:
                # Si hay URL, cargar desde URL
                self.image_viewer.load_image_from_url(image_url)
            else:
                self.image_viewer.clear_image()
            
            # Actualizar contador de navegación
            self.toolbar.update_navigation_label(index + 1, len(self.records_data))
    
    def handle_add_record(self):
        """Maneja la acción de agregar un nuevo registro"""
        data = self.form_fields.get_data()
        
        # Validar datos
        if not data.get("name") or not data.get("price"):
            QMessageBox.warning(
                self,
                "Datos Incompletos",
                "Por favor completa al menos el nombre y precio del plato."
            )
            return
        
        # Validar que el precio sea un número válido
        try:
            precio_float = float(data.get("price", 0).replace(',', '.'))
            if precio_float <= 0:
                QMessageBox.warning(
                    self,
                    "Precio Inválido",
                    "El precio debe ser mayor a 0."
                )
                return
        except ValueError:
            QMessageBox.warning(
                self,
                "Precio Inválido",
                "Por favor ingresa un precio válido (número)."
            )
            return
        
        try:
            self.setCursor(QCursor(Qt.CursorShape.WaitCursor))
            self.statusBar().showMessage("⏳ Agregando plato...")
            
            # Obtener la imagen del visor
            image_path = self.image_viewer.get_current_image_path()
            
            # Llamar al API con la imagen
            if image_path:
                # Subir con archivo local
                result = self.api_client.create_dish(
                    nombre=data.get("name"),
                    precio=precio_float,
                    imagen_path=image_path
                )
            else:
                # Si no hay imagen, usar placeholder
                result = self.api_client.create_dish(
                    nombre=data.get("name"),
                    precio=precio_float,
                    imagen_url="https://via.placeholder.com/400"
                )
            
            if result.get('success'):
                self.statusBar().showMessage("✅ Plato agregado exitosamente", 3000)
                QMessageBox.information(
                    self,
                    "Éxito",
                    f"El plato '{data.get('name')}' fue agregado correctamente."
                )
                # Recargar datos
                self.load_data_from_backend()
                
                # Ir al último registro (el recién creado)
                if self.records_data:
                    self.current_record_index = len(self.records_data) - 1
                    self.load_record(self.current_record_index)
            else:
                error_msg = result.get('error', 'Error desconocido')
                self.statusBar().showMessage(f"❌ Error al agregar: {error_msg}", 5000)
                
                # Mensaje específico para plato duplicado
                if 'ya existe' in error_msg.lower():
                    QMessageBox.warning(
                        self,
                        "Plato Duplicado",
                        f"Ya existe un plato con ese nombre en el menú.\n\n{error_msg}"
                    )
                else:
                    QMessageBox.critical(
                        self,
                        "Error",
                        f"No se pudo agregar el plato.\n\nError: {error_msg}"
                    )
            
        except Exception as e:
            self.statusBar().showMessage(f"❌ Error al agregar: {str(e)}", 5000)
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo agregar el plato.\n\nError: {str(e)}"
            )
        finally:
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
    
    def handle_edit_record(self):
        """Maneja la acción de modificar el registro actual"""
        if not self.records_data:
            QMessageBox.warning(self, "Sin Registros", "No hay platos para modificar.")
            return
        
        data = self.form_fields.get_data()
        current_record = self.records_data[self.current_record_index]
        dish_id = current_record.get("id")
        
        if not dish_id:
            QMessageBox.warning(self, "Error", "No se puede identificar el plato.")
            return
        
        # Validar datos
        if not data.get("name") or not data.get("price"):
            QMessageBox.warning(
                self,
                "Datos Incompletos",
                "Por favor completa al menos el nombre y precio del plato."
            )
            return
        
        # Validar que el precio sea un número válido
        try:
            precio_float = float(data.get("price", 0).replace(',', '.'))
            if precio_float <= 0:
                QMessageBox.warning(
                    self,
                    "Precio Inválido",
                    "El precio debe ser mayor a 0."
                )
                return
        except ValueError:
            QMessageBox.warning(
                self,
                "Precio Inválido",
                "Por favor ingresa un precio válido (número)."
            )
            return
        
        try:
            self.setCursor(QCursor(Qt.CursorShape.WaitCursor))
            self.statusBar().showMessage("⏳ Actualizando plato...")
            
            # Obtener la imagen del visor
            image_path = self.image_viewer.get_current_image_path()
            
            # Determinar si es un archivo local o una URL
            is_local_file = image_path and not image_path.startswith(('http://', 'https://'))
            
            # Llamar al API
            if is_local_file:
                # Si hay una nueva imagen local, subirla
                result = self.api_client.update_dish(
                    dish_id=dish_id,
                    nombre=data.get("name"),
                    precio=precio_float,
                    imagen_path=image_path
                )
            else:
                # Mantener la URL actual (ya está en Cloudinary)
                result = self.api_client.update_dish(
                    dish_id=dish_id,
                    nombre=data.get("name"),
                    precio=precio_float,
                    imagen_url=image_path if image_path else current_record.get("image_url", "")
                )
            
            if result.get('success'):
                self.statusBar().showMessage("✅ Plato actualizado exitosamente", 3000)
                QMessageBox.information(
                    self,
                    "Éxito",
                    f"El plato '{data.get('name')}' fue actualizado correctamente."
                )
                # Recargar datos
                self.load_data_from_backend()
                
                # Buscar y mostrar el plato actualizado
                if self.records_data:
                    for i, record in enumerate(self.records_data):
                        if record.get('id') == dish_id:
                            self.current_record_index = i
                            self.load_record(self.current_record_index)
                            break
            else:
                error_msg = result.get('error', 'Error desconocido')
                self.statusBar().showMessage(f"❌ Error al actualizar: {error_msg}", 5000)
                QMessageBox.critical(
                    self,
                    "Error",
                    f"No se pudo actualizar el plato.\n\nError: {error_msg}"
                )
            
        except Exception as e:
            self.statusBar().showMessage(f"❌ Error al actualizar: {str(e)}", 5000)
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo actualizar el plato.\n\nError: {str(e)}"
            )
        finally:
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
    
    def handle_delete_record(self):
        """Maneja la acción de eliminar el registro actual"""
        if not self.records_data:
            QMessageBox.warning(self, "Sin Registros", "No hay platos para eliminar.")
            return
        
        current_record = self.records_data[self.current_record_index]
        dish_id = current_record.get("id")
        dish_name = current_record.get("name")
        
        if not dish_id:
            QMessageBox.warning(self, "Error", "No se puede identificar el plato.")
            return
        
        # Confirmación
        reply = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Estás seguro de eliminar el plato '{dish_name}'?\n\nEsta acción no se puede deshacer.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply != QMessageBox.StandardButton.Yes:
            return
        
        try:
            self.setCursor(QCursor(Qt.CursorShape.WaitCursor))
            self.statusBar().showMessage("⏳ Eliminando plato...")
            
            # Enviar al backend
            result = self.api_client.delete_dish(dish_id)
            
            if result.get('success'):
                self.statusBar().showMessage("✅ Plato eliminado exitosamente", 3000)
                QMessageBox.information(
                    self,
                    "Éxito",
                    f"El plato '{dish_name}' fue eliminado correctamente."
                )
                # Recargar datos
                self.load_data_from_backend()
                
                # Ajustar navegación después de eliminar
                if not self.records_data:
                    # No hay más platos
                    self.current_record_index = -1
                    self.form_fields.clear_data()
                    self.image_viewer.clear_image()
                    self.toolbar.update_navigation_label(0, 0)
                else:
                    # Ajustar el índice si está fuera de rango
                    if self.current_record_index >= len(self.records_data):
                        self.current_record_index = len(self.records_data) - 1
                    # Cargar el plato en la posición actual
                    if self.current_record_index >= 0:
                        self.load_record(self.current_record_index)
            else:
                error_msg = result.get('error', 'Error desconocido')
                self.statusBar().showMessage(f"❌ Error al eliminar: {error_msg}", 5000)
                QMessageBox.critical(
                    self,
                    "Error",
                    f"No se pudo eliminar el plato.\n\nError: {error_msg}"
                )
            
        except Exception as e:
            self.statusBar().showMessage(f"❌ Error al eliminar: {str(e)}", 5000)
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo eliminar el plato.\n\nError: {str(e)}"
            )
        finally:
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
    
    def handle_previous_record(self):
        """Navega al registro anterior"""
        if self.current_record_index > 0:
            self.load_record(self.current_record_index - 1)
    
    def handle_next_record(self):
        """Navega al siguiente registro"""
        if self.current_record_index < len(self.records_data) - 1:
            self.load_record(self.current_record_index + 1)
    
    def handle_upload_image(self):
        """Maneja la carga de imagen local"""
        image_path = self.form_fields.open_file_dialog()
        if image_path:
            # Cargar imagen en el visor
            self.image_viewer.load_image(image_path)
            
            # Aquí se subirá a Cloudinary (backend)
            print(f"📤 Imagen seleccionada: {image_path}")
            print("TODO: Subir a Cloudinary y obtener URL")
            # TODO: Llamar a utils.cloudinary_uploader.upload(image_path)
            # TODO: Actualizar campo image_url con la URL retornada
    
    def print_record_ui(self):
        """Prepara y muestra preview de impresión del registro actual"""
        print("🖨️ ACCIÓN: Imprimir registro actual")
        
        # Obtener datos del registro actual (formulario + datos del registro)
        data = self.form_fields.get_data()

        record = self.records_data[self.current_record_index]

        # Preparar documento para impresión
        document_data = {
            "name": data.get("name", "Sin nombre"),
            "price": f"${data.get('price', '0.00')}",
            "date": data.get("date", ""),
            "image_path": record.get("image_path", ""),
            "image_url": record.get("image_url", "")
        }
        
        # Llamar al gestor de impresión
        PrintManager.print_document(document_data)
