from flask import request, jsonify
import re
from utils.cloudinary_config import CloudinaryConfig


class MenuController:
    def __init__(self, menu_model):
        self.menu_model = menu_model
        self.cloudinary = CloudinaryConfig()
    
    def _sanitize_string(self, value, max_length=100):
        """
        Sanitiza strings para prevenir inyecciones y XSS
        """
        if not isinstance(value, str):
            return str(value)
        
        # Eliminar caracteres peligrosos
        value = value.strip()
        
        # Limitar longitud
        value = value[:max_length]
        
        # Escapar caracteres especiales HTML
        value = (value
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#x27;'))
        
        return value
    
    def _validate_price(self, precio):
        """
        Valida que el precio sea un número válido y positivo
        """
        try:
            precio_float = float(precio)
            if precio_float < 0:
                return False, "El precio no puede ser negativo"
            if precio_float > 999999.99:
                return False, "El precio excede el límite máximo"
            return True, precio_float
        except (ValueError, TypeError):
            return False, "El precio debe ser un número válido"
    
    def _validate_url(self, url):
        """
        Valida que sea una URL segura (http/https)
        """
        if not url:
            return False, "La URL de la imagen es requerida"
        
        # Patrón básico para URLs HTTP/HTTPS
        url_pattern = re.compile(
            r'^https?://'  # http:// o https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # dominio
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...o IP
            r'(?::\d+)?'  # puerto opcional
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        if not url_pattern.match(url):
            return False, "URL inválida. Debe ser una URL HTTP/HTTPS válida"
        
        return True, url
    
    def _validate_id(self, id_value):
        """
        Valida que el ID sea un entero positivo
        """
        try:
            id_int = int(id_value)
            if id_int <= 0:
                return False, "El ID debe ser un número positivo"
            return True, id_int
        except (ValueError, TypeError):
            return False, "El ID debe ser un número entero válido"
    
    def get_all_dishes(self):
        """
        Obtiene todos los platos del menú
        GET /menu
        """
        try:
            result = self.menu_model.get_all()
            return jsonify(result), result.get('code', 500)
        except Exception as e:
            return jsonify({
                "code": 500,
                "message": f"Error interno del servidor: {str(e)}"
            }), 500
    
    def get_dish_by_id(self, dish_id):
        """
        Obtiene un plato específico por ID
        GET /menu/<id>
        """
        try:
            # Validar ID
            is_valid, validated_id = self._validate_id(dish_id)
            if not is_valid:
                return jsonify({
                    "code": 400,
                    "message": validated_id
                }), 400
            
            result = self.menu_model.get_by_id(validated_id)
            return jsonify(result), result.get('code', 500)
        except Exception as e:
            return jsonify({
                "code": 500,
                "message": f"Error interno del servidor: {str(e)}"
            }), 500
    
    def create_dish(self):
        """
        Crea un nuevo plato en el menú
        POST /menu
        Body: {
            "nombre": "string",
            "precio": number,
            "imagen_url": "string" (opcional si se envía archivo)
        }
        O con multipart/form-data para subir imagen
        """
        try:
            # Obtener datos del request
            if request.is_json:
                data = request.get_json()
            else:
                data = request.form.to_dict()
            
            # Validar campos requeridos
            if not data.get('nombre'):
                return jsonify({
                    "code": 400,
                    "message": "El nombre del plato es requerido"
                }), 400
            
            if not data.get('precio'):
                return jsonify({
                    "code": 400,
                    "message": "El precio es requerido"
                }), 400
            
            # Sanitizar nombre
            nombre = self._sanitize_string(data['nombre'], max_length=100)
            if not nombre:
                return jsonify({
                    "code": 400,
                    "message": "El nombre del plato no puede estar vacío"
                }), 400
            
            # Verificar que no exista un plato con el mismo nombre
            existing_dish = self.menu_model.get_by_name(nombre)
            if existing_dish.get('code') == 200 and existing_dish.get('data'):
                return jsonify({
                    "code": 409,
                    "message": f"Ya existe un plato con el nombre '{nombre}' en el menú"
                }), 409
            
            # Validar precio
            is_valid, precio = self._validate_price(data['precio'])
            if not is_valid:
                return jsonify({
                    "code": 400,
                    "message": precio
                }), 400
            
            # Manejar imagen
            imagen_url = None
            
            # Si hay un archivo en el request
            if 'imagen' in request.files:
                file = request.files['imagen']
                if file.filename:
                    # Validar tipo de archivo
                    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                    file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
                    
                    if file_ext not in allowed_extensions:
                        return jsonify({
                            "code": 400,
                            "message": f"Formato de imagen no permitido. Use: {', '.join(allowed_extensions)}"
                        }), 400
                    
                    # Subir a Cloudinary
                    upload_result = CloudinaryConfig.upload_image(file)
                    
                    if not upload_result.get('success'):
                        return jsonify({
                            "code": 500,
                            "message": upload_result.get('error', 'Error al subir imagen')
                        }), 500
                    
                    imagen_url = upload_result['url']
            
            # Si no hay archivo pero sí URL
            elif data.get('imagen_url'):
                is_valid, validated_url = self._validate_url(data['imagen_url'])
                if not is_valid:
                    return jsonify({
                        "code": 400,
                        "message": validated_url
                    }), 400
                imagen_url = validated_url
            else:
                return jsonify({
                    "code": 400,
                    "message": "Debe proporcionar una imagen (archivo o URL)"
                }), 400
            
            # Crear plato
            dish_data = {
                "nombre": nombre,
                "precio": precio,
                "imagen_url": imagen_url
            }
            
            result = self.menu_model.create_dish(dish_data)
            return jsonify(result), result.get('code', 500)
            
        except Exception as e:
            return jsonify({
                "code": 500,
                "message": f"Error interno del servidor: {str(e)}"
            }), 500
    
    def update_dish(self, dish_id):
        """
        Actualiza un plato existente
        PUT /menu/<id>
        Body: {
            "nombre": "string",
            "precio": number,
            "imagen_url": "string" (opcional si se envía archivo)
        }
        """
        try:
            # Validar ID
            is_valid, validated_id = self._validate_id(dish_id)
            if not is_valid:
                return jsonify({
                    "code": 400,
                    "message": validated_id
                }), 400
            
            # Obtener datos del request
            if request.is_json:
                data = request.get_json()
            else:
                data = request.form.to_dict()
            
            # Validar campos requeridos
            if not data.get('nombre'):
                return jsonify({
                    "code": 400,
                    "message": "El nombre del plato es requerido"
                }), 400
            
            if not data.get('precio'):
                return jsonify({
                    "code": 400,
                    "message": "El precio es requerido"
                }), 400
            
            # Sanitizar nombre
            nombre = self._sanitize_string(data['nombre'], max_length=100)
            if not nombre:
                return jsonify({
                    "code": 400,
                    "message": "El nombre del plato no puede estar vacío"
                }), 400
            
            # Validar precio
            is_valid_price, precio = self._validate_price(data['precio'])
            if not is_valid_price:
                return jsonify({
                    "code": 400,
                    "message": precio
                }), 400
            
            # Obtener plato actual para manejar imagen antigua
            current_dish = self.menu_model.get_by_id(validated_id)
            old_imagen_url = None
            if current_dish.get('code') == 200 and current_dish.get('data'):
                old_imagen_url = current_dish['data'].get('imagen_url')
            
            # Manejar nueva imagen
            imagen_url = None
            
            # Si hay un archivo nuevo en el request
            if 'imagen' in request.files:
                file = request.files['imagen']
                if file.filename:
                    # Validar tipo de archivo
                    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                    file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
                    
                    if file_ext not in allowed_extensions:
                        return jsonify({
                            "code": 400,
                            "message": f"Formato de imagen no permitido. Use: {', '.join(allowed_extensions)}"
                        }), 400
                    
                    # Subir nueva imagen a Cloudinary
                    upload_result = CloudinaryConfig.upload_image(file)
                    
                    if not upload_result.get('success'):
                        return jsonify({
                            "code": 500,
                            "message": upload_result.get('error', 'Error al subir imagen')
                        }), 500
                    
                    imagen_url = upload_result['url']
                    
                    # Eliminar imagen antigua de Cloudinary si existe
                    if old_imagen_url and 'cloudinary.com' in old_imagen_url:
                        old_public_id = CloudinaryConfig.extract_public_id(old_imagen_url)
                        if old_public_id:
                            CloudinaryConfig.delete_image(old_public_id)
            
            # Si no hay archivo pero sí URL nueva
            elif data.get('imagen_url'):
                is_valid_url, validated_url = self._validate_url(data['imagen_url'])
                if not is_valid_url:
                    return jsonify({
                        "code": 400,
                        "message": validated_url
                    }), 400
                imagen_url = validated_url
            
            # Si no se proporciona nueva imagen, mantener la antigua
            elif old_imagen_url:
                imagen_url = old_imagen_url
            else:
                return jsonify({
                    "code": 400,
                    "message": "Debe proporcionar una imagen (archivo o URL)"
                }), 400
            
            # Actualizar plato
            dish_data = {
                "nombre": nombre,
                "precio": precio,
                "imagen_url": imagen_url
            }
            
            result = self.menu_model.update_dish(validated_id, dish_data)
            return jsonify(result), result.get('code', 500)
            
        except Exception as e:
            return jsonify({
                "code": 500,
                "message": f"Error interno del servidor: {str(e)}"
            }), 500
    
    def delete_dish(self, dish_id):
        """
        Elimina un plato del menú
        DELETE /menu/<id>
        """
        try:
            # Validar ID
            is_valid, validated_id = self._validate_id(dish_id)
            if not is_valid:
                return jsonify({
                    "code": 400,
                    "message": validated_id
                }), 400
            
            # Obtener plato para eliminar imagen de Cloudinary
            current_dish = self.menu_model.get_by_id(validated_id)
            
            # Eliminar del modelo
            result = self.menu_model.delete_dish(validated_id)
            
            # Si se eliminó exitosamente, eliminar imagen de Cloudinary
            if result.get('code') == 200:
                if current_dish.get('code') == 200 and current_dish.get('data'):
                    imagen_url = current_dish['data'].get('imagen_url')
                    if imagen_url and 'cloudinary.com' in imagen_url:
                        public_id = CloudinaryConfig.extract_public_id(imagen_url)
                        if public_id:
                            CloudinaryConfig.delete_image(public_id)
            
            return jsonify(result), result.get('code', 500)
            
        except Exception as e:
            return jsonify({
                "code": 500,
                "message": f"Error interno del servidor: {str(e)}"
            }), 500
