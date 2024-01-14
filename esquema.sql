-- esquema.sql

CREATE DATABASE IF NOT EXISTS InventarioTienda;

USE InventarioTienda;

CREATE TABLE Productos (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Descripcion TEXT,
    Precio DECIMAL(10, 2) NOT NULL,
    CantidadDisponible INT NOT NULL
);