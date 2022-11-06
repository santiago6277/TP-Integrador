import json


def agregar_expediente(datos_nuevos):
    """
    Guarda los datos de un nuevo expediente en el archivo de expedientes.json
    """
    with open('files/expedientes.json', 'r') as archivo:
        lista_expedientes = json.load(archivo)
    if not lista_expedientes:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_expedientes, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_expedientes.append(datos_nuevos)
    with open('files/expedientes.json', 'w') as archivo:
        json.dump(lista_expedientes, archivo, indent=4)


def leer_archivo():
    """
    Lee todos los datos de expedientes.json y los devuelve como una lista de diccionarios
    """
    with open('files/expedientes.json', 'r') as file: 
        datos = json.load(file)
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([ dato["-EX-"], dato["-Ano-"], dato["-Numero-"], dato["-GDEBA-"], dato["-Reparticion-"]])
    return datos_para_tabla

