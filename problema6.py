class Producto:
    def __init__(self, nombre, tipo, precio, año):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - ${self.precio} - Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_lista_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        try:
            año = int(año)
            productos_filtrados = [producto for producto in self.productos if producto.año == año]
            return productos_filtrados
        except ValueError:
            print("Error: Por favor, introduce un año válido (número entero).")
            return []

    def filtrar_por_tipo(self, tipo):
        productos_filtrados = [producto for producto in self.productos if producto.tipo.lower() == tipo.lower()]
        return productos_filtrados


if __name__ == "__main__":
    catalogo = Catalogo()

    try:
        producto1 = Producto("Filtro de aceite", "Filtros", 15.99, 2022)
        producto2 = Producto("Pastillas de freno", "Frenos", 39.99, 2021)
        producto3 = Producto("Batería de automóvil", "Baterías", 89.99, 2022)

        catalogo.agregar_producto(producto1)
        catalogo.agregar_producto(producto2)
        catalogo.agregar_producto(producto3)

        print("Lista completa de productos:")
        catalogo.mostrar_lista_productos()

        año_filtro = input("\nIntroduce el año para filtrar: ")
        productos_filtrados_por_año = catalogo.filtrar_por_año(año_filtro)
        print(f"\nProductos del año {año_filtro}:")
        for producto in productos_filtrados_por_año:
            print(producto)

        tipo_filtro = input("\nIntroduce el tipo para filtrar: ")
        productos_filtrados_por_tipo = catalogo.filtrar_por_tipo(tipo_filtro)
        print(f"\nProductos de la categoría '{tipo_filtro}':")
        for producto in productos_filtrados_por_tipo:
            print(producto)
        
    except ValueError:
        print("Error: Por favor, introduce el valor corretacmente.")
    