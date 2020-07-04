import sys
import requests
import valores
import clases

def obtener_argumentos():
    '''
    Obtiene los parámetros dados en consola,
    dejando algunos como valor predeterminado
    si no son especificados
    '''
    grupo = None
    enlace = None
    archivo = None
    numero_grupo = None

    argumentos = sys.argv
    if len(argumentos) >= 2:
        grupo = argumentos[1]
        if "grupo" in grupo:
            if grupo.replace("grupo", "").isnumeric():
                numero_grupo = int(grupo.replace("grupo", ""))
            else:
                grupo = None
        elif grupo.isnumeric():
            numero_grupo = int(grupo)
            grupo = "grupo" + grupo
        else:
            grupo = None
    if len(argumentos) >= 3:
        if ":" in argumentos[2]:
            enlace = argumentos[2]
            if len(argumentos) >= 4:
                archivo = argumentos[3]
        else:
            archivo = argumentos[2]

    if enlace is None:
        enlace = (valores.group_host + ":" + str(valores.group_port)
            if valores.group_port else valores.group_host)
    if archivo is None and grupo is not None:
        archivo = valores.group_file.replace("%numero", str(numero_grupo))

    obtenidos = [grupo, enlace, archivo, numero_grupo]
    return obtenidos

obtenidos = obtener_argumentos()
grupo, enlace, archivo, numero_grupo = obtenidos
print("¡Hola! Bienvenide a corregir_e4.py")
if None in obtenidos:
    print("A continuación puede especificar el grupo a revisar :D")
    while grupo is None:
        grupo = input("> grupo = ")
        if "grupo" in grupo:
            if grupo.replace("grupo", "").isnumeric():
                numero_grupo = int(grupo.replace("grupo", ""))
            else:
                grupo = None
        elif grupo.isnumeric():
            numero_grupo = int(grupo)
            grupo = "grupo" + grupo
        else:
            grupo = None
            print("Grupo o número de grupo no válidos :O")
        if grupo is not None:
            archivo = valores.group_file.replace("%numero", str(numero_grupo))

import lista_consultas
lista_consultas.listo(archivo)
# r = requests.get('https://iic2413-2020-1-api.herokuapp.com/text-search', json={"desired": "P NP"})
# print(r.json())
