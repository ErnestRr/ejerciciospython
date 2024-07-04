#Construye una pokédex, obteniendo datos de https://pokeapi.co/
#Cuando el usuario introduzca el nombre de un Pokémon, si no existe que le mande un mensaje de error; 
# si existe, que muestre una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos). 
#Posteriormente, guardarás toda la información del pokémon (junto con el link de la imagen frontal del 
# pokémon) en un archivo .json dentro de una carpeta llamada “pokedex”.

#el programa se divide en 3 partes: 

#1) abarca el llamado de las bibliotecas requeridas para el funcionamiento del programa la conexión a la api 
# y la validación de un posible error (400 o similares) que pudieran cerrar el programa, siempre buscando 
# obtener el código 200.
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import os
pokemon = input('dime un pokemon: ')
url = 'https://pokeapi.co/api/v2/pokemon/'+ pokemon
respuesta = requests.get(url)
if respuesta.status_code !=200:
    print('pokemon no encontrado')
    exit()

# 2) en el consumo de la API se lleva a cabo la obtención de los datos específicos de un jason del respetivo pokémon.
datos = respuesta.json()
nombre = datos ['name']
peso = datos ['weight']
tamaño = datos ['height']
mov = datos ['moves'][0]['move']['name']
habil= datos ['abilities'][0]['ability']['name']
types = datos ['types'][0]['type']['name']
url_imagen = datos ['sprites']['front_default']
plt.title(respuesta.json()['name'])

try:
    os.makedirs('C:\\pokedex_')
    datos = {'nombre':nombre,'peso':peso,'tamaño':tamaño,'mov':mov,'habilidades':habil,'tipos':types,'imagen':url_imagen}
except FileExistsError:

    with open ('C:\\pokedex_\poke.json','w') as archivo:
        json.dump(datos, archivo)
    with open ('C:\\pokedex_\poke.json','r') as archivo:
        data = json.load(archivo)

#3) finalmente se muestra la imagen y los valores de acuerdo a la requisición, así como el proceso de 
# guardar los datos en un archivo jason.

imagen = Image.open(urlopen(url_imagen))
imgplot =  plt.imshow(imagen)
plt.show()

print(f'Su peso: {peso}')
print(f'Su tamaño: {tamaño}')
print(f'movimientos: {mov}')
print(f'habil: {habil}')
print(f'tipo: {types}')
#----