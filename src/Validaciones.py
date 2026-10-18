#Validaciones de números enteros
def ValidarEntero(mensaje):
 while True:
  try:
    valor = int(input(mensaje))
    return valor
  except ValueError:
    print("Debe ingresar un numero entero, no aceptamos Caracteres!!!")

#Validaciones de números flotantes
def ValidarFlotante(mensaje):
 while True:
  try:
    valor = float(input(mensaje))
    return valor
  except ValueError:
    print("Debe ingresar un numero entero, no aceptamos Caracteres!!!")