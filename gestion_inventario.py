# gestion_inventario.py

import mysql.connector

class InventarioRepository:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def crear_producto(self, nombre, descripcion, precio, cantidad_disponible):
        query = "INSERT INTO Productos (Nombre, Descripcion, Precio, CantidadDisponible) VALUES (%s, %s, %s, %s)"
        values = (nombre, descripcion, precio, cantidad_disponible)
        self.cursor.execute(query, values)
        self.connection.commit()

    def obtener_producto_por_id(self, producto_id):
        query = "SELECT * FROM Productos WHERE ID = %s"
        self.cursor.execute(query, (producto_id,))
        return self.cursor.fetchone()

    def actualizar_cantidad_disponible(self, producto_id, nueva_cantidad):
        query = "UPDATE Productos SET CantidadDisponible = %s WHERE ID = %s"
        values = (nueva_cantidad, producto_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def actualizar_informacion_producto(self, producto_id, precio, descripcion):
        query = "UPDATE Productos SET Precio = %s, Descripcion = %s WHERE ID = %s"
        values = (precio, descripcion, producto_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def eliminar_producto(self, producto_id):
        query = "DELETE FROM Productos WHERE ID = %s"
        self.cursor.execute(query, (producto_id,))
        self.connection.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
