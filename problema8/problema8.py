import random
class modulo:
 def generar_numeros_aleatorios(cantidad):
    return [random.randint(0, 100) for _ in range(cantidad)]

 def mostrar_lista(lista):
    print("Lista de números:")
    print(lista)

 def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    

    lista_numeros = modulo.generar_numeros_aleatorios(20)

    modulo.mostrar_lista(lista_numeros)

    modulo.ordenar_y_mostrar(lista_numeros)