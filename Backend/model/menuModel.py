import mysql.connector


class MenuModel:
    def __init__(self, conn):
        self.conn = conn
        
    
    def _validate_data(self, data, required_fields):
        missing_fields = [fields for fields in required_fields \
            if fields not in data or data[fields] is None]
        if missing_fields:
            raise ValueError(f"Faltan campos requeridos: {', '.join(missing_fields)}")
        if 'precio' in data:
            try:
                precio = float(data["precio"])
            except (ValueError, TypeError):
                # Captura si el valor no se puede convertir a número
                raise ValueError("El precio debe ser un valor numérico válido.")
            
            if precio < 0:
                # Ahora la comprobación es directa
                raise ValueError("El precio no puede ser negativo.")
            
        return True
        
                
     
        
    
    def get_all(self):
        cursor = None
        try:
            cursor = self.conn.connection.cursor(dictionary=True)
            query = "SELECT * FROM menu"
            cursor.execute(query)
            data = cursor.fetchall()
            return {
                "code": 200,
                "data": data,
                "message": "OK"
            }
        except Exception as e: 
            print(f"Error al obtener los datos del menú: {e}")
            return {
                "code": 500,
                "message": f"Error al obtener los datos del menú: {e}"
                }
        finally:
            if cursor:
                cursor.close()
            
    def get_by_id(self, id):
        cursor = None
        try:
            self._validate_data({"id": id}, ["id"])
            cursor = self.conn.connection.cursor(dictionary=True)
            query = "SELECT * FROM menu WHERE id = %s"
            cursor.execute(query, (id,))
            data = cursor.fetchone()
            if data is not None:
                return {
                    "code": 200,
                    "data": data,
                    "message": "OK"
                }
            return {
                "code": 404,
                "message": "Elemento no encontrado"
            }
        
        except Exception as e: 
            return {
                "code": 500,
                "message": f"Error al obtener el elemento: {e}"
            
            }
        finally:
            if cursor:
                cursor.close()
            
    def get_by_name(self, nombre):
        cursor = None
        try:
            cursor = self.conn.connection.cursor(dictionary=True)
            query = "SELECT * FROM menu WHERE nombre = %s"
            cursor.execute(query, (nombre,))
            data = cursor.fetchone()
            if data is not None:
                return {
                    "code": 200,
                    "data": data,
                    "message": "OK"
                }
            return {
                "code": 404,
                "message": "Elemento no encontrado"
            }
        
        except Exception as e: 
            return {
                "code": 500,
                "message": f"Error al buscar el elemento: {e}"
            
            }
        finally:
            if cursor:
                cursor.close()
    
    def create_dish(self, data):
        cursor = None
        try:
            self._validate_data(data, ["nombre", "precio", "imagen_url"])
            cursor = self.conn.connection.cursor()
            query = "INSERT INTO menu (nombre, precio, imagen_url) \
                    VALUES (%s, %s, %s)"
            nombre = data.get("nombre")
            precio = data.get("precio")
            imagen_url = data.get("imagen_url")
            cursor.execute(query, (nombre, precio, imagen_url))
            self.conn.connection.commit()
            return {
                "code": 201,
                "message": "Plato creado exitosamente"
            }
        except ValueError as ve:
            return {"code": 400, "message": str(ve)}
        except mysql.connector.Error as db_err:
            self.conn.connection.rollback()
            return {
                "code": 500,
                "message": f"Error de base de datos al crear el plato: {db_err}"
            }
        except Exception as e:
            self.conn.connection.rollback()
            return {
                "code": 500,
                "message": f"Error interno inesperado: {e}"
            }
        finally:
            if cursor:
                cursor.close()
            
    
    def update_dish(self, id, data):
        cursor = None
        try:
            # Verificar si existe primero para distinguir entre "no encontrado" y "sin cambios"
            check_cursor = self.conn.connection.cursor()
            check_cursor.execute("SELECT id FROM menu WHERE id = %s", (id,))
            if not check_cursor.fetchone():
                check_cursor.close()
                return {
                    "code": 404,
                    "message": "Elemento no encontrado"
                }
            check_cursor.close()

            self._validate_data({"id": id}, ["id"])
            self._validate_data(data, ["nombre", "precio", "imagen_url"])
            cursor = self.conn.connection.cursor()
            query = "UPDATE  menu \
                    SET nombre = %s, precio = %s, imagen_url = %s \
                    WHERE id = %s"
            nombre = data.get("nombre")
            precio = data.get("precio")
            imagen_url = data.get("imagen_url")
            cursor.execute(query, (nombre, precio, imagen_url, id))
            self.conn.connection.commit()
            
            # Si llegamos aquí, el registro existe. 
            # rowcount=0 solo significa que no hubo cambios en los datos.
            return {
                "code": 200,
                "message": "Plato actualizado exitosamente"
            }
        except ValueError as ve:
            return {"code": 400, "message": str(ve)}
        except mysql.connector.Error as db_err:
            self.conn.connection.rollback()
            return {
                "code": 500,
                "message": f"Error de base de datos al actualizar el plato: {db_err}"
            }
        except Exception as e:
            self.conn.connection.rollback()
            return {
                "code": 500,
                "message": f"Error interno inesperado:: {e}"
            }
        finally:
            if cursor:
                cursor.close()
                
    
    def delete_dish(self, id):
        cursor = None
        try:
            self._validate_data({"id": id}, ["id"])
            cursor = self.conn.connection.cursor()
            query = "DELETE FROM menu WHERE id = %s"
            cursor.execute(query, (id,))
            self.conn.connection.commit()
            if cursor.rowcount == 0:
                return {
                    "code": 404,
                    "message": "Elemento no encontrado"
                }
            return {
                "code": 200,
                "message": "Plato eliminado exitosamente"
                }
        
        except ValueError as ve:
            return {"code": 400, "message": str(ve)}
        except mysql.connector.Error as db_err:
            self.conn.connection.rollback()
            return {
                "code": 500,
                "message": f"Error de base de datos al eliminar el plato: {db_err}"
            }
        except Exception as e:
            self.conn.connection.rollback()
            return {
                "code": 500,
                "message": f"Error interno inesperado: {e}"
            }
        finally:
            if cursor:
                cursor.close() 
            

            
            
                
                