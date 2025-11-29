"""
Validadores para los campos del formulario
"""

import re
from datetime import datetime


class Validators:
    """Clase con métodos de validación de datos"""
    
    @staticmethod
    def validate_dish_name(name):
        """
        Valida el nombre del plato
        
        Args:
            name: String con el nombre
            
        Returns:
            Tuple (is_valid: bool, error_message: str)
        """
        if not name or len(name.strip()) == 0:
            return False, "El nombre del plato no puede estar vacío"
        
        if len(name) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"
        
        if len(name) > 100:
            return False, "El nombre no puede exceder 100 caracteres"
        
        return True, ""
    
    @staticmethod
    def validate_price(price):
        """
        Valida el precio
        
        Args:
            price: String con el precio
            
        Returns:
            Tuple (is_valid: bool, error_message: str)
        """
        if not price or len(price.strip()) == 0:
            return False, "El precio no puede estar vacío"
        
        # Permitir formato: 24.50 o 24,50
        price_cleaned = price.replace(',', '.')
        
        try:
            price_float = float(price_cleaned)
            
            if price_float < 0:
                return False, "El precio no puede ser negativo"
            
            if price_float > 9999.99:
                return False, "El precio es demasiado alto"
            
            return True, ""
        
        except ValueError:
            return False, "El precio debe ser un número válido"
    
    @staticmethod
    def validate_date(date_string):
        """
        Valida la fecha
        
        Args:
            date_string: String en formato YYYY-MM-DD
            
        Returns:
            Tuple (is_valid: bool, error_message: str)
        """
        if not date_string:
            return False, "La fecha no puede estar vacía"
        
        try:
            date_obj = datetime.strptime(date_string, "%Y-%m-%d")
            
            # No permitir fechas futuras
            if date_obj > datetime.now():
                return False, "La fecha no puede ser futura"
            
            return True, ""
        
        except ValueError:
            return False, "Formato de fecha inválido"
    
    @staticmethod
    def validate_image_path(path):
        """
        Valida la ruta de imagen
        
        Args:
            path: String con la ruta
            
        Returns:
            Tuple (is_valid: bool, error_message: str)
        """
        if not path:
            return True, ""  # La imagen es opcional
        
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        
        if not any(path.lower().endswith(ext) for ext in valid_extensions):
            return False, "Formato de imagen no soportado"
        
        return True, ""
    
    @staticmethod
    def validate_all(name, price, date, image_path=""):
        """
        Valida todos los campos
        
        Returns:
            Tuple (is_valid: bool, errors: dict)
        """
        errors = {}
        
        valid_name, error_name = Validators.validate_dish_name(name)
        if not valid_name:
            errors['name'] = error_name
        
        valid_price, error_price = Validators.validate_price(price)
        if not valid_price:
            errors['price'] = error_price
        
        valid_date, error_date = Validators.validate_date(date)
        if not valid_date:
            errors['date'] = error_date
        
        valid_image, error_image = Validators.validate_image_path(image_path)
        if not valid_image:
            errors['image'] = error_image
        
        return len(errors) == 0, errors
