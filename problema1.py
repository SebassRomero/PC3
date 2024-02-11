while (True):
    try :
       x = int(input('Ingrese el primer número: '))
       y = int(input('Ingrese el segundo número: '))
       if x==y:
          print('F')
       if x > y:
          print('El primer numero No debe ser mayor')
          continue
       else:
          print(f'{(x/y)*100} %')
    except ZeroDivisionError:
       print('El segundo número NO debe ser cero')
    except ValueError:
       print('Los numeros deben ser enteros')  
    else: 
       print('Todo ha funcionado correctamente')
       break
       
    