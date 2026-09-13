import logging
from pathlib import Path


# ===========================================================
# CONFIGURACIÓN DEL LOGGER
# ===========================================================

# Obtiene la carpeta donde está ubicado este archivo Python
ruta_log = Path(__file__).parent / "tienda.log"

logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


# ===========================================================
# CLASE PRODUCTO
# ===========================================================

class Producto:

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:,.2f}"
        )


# ===========================================================
# CLASE TIENDA
# ===========================================================

class Tienda:

    def __init__(self):
        self.productos = []
        self.siguiente_id = 1

        logger.info("Sistema iniciado.")

    # --------------------------------------------------------
    # CREATE - Crear producto
    # --------------------------------------------------------

    def crear_producto(self):

        try:
            nombre = input("Ingrese el nombre del producto: ")

            precio = float(
                input("Ingrese el precio del producto: ")
            )

            producto = Producto(
                self.siguiente_id,
                nombre,
                precio
            )

            self.productos.append(producto)

            self.siguiente_id += 1

            logger.info(
                f"Producto creado - "
                f"ID: {producto.id}, "
                f"Nombre: {producto.nombre}, "
                f"Precio: {producto.precio}"
            )

            print("\nProducto creado correctamente.\n")

        except ValueError:

            logger.error(
                "Error al crear producto: "
                "el precio ingresado no es válido."
            )

            print("\nError: el precio debe ser un número.\n")

    # --------------------------------------------------------
    # READ - Mostrar productos
    # --------------------------------------------------------

    def mostrar_productos(self):

        logger.info("Se consultó la lista de productos.")

        if len(self.productos) == 0:

            print("\nNo hay productos registrados.\n")

            return

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            producto.mostrar()

        print("===============================\n")

    # --------------------------------------------------------
    # UPDATE - Actualizar producto
    # --------------------------------------------------------

    def actualizar_producto(self):

        try:

            id_producto = int(
                input("Ingrese el ID del producto: ")
            )

            for producto in self.productos:

                if producto.id == id_producto:

                    print("\nProducto encontrado.")
                    print(f"Nombre actual: {producto.nombre}")
                    print(f"Precio actual: ${producto.precio}\n")

                    nuevo_nombre = input(
                        "Ingrese el nuevo nombre: "
                    )

                    nuevo_precio = float(
                        input("Ingrese el nuevo precio: ")
                    )

                    producto.nombre = nuevo_nombre
                    producto.precio = nuevo_precio

                    logger.info(
                        f"Producto actualizado - "
                        f"ID: {producto.id}, "
                        f"Nombre: {producto.nombre}, "
                        f"Precio: {producto.precio}"
                    )

                    print(
                        "\nProducto actualizado correctamente.\n"
                    )

                    return

            logger.warning(
                f"Intento de actualizar producto inexistente - "
                f"ID: {id_producto}"
            )

            print("\nNo se encontró un producto con ese ID.\n")

        except ValueError:

            logger.error(
                "Error al actualizar producto: "
                "ID o precio inválido."
            )

            print("\nError: debe ingresar datos válidos.\n")

    # --------------------------------------------------------
    # DELETE - Eliminar producto
    # --------------------------------------------------------

    def eliminar_producto(self):

        try:

            id_producto = int(
                input("Ingrese el ID del producto: ")
            )

            for producto in self.productos:

                if producto.id == id_producto:

                    self.productos.remove(producto)

                    logger.info(
                        f"Producto eliminado - "
                        f"ID: {producto.id}, "
                        f"Nombre: {producto.nombre}"
                    )

                    print(
                        "\nProducto eliminado correctamente.\n"
                    )

                    return

            logger.warning(
                f"Intento de eliminar producto inexistente - "
                f"ID: {id_producto}"
            )

            print("\nNo se encontró un producto con ese ID.\n")

        except ValueError:

            logger.error(
                "Error al eliminar producto: "
                "ID inválido."
            )

            print("\nError: el ID debe ser un número.\n")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():

    print("================================")
    print("       SISTEMA DE TIENDA")
    print("================================")
    print("1. Crear producto")
    print("2. Mostrar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("================================")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

tienda = Tienda()

while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        tienda.crear_producto()

    elif opcion == "2":

        tienda.mostrar_productos()

    elif opcion == "3":

        tienda.actualizar_producto()

    elif opcion == "4":

        tienda.eliminar_producto()

    elif opcion == "5":

        logger.info("Sistema cerrado por el usuario.")

        print("\nPrograma finalizado.")

        break

    else:

        logger.warning(
            f"El usuario seleccionó una opción inválida: {opcion}"
        )

        print("\nOpción inválida. Intente nuevamente.\n")
        
