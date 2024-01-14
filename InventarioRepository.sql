-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS InventarioTienda;

-- Seleccionar la base de datos
USE InventarioTienda;

CREATE TABLE Productos (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Descripcion TEXT,
    Precio DECIMAL(10, 2) NOT NULL,
    CantidadDisponible INT NOT NULL
);

INSERT INTO Productos (ID, Nombre, Descripcion, Precio, CantidadDisponible)
VALUES (1, 'Producto1', 'Descripción del Producto1', 19.99, 100);

SELECT * FROM Productos WHERE ID = 1;

UPDATE Productos SET CantidadDisponible = 80 WHERE ID = 1;

UPDATE Productos SET Precio = 24.99, Descripcion = 'Nueva Descripcion' WHERE ID = 1;

DELETE FROM Productos WHERE ID = 1;

START TRANSACTION;

-- Verificar si hay suficiente cantidad disponible del producto
SELECT CantidadDisponible FROM Productos WHERE ID = 1 FOR UPDATE;

-- Realizar la venta y actualizar la cantidad disponible
UPDATE Productos SET CantidadDisponible = CantidadDisponible - 1 WHERE ID = 1;

COMMIT;