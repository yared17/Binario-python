from os import system, name
from typing import Optional
# Funcion que permite limpiar la consola
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


Binario=int(input('Digite un numero para su conversion: '))
print(''' Escoga una base de conversion:
[1] convertir a Decimal
[2] convertir a Hexagecimal
[3] convertir a octal
''')

opcion = int(input('Opcion: '))
if opcion ==1:
   print('El numero {} en el convertidor para decimal es igual a {}'.format(Binario,(int(str(Binario),2))))
elif opcion ==2:
  print('El numero {} en el convertidor para octal es igual a {}'.format(Binario, oct(Binario)))
elif opcion ==3:
  print('El numero {} en el convertidor para Hexagecimal es igual a {}'.format(Binario, hex(Binario)))
else: 
  print('opcion invalida, intente nuevamente.')
Numero=(input('Digite un numero para su conversion: '))
print(''' Convertir a binario:
[1] convertir de Decimal a binario
[2] convertir de Octal a binario
[3] convertir de Hexagecimal a binario''')

conversion =int(input('Opcion:'))
if conversion ==1:
   print('El numero {} en el convertidor de decimal a binario es igual a {}'.format(Numero,(int(bin(int(Numero))[2:]))))
elif conversion ==2:
  print('El numero {} en el convertidor de octal a binario es igual a {}'.format(Numero,(int(bin(int(Numero, 8))[2:]))))
elif conversion ==3:
  print('El numero {} en el convertidor de Hexagecimal a Binario es igual a {}'.format(Numero,(int(bin(int(Numero , 16))[2:]))))
else: 
  print('opcion invalida, intente nuevamente.')

  
  