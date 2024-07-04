"""
Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta \
debe tener entre cuatro y ocho letras:
    -Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir\
    un mensaje que indique que la palabra es correcta 
    -Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. \
    Solo tiene N letras (siendo N el número de letras de la palabra)
    -
    Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. \
    Tiene N letras ((siendo N el número de letras de la palabra))
"""
#se requiere una palabra para examinar su rango
palabra = input('escribe una palabra: ')
n = (len( palabra ))

#se generan condicionales para determinar los digitos que incluye con 3 opciones disponibles
if n in range(4,9):
    print('la palabra es correcta')
elif n <4:
    print(f'hacen falta letras, sólo tiene {n}')
elif n > 8:
    print(f'sobran letras, tiene {n}')
###################################################################################################
"""
Crear un programa que en base a 2 números de entrada, coordenadas, identifique en cuál de los 4 \
cuadrantes se encuentra el punto. El programa debe verificar que ninguna coordenada sea 0.
"""
#este programa pretende poner en práctica el uso de listas, diccionarios o tuplas y condicionales
# para obtener el punto en el cual tendría que esta el punto a graficar con 5 posibles opciones
x = int(input('ingresa el valor x: '))
y = int(input('ingresa el valor y: '))
coordenadas = (x,y)
if x ==0 and y==0:
    print(f'{coordenadas} = sin coordenadas!!!')
if x>0 and y>0:
    print(f'Cuadrante I \n {coordenadas} = (+,+) ')
if x<0 and y>0:
    print(f'Cuadrante II \n {coordenadas} = (-,+) ')
if x<0 and y<0:
    print(f'Cuadrante III \n {coordenadas} = (-,-) ')
if x>0 and y<0:
    print(f'Cuadrante IV \n {coordenadas} = (+,-) ')
#----