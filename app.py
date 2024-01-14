# tu_codigo.py

from configuracion import configuracion
import mysql.connector # Asegúrate de tener el paquete MySQL Connector instalado

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host=configuracion['db_host'],
    user=configuracion['db_user'],
    password=configuracion['db_password']
    database=configuracion['db_name']
)

# Resto de tu código aquí...