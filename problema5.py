class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {', '.join(map(str, self.notas))}")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

if __name__ == "__main__":
    try:
        nombre_alumno = input("Introduce el nombre del estudiante: ")
        registro_alumno = input("Introduce el número de registro del estudiante: ")

        alumno = Alumno(nombre_alumno, registro_alumno)

        while True:
            try:
                edad_alumno = int(input("Introduce la edad del estudiante: "))
                alumno.set_edad(edad_alumno)
                break
            except ValueError:
                print("Error: Por favor, introduce una edad válida (número entero).")

        while True:
            try:
                notas_alumno = [float(nota) for nota in input("Introduce las notas del estudiante separadas por comas: ").split(',')]
                alumno.set_notas(notas_alumno)
                break
            except ValueError:
                print("Error: Por favor, introduce notas válidas (números).")

        print("\nInformación del Estudiante:")
        alumno.display()
    except ValueError:
       print('Introducir los datos corrrectamente')