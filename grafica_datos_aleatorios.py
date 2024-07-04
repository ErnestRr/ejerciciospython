#Será la simulación de una máquina de Galton de 3000 canicas. 
#En total tendrá 12 niveles de obstáculos 
#El resultado final será un histograma que represente la cantidad de canicas en cada contenedor\
# como el siguiente -No olvides colocar nombre a los ejes y un título al gráfico. 
#Deberás emplear dos funciones, una para calcular los resultados de las canicas y la \
# segunda para la graficación del histograma. 

import numpy as np
import matplotlib.pyplot as plt
from random import randint

# se definen las funciones: las dos primeras generan la distribución de las canicas en una iteración 
# de 12 niveles dando como resultado contenedores con 3000 canicas
# la última función pretende generar la gráfica de histograma a traves de 3 variables: valores del 
# eje X número de barras y color


def random(n):
    x= np.random.randint(0,2,(cont,n))
    return(x)
"""Función que calcula la distribución de las canicas asignadas para cada nivel"""

def pos(niveles):
    posicion=np.cumsum(niveles,axis=0)
    return(posicion)
"""Función que calcula la posición de las canicas """

def graficar(pasos):
    plt.hist(pasos[-1],color='red')
    plt.suptitle('Simulación tablero de Galton')
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.show()
"""Función que grafica las canicas contenidas en los 12 niveles"""

n=3000
niveles =12
cont =1

for i in range(niveles):
    dir = int(input('Asigna la dirección de las canicas: izquierda>--(2), derecha>--(1): '))
    
    if dir == 2:
        niveles = random(n) * 2
        pos(niveles) 
        cont +=1       

    elif dir == 1:
        niveles = random(n) * 1 
        pos(niveles)
        cont +=1

    print(pos(niveles))
graficar(pos(niveles))
        
#-----------