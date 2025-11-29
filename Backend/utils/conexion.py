#credentials
import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
   _instance = None
   _is_initialized = False
   
   def __new__(cls, *args, **kwargs):
       if cls._instance is None:
           cls._instance = super().__new__(cls)
       return cls._instance
   
   def __init__(self, host, user, password, port, database):
       if DatabaseConnection._is_initialized:
           return
       
       self.host = host
       self.user = user
       self.password = password
       self.port = port
       self.database = database
       self.connection = None
       self.connect()
       DatabaseConnection._is_initialized = True
   
   def connect(self):
       try:
           self.connection = mysql.connector.connect(
               host=self.host,
               user=self.user,
               password=self.password,
               port=self.port,
               database=self.database
           )
           if self.connection.is_connected():
               print("Conexión exitosa a la base de datos")
               
       except Error as e:
           self.connection = None
           raise (f"Error al conectar a la base de datos: {e}")
           
             
       return self.connection
   
   def get_cursor(self):
       if self.connection and self.connection.is_connected():
           return self.connection.cursor()
       else:
           self.connect()
           if self.connection and self.connection.is_connected():
               return self.connection.cursor()
           raise Exception("No se pudo establecer la conexión a la base de datos")
       
       
       
   def close(self):
      if self.connection and self.connection.is_connected():
          self.connection.close()
          print("Conexión a la base de datos cerrada")
          

   

if __name__ == "__main__":
    
    DB_CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":"",
    "port": 3306,
    "database":"restaurante"
    }
    def prueba_conexion():
        conn = DatabaseConnection(**DB_CONFIG)
        cursor = conn.get_cursor()
        query = "SELECT * FROM menu"

        try:
            cursor.execute(query)
            data = cursor.fetchall()
            return {
                "status": "success",
                "code": 200,
                "data": data
            }   
        except Error as e:
            return {
                "status": "error",
                "code": 500,
                "message": str(e)
            }
            
    print(prueba_conexion())
        
