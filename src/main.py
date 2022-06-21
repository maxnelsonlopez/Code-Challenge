# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def descargar_datos():
    #Obtener los 3 archivos de fuente utilizando la libreria
    #requests y almacenarse de forma local
    #Las Urls pueden cambiar en un futuro

    #Necesito las Urls,hacer un request para cada una y almacenarla
    #En objetos request, luego llamo json() y de json() lo pasaré a csv

    #Datos Argentina Museos
    datos_argentina_museos = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/archivo/4207def0-2ff7-41d5-9095-d42ae8207a5d')
    print(datos_argentina_museos.headers)
    #museos_json = datos_argentina_museos.json()
    #print(museos_json)
    #Datos Argentina Salas de Cine
    #Datos Argentina Bibliotecas Populares

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    descargar_datos()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
