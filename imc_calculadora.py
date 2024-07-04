#  Aqui se piden datos personales básicos es importante rellenarlos de lo contrario no permitira seguir
# se agrego .isalpha e .isspace para no recibir datos numericos o espacios en blanco
nombre = input('Ingresa tu nombre: ')
while not nombre.isalpha():
    nombre = input('Ingresa tu nombre: ')
while nombre.isspace():
    nombre = input('Ingresa tu nombre: ')

ap = input('Ingresa tu apellido paterno: ')
while not ap.isalpha():
    ap = input('Ingresa tu apellido paterno: ')
while Ap.isspace():
    ap = input('Ingresa tu apellido paterno: ')

am = input('Ingresa tu apellido materno: ')
while not am.isalpha():
    am = input('Ingresa tu apellido materno: ')
while am.isspace():
    am = input('Ingresa tu apellido materno: ')

edad = (input('dime tu edad: '))
while not edad.isdigit():
    edad = input('dime tu edad: ')
while edad.isspace():
    edad = input('dime tu edad: ')

# se permiten datos con decimales por eso esta el float por si la persona quiere resultado exacto
peso = float(input('dime tu peso: '))
while peso <= 0:
    peso = float(input('dime tu peso: '))
# se permiten datos con decimales por eso esta el float por si la persona quiere resultado exacto
est = float(input('dime tu est: '))
while est <= 0:
  est = float(input('dime tu est: '))
while est > 2.50:
  est = float(input('dime tu est: '))

# si los anteriores datos se responden correctamente, entonces se calcula el IMC
# se agrego round para redondear el resultado a dos decimales
else:
    print('Tu IMC es de', round(peso/(est**2),2), "es decir" , end =" ")

# de acuerdo al resultado anterior se segmenta de acuerdo a la fuente ISSSTE

IMC = peso/(est**2)

if IMC < 18.9:
    print(' tienes peso bajo')

elif IMC >= 18.9 and IMC <= 24.9:
    print('tienes peso normal')
elif IMC >= 25.0 and IMC <= 29.9:
    print('tienes sobrepeso')

elif IMC >= 30.0 and IMC <= 34.9:
    print('tienes obesidad leve')
elif IMC >= 35.0 and IMC <= 39.9:
    print('tienes obesidad media')

else:
    print('tienes obesidad morbida')
    
print('Fin del programa')
#----