from clases import *
from datetime import datetime

#Consulta("/").ids_disponibles()
def listo(archivo):
    consulta = ListaConsultas(0, "/", "https://iic2413-2020-1-api.herokuapp.com", "http://localhost:5000")
    # Consulta.ids = consulta.ids_disponible()
    # if not Consulta.ids:
    #     Consulta.ids = list(range(1, 221))
    # print(Consulta.ids
    import os
    if not os.path.exists(archivo):
        os.makedirs(archivo)
    ahora = datetime.now()
    a = archivo + '/' + ahora.strftime("%d-%m-%y %H-%M-%S")
    if not os.path.exists(a):
        os.makedirs(a)
    Consulta.nombre_archivo = archivo + '/' + ahora.strftime("%d-%m-%y %H-%M-%S")
    consulta.cargar()
    consulta.correr()
    consulta.guardar(ahora=ahora)
