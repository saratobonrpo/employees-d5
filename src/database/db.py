import pyodbc
from dotenv import load_dotenv
import os


load_dotenv()

class DatabaseManager:
    def __init__(self):
        try:
            self.server = os.environ.get('DB_SERVER')
            self.database = os.environ.get('DB_NAME')
            self.username = os.environ.get('DB_USER')
            self.password = os.environ.get('DB_PASSWORD')
            self.conn = pyodbc.connect (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server},1433;DATABASE={self.database};UID={self.username};PWD={self.password};Encrypt=no;TrustServerCertificate=no;Connection Timeout=60;"
                )
            print('Conexión exitosa')

        except Exception as e:
            print('Error al conectarse: ', e)


    def execute_query(self, query, parameters=None, commit=False):
        cursor = self.conn.cursor()
        
        try:
            if commit:
                cursor.execute(query, parameters)
                self.conn.commit()
            else:
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)

                result = cursor.fetchall()  
                return result
    
        except Exception as e:
            self.conn.rollback()
            print ("Error ejecutando", e)
            raise e
        
        finally:
            cursor.close() 
    

connection = DatabaseManager()