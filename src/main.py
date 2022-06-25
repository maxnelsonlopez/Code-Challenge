# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import os
import logging
import pandas as pd
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
    logging.info("Funcion descargar_datos")
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
    # Esta funcion descarga los datos de la url y los guarda en un archivo csv
    logging.info("Cargando datos al csv")
    logging.info(archivo)
    with requests.get(url, stream=True) as datos_argentina_categoria:
        lines = (line.decode('utf-8') for line in datos_argentina_categoria.iter_lines())
        for row in csv.reader(lines):
            spamwriter = csv.writer(archivo, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(row)


def crear_archivo(categoria):
    # Crea la ruta con el formato especificado en el pdf y luego crea el archivo
    nombre_archivo, ruta_archivo = generar_nombre_archivo(categoria)
    logging.info("Creando archivo %s", nombre_archivo)
    # print(nombre_archivo)
    os.makedirs(ruta_archivo, exist_ok=True)
    # print(os.getcwd())
    existe = exists(nombre_archivo)
    if existe:
        os.remove(nombre_archivo)
    archivo = open(nombre_archivo, "w")
    return archivo


def generar_nombre_archivo(categoria):
    # Genera la ruta y el nombre del archivo segun la categoria
    ruta_archivo = "{}/".format(categoria) + strftime("%Y-%B", gmtime()) + "/"
    nombre_archivo = ruta_archivo + "{categoria}-{date}.csv".format(categoria=categoria, date=strftime("%d-%m-%Y"))
    return nombre_archivo, ruta_archivo


def iniciar_log():
    # Configuraciones basicas del log
    logging.basicConfig(filename='Registro.log', encoding='utf-8', level=logging.DEBUG)
    logging.info("Iniciando proceso")


def normalizar_datos():
    # Funcion para cargar los .csv en data frames de pandas
    logging.info("Normalizacion de datos")
    nombre_museos, museos_ruta = generar_nombre_archivo("museos")
    cines_csv, cines_ruta = generar_nombre_archivo("cines")
    bibliotecas_csv, bibliotecas_ruta = generar_nombre_archivo("bibliotecas")
    print(museos_csv)

    csv_a_pandas(nombre_museos)


def csv_a_pandas(nombre_museos):
    """
    Retorna un dataframe a partir de la ruta a un archivo csv

            parametros:
                    nombre_museos (string): The path to the archive
            :return: data_frame (pandas.DataFrame)
    :type nombre_museos: csv file
    """
    museos_csv = open(nombre_museos)
    # use the first 2 lines of the file to detect separator
    temp_lines = museos_csv.readline() + '\n' + museos_csv.readline()
    dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')
    # remember to go back to the start of the file for the next time it's read
    museos_csv.seek(0)
    data_frame = pd.read_csv(museos_csv, sep=dialect.delimiter)
    data_frame.fillna(pd.NA, inplace=True)
    
    return data_frame

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    iniciar_log()
    # descargar_datos()
    normalizar_datos()
    # TODO agregar funcionalidad de logging

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
