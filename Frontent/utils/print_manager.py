"""
Gestor de impresión de documentos
Maneja vista previa, detección de impresoras y envío a impresión
Compatible con Windows y Linux
"""

from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog, QPrinterInfo
from PyQt6.QtGui import QPainter, QFont, QPixmap, QImage, QPageSize, QPageLayout, QColor, QPen
from PyQt6.QtCore import Qt, QRectF, QMarginsF, QRect
from PyQt6.QtWidgets import QMessageBox
from pathlib import Path
import requests


class PrintManager:
    """Clase para gestionar la impresión de registros"""
    
    @staticmethod
    def print_document(document_data):
        """
        Muestra la vista previa de impresión y permite imprimir
        
        Args:
            document_data: Dict con los datos del plato
                - name: Nombre del plato
                - price: Precio
                - date: Fecha
                - image_path: Ruta local de la imagen
                - image_url: URL de Cloudinary (opcional)
        """
        print("\n" + "="*50)
        print("📄 PREPARANDO DOCUMENTO PARA IMPRESIÓN")
        print("="*50)
        
        # Extraer datos
        name = document_data.get("name", "Sin nombre")
        price = document_data.get("price", "$0.00")
        date = document_data.get("date", "")
        image_path = document_data.get("image_path", "")
        image_url = document_data.get("image_url", "")
        
        print(f"Nombre del Plato: {name}")
        print(f"Precio: {price}")
        print(f"Fecha en menú: {date}")
        print(f"Imagen local: {image_path if image_path else 'No disponible'}")
        print(f"URL Cloudinary: {image_url if image_url else 'No disponible'}")
        
        # Detectar impresoras disponibles
        available_printers = PrintManager.get_available_printers()
        default_printer = PrintManager.get_default_printer()
        
        print(f"\n🖨️  Impresoras disponibles: {len(available_printers)}")
        for i, printer_name in enumerate(available_printers, 1):
            is_default = " (Predeterminada)" if printer_name == default_printer else ""
            print(f"   {i}. {printer_name}{is_default}")
        
        if not available_printers:
            print("⚠️  ADVERTENCIA: No se detectaron impresoras")
            QMessageBox.warning(
                None,
                "Sin Impresoras",
                "No se detectaron impresoras conectadas.\n\n"
                "Asegúrate de tener una impresora instalada y conectada."
            )
            return
        
        print("="*50)
        
        # Crear impresora con configuración óptima
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        
        # Configurar tamaño de página (Letter)
        page_size = QPageSize(QPageSize.PageSizeId.Letter)
        printer.setPageSize(page_size)
        
        # Configurar orientación (Portrait)
        page_layout = QPageLayout()
        page_layout.setPageSize(page_size)
        page_layout.setOrientation(QPageLayout.Orientation.Portrait)
        printer.setPageLayout(page_layout)
        
        # Establecer impresora predeterminada si existe
        if default_printer:
            printer.setPrinterName(default_printer)
        
        # Crear diálogo de vista previa
        preview_dialog = QPrintPreviewDialog(printer)
        preview_dialog.setWindowTitle("Vista Previa - Impresión de Plato")
        preview_dialog.resize(900, 700)
        
        # Conectar la señal de renderizado
        preview_dialog.paintRequested.connect(
            lambda p: PrintManager._render_document(p, document_data)
        )
        
        # Mostrar vista previa (modal)
        result = preview_dialog.exec()
        
        if result:
            print("✅ Vista previa cerrada - El usuario pudo imprimir desde la vista previa")
        else:
            print("❌ Vista previa cancelada")
    
    @staticmethod
    def _render_document(printer, document_data):
        """
        Renderiza el documento en el objeto printer
        
        Args:
            printer: Objeto QPrinter
            document_data: Datos del plato
        """
        painter = QPainter()
        
        if not painter.begin(printer):
            QMessageBox.critical(
                None,
                "Error de Impresión",
                "No se pudo inicializar la impresión.\n"
                "Verifica que la impresora esté disponible y encendida."
            )
            return
        
        try:
            # Configurar sistema de coordenadas lógico independiente del dispositivo
            # Usaremos un ancho lógico fijo de 816 unidades (8.5 pulgadas * 96 DPI)
            # Esto garantiza que el diseño se vea igual en cualquier impresora
            
            # 1. Obtener dimensiones físicas reales (en píxeles de la impresora)
            rect_fisico = printer.pageRect(QPrinter.Unit.DevicePixel)
            
            # 2. Definir dimensiones lógicas (Carta: 8.5" x 11")
            # Usamos 96 DPI lógicos como base para el diseño
            ancho_logico = 816  # 8.5 * 96
            
            # Calcular alto lógico manteniendo la proporción del papel físico
            if rect_fisico.width() > 0:
                ratio = rect_fisico.height() / rect_fisico.width()
            else:
                ratio = 1.2941  # Ratio por defecto (11/8.5)
                
            alto_logico = int(ancho_logico * ratio)
            
            print(f"🖨️  Dimensiones Físicas: {rect_fisico.width()}x{rect_fisico.height()} px")
            print(f"📐 Dimensiones Lógicas: {ancho_logico}x{alto_logico} unidades")
            
            # 3. Configurar el viewport (físico) y la ventana (lógica)
            # Esto hace que Qt escale automáticamente todo lo que dibujemos
            # Convertir a int explícitamente ya que setViewport requiere enteros
            painter.setViewport(
                int(rect_fisico.x()), 
                int(rect_fisico.y()), 
                int(rect_fisico.width()), 
                int(rect_fisico.height())
            )
            painter.setWindow(0, 0, ancho_logico, alto_logico)
            
            # Usar las dimensiones lógicas para el resto del código
            page_width = ancho_logico
            page_height = alto_logico
            
            # Márgenes y configuración
            margin_left = 80
            margin_right = 80
            margin_top = 40
            content_width = page_width - margin_left - margin_right
            
            # ====== ENCABEZADO PRINCIPAL ======
            # Fondo decorativo para el título (ocupa todo el ancho desde arriba)
            header_height = 100
            painter.setBrush(QColor("#8C4A33"))  # Color café/marrón
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(0, 0, int(page_width), header_height)
            
            # Título principal (centrado verticalmente en el header)
            painter.setPen(QColor("white"))
            font_title = QFont("Arial")
            font_title.setPixelSize(36)  # 36 unidades lógicas
            font_title.setBold(True)
            painter.setFont(font_title)
            title_rect = QRect(int(margin_left), 30, int(content_width), 40)
            painter.drawText(title_rect, Qt.AlignmentFlag.AlignCenter, "🍽️ MENÚ DEL RESTAURANTE")
            
            # Posición inicial: DESPUÉS del header + margen
            y_pos = header_height + margin_top
            
            # Línea decorativa después del header
            painter.setPen(QPen(QColor("#8C4A33"), 3))
            painter.drawLine(int(margin_left), int(y_pos), int(page_width - margin_right), int(y_pos))
            y_pos += 40
            
            # ====== CONFIGURACIÓN DE COLUMNAS ======
            # Definir dos columnas: Izquierda (Texto) y Derecha (Imagen)
            gutter = 40  # Espacio entre columnas
            col_width = (content_width - gutter) / 2
            
            left_col_x = margin_left
            right_col_x = margin_left + col_width + gutter
            
            # Guardar posición Y inicial para ambas columnas
            start_y_pos = y_pos
            
            # ====== COLUMNA IZQUIERDA: INFORMACIÓN ======
            current_y = start_y_pos
            
            # Título de sección
            painter.setPen(QColor("#333333"))
            font_section = QFont("Arial")
            font_section.setPixelSize(20)
            font_section.setBold(True)
            painter.setFont(font_section)
            painter.drawText(int(left_col_x), int(current_y + 20), "DETALLES DEL PLATO")
            current_y += 35
            
            # Línea separadora corta
            painter.setPen(QPen(QColor("#CCCCCC"), 1))
            painter.drawLine(int(left_col_x), int(current_y), int(left_col_x + col_width), int(current_y))
            current_y += 25
            
            # Configurar fuentes para campos
            font_label = QFont("Arial")
            font_label.setPixelSize(12)
            font_label.setBold(True)
            
            font_value = QFont("Arial")
            font_value.setPixelSize(18)
            font_value.setBold(False)
            
            font_price = QFont("Arial")
            font_price.setPixelSize(24)
            font_price.setBold(True)
            
            # --- CAMPO: NOMBRE ---
            painter.setPen(QColor("#666666"))
            painter.setFont(font_label)
            painter.drawText(int(left_col_x), int(current_y + 12), "NOMBRE DEL PLATO")
            current_y += 20
            
            painter.setPen(QColor("#000000"))
            painter.setFont(font_value)
            nombre_text = str(document_data.get("name", "Sin nombre"))
            # Usar drawText con rectángulo para permitir word-wrap si es muy largo
            name_rect = QRect(int(left_col_x), int(current_y), int(col_width), 60)
            painter.drawText(name_rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop | Qt.TextFlag.TextWordWrap, nombre_text)
            current_y += 50
            
            # --- CAMPO: PRECIO ---
            painter.setPen(QColor("#666666"))
            painter.setFont(font_label)
            painter.drawText(int(left_col_x), int(current_y + 12), "PRECIO")
            current_y += 20
            
            # Caja de precio
            precio_text = str(document_data.get("price", "$0.00"))
            price_bg_rect = QRect(int(left_col_x), int(current_y), 140, 45)
            painter.setBrush(QColor("#E8F5E9"))
            painter.setPen(QPen(QColor("#4CAF50"), 2))
            painter.drawRoundedRect(price_bg_rect, 6, 6)
            
            painter.setPen(QColor("#2E7D32"))
            painter.setFont(font_price)
            painter.drawText(price_bg_rect, Qt.AlignmentFlag.AlignCenter, precio_text)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            current_y += 65
            
            # --- CAMPO: FECHA ---
            if document_data.get("date"):
                painter.setPen(QColor("#666666"))
                painter.setFont(font_label)
                painter.drawText(int(left_col_x), int(current_y + 12), "FECHA DE INGRESO")
                current_y += 20
                
                painter.setPen(QColor("#000000"))
                painter.setFont(font_value)
                fecha_text = str(document_data.get("date", ""))
                painter.drawText(int(left_col_x), int(current_y + 18), fecha_text)
                current_y += 40

            # ====== COLUMNA DERECHA: IMAGEN ======
            image = PrintManager._load_image(document_data)
            
            if image and not image.isNull():
                # Calcular espacio disponible para imagen
                # Altura máxima: desde start_y hasta footer (menos margen)
                footer_y = int(page_height - 60)
                max_img_height = footer_y - start_y_pos - 20
                
                # Ancho máximo: ancho de columna
                max_img_width = int(col_width)
                
                # Escalar imagen manteniendo proporción
                scaled_image = image.scaled(
                    max_img_width, 
                    max_img_height, 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                
                # Centrar imagen en su columna (vertical y horizontalmente)
                img_x = int(right_col_x + (col_width - scaled_image.width()) / 2)
                img_y = int(start_y_pos) # Alinear arriba con el texto
                
                # Dibujar borde decorativo
                border_padding = 8
                border_rect = QRect(
                    img_x - border_padding,
                    img_y - border_padding,
                    scaled_image.width() + (2 * border_padding),
                    scaled_image.height() + (2 * border_padding)
                )
                
                painter.setPen(QPen(QColor("#8C4A33"), 2))
                painter.setBrush(QColor("white"))
                painter.drawRect(border_rect)
                
                # Dibujar imagen
                painter.drawImage(img_x, img_y, scaled_image)
            
            # ====== PIE DE PÁGINA ======
            footer_y = int(page_height - 60)
            
            # Línea superior del pie
            painter.setPen(QPen(QColor("#8C4A33"), 2))
            painter.drawLine(int(margin_left), footer_y, int(page_width - margin_right), footer_y)
            
            # Texto del pie
            painter.setPen(QColor("#666666"))
            font_footer = QFont("Arial")
            font_footer.setPixelSize(12)  # 12 unidades lógicas
            painter.setFont(font_footer)
            footer_text = "Documento generado por Gestor de Menú - Restaurante"
            footer_rect = QRect(int(margin_left), footer_y + 10, int(content_width), 30)
            painter.drawText(footer_rect, Qt.AlignmentFlag.AlignCenter, footer_text)
            
            # Fecha de impresión
            from datetime import datetime
            fecha_impresion = datetime.now().strftime("%d/%m/%Y %H:%M")
            font_footer_small = QFont("Arial")
            font_footer_small.setPixelSize(10)  # 10 unidades lógicas
            painter.setFont(font_footer_small)
            painter.drawText(footer_rect.adjusted(0, 15, 0, 0), Qt.AlignmentFlag.AlignCenter, 
                           f"Impreso el: {fecha_impresion}")
            
            print("📄 Documento renderizado correctamente")
            
        except Exception as e:
            QMessageBox.critical(
                None,
                "Error al Renderizar",
                f"Error al generar el documento de impresión:\n{str(e)}"
            )
            print(f"❌ Error al renderizar: {e}")
        finally:
            painter.end()
    
    @staticmethod
    def _load_image(data):
        """
        Carga la imagen desde archivo local o URL de Cloudinary
        
        Args:
            data: Datos del documento con image_path o image_url
            
        Returns:
            QImage: Imagen cargada o None si falla
        """
        # Intentar cargar desde archivo local primero
        image_path = data.get("image_path", "")
        if image_path and Path(image_path).exists():
            print(f"📷 Cargando imagen desde: {image_path}")
            return QImage(image_path)
        
        # Intentar cargar desde URL (Cloudinary)
        image_url = data.get("image_url", "")
        if image_url:
            try:
                print(f"📷 Descargando imagen desde: {image_url}")
                # Timeout reducido para evitar congelar la UI demasiado tiempo
                response = requests.get(image_url, timeout=3)
                if response.status_code == 200:
                    image = QImage()
                    if image.loadFromData(response.content):
                        print("✅ Imagen cargada desde Cloudinary")
                        return image
            except Exception as e:
                print(f"❌ Error al descargar imagen desde URL: {e}")
        
        print("⚠️  No se pudo cargar la imagen")
        return None
    
    @staticmethod
    def get_available_printers():
        """
        Obtiene la lista de impresoras disponibles en el sistema
        
        Returns:
            list: Lista de nombres de impresoras disponibles
        """
        printers = QPrinterInfo.availablePrinters()
        printer_names = [printer.printerName() for printer in printers]
        return printer_names
    
    @staticmethod
    def get_default_printer():
        """
        Obtiene la impresora predeterminada del sistema
        
        Returns:
            str: Nombre de la impresora predeterminada o None
        """
        default_printer = QPrinterInfo.defaultPrinter()
        if default_printer.isNull():
            return None
        return default_printer.printerName()
