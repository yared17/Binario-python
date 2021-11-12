#  =========== VIEW =================
## UI/UX
def viewWelcome(): ## Function dummy
  print('''Bienvenido al CONVERTIDOR de NÚMEROS
  ⭐interactivo por linea de comandos''')

def viewGoodBye():  # Function dummy
  print('''
  Saliendo del programa.
  Muchas gracias por usar el programa 👋
  Desarrollado por Yared y Andres''')

def viewAppMenu():  # UI AppMenu
  print('''
  MENU PRINCIPAL, escoga:
  [1] convertir a Decimal/Hexagecimal/Octal
  [2] convertir a Binario
  [3] salir
  ''')

## UI MENU of conversion
def viewMenuOfConversion():
  print('''
  Usted eligio convertir un NÚMERO a:
    Escoga una opción:
    [1] convertir a Decimal
    [2] convertir a Octal
    [3] convertir a Hexagecimal
  ''')

def viewUserNumber():  # Funtion dummy
    print('''Ingresa tú número.
    ''')
# ======== END-VIEW ==================

# ======== CONTROLLERS  ============= (no tengo ni idea si se llama asi para este caso)
## Funtion utils
def inputNumber():
  # Funcion que captura el numero del usuario para convertilo a la opcion que el usuario desee, no recibe parametrs, tiene que devolver un numero int
  while True:
    try:
      num = int(input('Digite a continuación: '))
      # customConditional(num)
      if type(num):  # Esta parte del codigo deberia estar dentro una funcion, para que pueda ser modificable a gusto propio
        # por ejemplo un rango de numeros etc
          print(f'Su digitación fue {num} \n')
          break
    except ValueError:
      print("Error, no ingreso un número. Intentelo de nuevo, Ingrese un número")
  return num

def converterNumber():
  viewMenuOfConversion()
  option = inputNumber()
  viewUserNumber()
  num = inputNumber()
  if option ==1:
    print('El numero {} en el convertidor para decimal es igual a {}'.format(num, num, 2))
    return viewAppMenu()
  elif option ==2:
    print('El numero {} en el convertidor para octal es igual a {}'.format(num, oct(num)))
    return viewAppMenu()
  elif option ==3:
    print('El numero {} en el convertidor para Hexagecimal es igual a {}'.format(num, hex(num)))
    return viewAppMenu()
  return

def viewMenuConversionToBinario():
  print('''Elija una opcion para convertir a numero binario"
  Escoga una opcion de conversion:
  [1] convertir de Decimal a binario
  [2] convertir de Hexagecimal a binario
  [3] convertir de octal a binario
  ''')
def conversionToBinario():
  viewMenuConversionToBinario()
  option = inputNumber()
  print("Ingrese su número decimal/octal/Hexagecimal")
  num = inputNumber()
  if option == 1:
    print('El numero {} en el convertidor de decimal a binario es igual a {}'.format(num,(int(bin(int(num))[2:]))))
  elif option == 2:
    print('El numero {} en el convertidor de octal a binario es igual a {}'.format(num, (int(bin(int(num, 8))[2:]))))
  elif option == 3:
    print('El numero {} en el convertidor de Hexagecimal a Binario es igual a {}'.format(num, (int(bin(int(num, 16))[2:]))))
  else:
    print('opcion invalida, intente nuevamente.')


def process(option):
  if option == 1:
      converterNumber()
      return
  if option == 2:
      conversionToBinario()
      return
  if option == 3:
      viewGoodBye()
      return
  else:
    print("Opicion no valida")

## ===== FUNCTION MAIN ======
def main():
  viewWelcome()
  option = 0
  viewAppMenu()
  while option != 3:
      option = inputNumber()
      process(option)

## LLAMADA A LA APP
main()
