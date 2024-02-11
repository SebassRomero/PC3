def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Introduce las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Por favor, asegúrate de ingresar solo números separados por comas.")

if __name__ == "__main__":
    try:
        calificaciones_usuario = obtener_calificaciones()
        print("Calificaciones ingresadas:", calificaciones_usuario)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")