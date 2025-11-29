"""
Componente de vista previa de imagen
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from styles.colors import Colors
import requests


class ImageViewer(QWidget):
    """Widget para mostrar vista previa de imágenes"""
    
    def __init__(self):
        super().__init__()
        self.current_image_path = None
        self.init_ui()
    
    def init_ui(self):
        """Inicializa la interfaz del visor"""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Etiqueta
        label = QLabel("Vista Previa de Imagen")
        label.setObjectName("fieldLabel")
        layout.addWidget(label)
        
        # Frame contenedor de la imagen (acepta arrastrar y soltar)
        self.image_frame = QFrame()
        self.image_frame.setObjectName("imagePreview")
        self.image_frame.setAcceptDrops(True)
        
        # Asignar eventos drag & drop al frame
        self.image_frame.dragEnterEvent = self.dragEnterEvent
        self.image_frame.dropEvent = self.dropEvent
        self.image_frame.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        
        frame_layout = QVBoxLayout(self.image_frame)
        frame_layout.setContentsMargins(10, 10, 10, 10)
        
        # Label para mostrar la imagen
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(False)
        self.image_label.setStyleSheet("""
            QLabel {
                color: #8C4A33;
                font-size: 14px;
                font-style: italic;
            }
        """)
        
        frame_layout.addWidget(self.image_label)
        layout.addWidget(self.image_frame)
        
        # Mostrar placeholder inicial
        self.show_placeholder()
    
    def show_placeholder(self):
        """Muestra un placeholder cuando no hay imagen"""
        self.image_label.setText("🖼️\n\nNo hay imagen cargada\n\nArrastra y suelta una imagen aquí o haz doble clic")
        self.current_image_path = None
    
    def load_image(self, image_path):
        """Carga y muestra una imagen desde una ruta local"""
        if not image_path:
            self.show_placeholder()
            return
        
        pixmap = QPixmap(image_path)
        
        if pixmap.isNull():
            self.image_label.setText("❌\n\nError al cargar imagen")
            self.current_image_path = None
            return
        
        # Escalar imagen manteniendo aspecto según el tamaño del label
        target_w = min(600, max(200, self.image_label.width() or 400))
        target_h = min(420, max(160, self.image_label.height() or 280))
        scaled_pixmap = pixmap.scaled(
            target_w, target_h,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)
        self.current_image_path = image_path  # Guardar la ruta local
    
    def load_image_from_url(self, image_url):
        """Carga y muestra una imagen desde una URL"""
        if not image_url:
            self.show_placeholder()
            return
        
        try:
            # Descargar imagen desde URL
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            
            # Crear pixmap desde bytes
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            
            if pixmap.isNull():
                self.image_label.setText("❌\n\nError al cargar imagen desde URL")
                return
            
            # Escalar imagen manteniendo aspecto
            target_w = min(600, max(200, self.image_label.width() or 400))
            target_h = min(420, max(160, self.image_label.height() or 280))
            scaled_pixmap = pixmap.scaled(
                target_w, target_h,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            # Guardar la URL como path para poder obtenerla después
            self.current_image_path = image_url
            
        except Exception as e:
            self.image_label.setText(f"❌\n\nError al cargar imagen:\n{str(e)}")
    
    def clear_image(self):
        """Limpia la imagen actual"""
        self.show_placeholder()
    
    def get_current_image_path(self):
        """Retorna la ruta de la imagen actual"""
        return self.current_image_path

    # --- Drag & Drop handlers ---
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()
            self.load_image(path)
            event.acceptProposedAction()
        else:
            event.ignore()

    def mouseDoubleClickEvent(self, event):
        # Permitir abrir diálogo con doble clic como alternativa
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.load_image(file_path)
