# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import os
import logging
from os.path import exists
from time import strftime, gmtime

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def descargar_datos():
    # Obtener los 3 archivos de fuente utilizando la libreria
    # requests y almacenarse de forma local
    # Las Urls pueden cambiar en un futuro

    # Necesito las Urls,hacer un request para cada una y almacenarla
    # En objetos request, luego llamo json() y de json() lo pasaré a csv

    # Descargar Datos Argentina Museos
    url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7' \
                 '-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv '

    # Creando la ruta y el nombre de archivo del csv
    categoria = "museos"
    archivo_museos = crear_archivo(categoria)
    # Descargando los datos en el archivo
    cargar_a_archivo(archivo_museos, url_museos)
    # Descargar Datos Argentina Salas de Cine
    url_cines = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11' \
                '-4776-b280-6f1c7fae16ae/download/cine.csv '
    categoria = "cines"
    archivo_cines = crear_archivo(categoria)
    cargar_a_archivo(archivo_cines, url_cines)
    # Descargar Datos Argentina Bibliotecas Populares
    url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048' \
                      '-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv '
    categoria = "bibliotecas"
    archivo_bibliotecas = crear_archivo(categoria)
    cargar_a_archivo(archivo_bibliotecas, url_bibliotecas)


def cargar_a_archivo(archivo, url):
    with requests.get(url, stream=True) as datos_argentina_categoria:
        lines = (line.decode('utf-8') for line in datos_argentina_categoria.iter_lines())
        for row in csv.reader(lines):
            spamwriter = csv.writer(archivo, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(row)


def crear_archivo(categoria):
    # Crea la ruta con el formato especificado en el pdf y luego crea el archivo
    ruta_archivo = "{}/".format(categoria) + strftime("%Y-%B", gmtime()) + "/"
    nombre_archivo = ruta_archivo + "{categoria}-{date}.csv".format(categoria=categoria, date=strftime("%d-%m-%Y"))
    logging.info("Creando archivo %s", nombre_archivo)
    print(nombre_archivo)
    os.makedirs(ruta_archivo, exist_ok=True)
    print(os.getcwd())
    existe = exists(nombre_archivo)
    if existe:
        os.remove(nombre_archivo)
    archivo = open(nombre_archivo, "w")
    return archivo


def iniciar_log():
    #Configuraciones basicas del log
    logging.basicConfig(filename='Registro.log', encoding='utf-8', level=logging.DEBUG)
    logging.info("Iniciando proceso")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    iniciar_log()
    descargar_datos()

    # TODO agregar funcionalidad de logging

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
