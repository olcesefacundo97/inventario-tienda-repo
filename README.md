# Sistema de Gestión de Inventario para Tienda en Línea

Este proyecto es una aplicación de gestión de inventario para una tienda en línea. Permite realizar operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos de productos.

## Configuración

1. **Base de Datos:**
   - Asegúrate de tener un servidor de base de datos (por ejemplo, MySQL) instalado.
   - Crea una nueva base de datos llamada `InventarioTienda` (o el nombre que hayas elegido).

2. **Esquema de la Base de Datos:**
   - Ejecuta el script SQL en `esquema.sql` para crear la tabla `Productos`.

3. **Configuración de la Aplicación:**
   - Asegúrate de tener Python 3.x instalado.
   - Configura la conexión a la base de datos en el archivo `configuracion.py` (o el equivalente según el lenguaje).

## Operaciones Disponibles

- **Crear Producto:** Agrega un nuevo producto al inventario.
- **Leer Información del Producto:** Consulta detalles sobre un producto específico.
- **Actualizar Cantidad Disponible:** Modifica la cantidad disponible de un producto.
- **Actualizar Información del Producto:** Actualiza el precio o la descripción de un producto.
- **Eliminar Producto:** Elimina un producto del inventario.

## Ejemplos de Uso

```python
# Ejemplo en Python utilizando el módulo de gestión de inventario
from gestion_inventario import InventarioRepository

# Crear un nuevo producto
InventarioRepository.crear_producto('Nuevo Producto', 'Descripción del Nuevo Producto', 29.99, 50)

# Obtener información del producto con ID 1
producto = InventarioRepository.obtener_producto_por_id(1)
print(producto)

# Actualizar la cantidad disponible del producto con ID 1
InventarioRepository.actualizar_cantidad_disponible(1, 40)

# Eliminar el producto con ID 2
InventarioRepository.eliminar_producto(2)
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias de mejora, por favor crea un *issue* o envía un *pull request*.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE.md](LICENSE.md) para más detalles.
