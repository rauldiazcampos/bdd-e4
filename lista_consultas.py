from clases import *

#Consulta("/").ids_disponibles()

consulta = ListaConsultas(0, "/", "https://iic2413-2020-1-api.herokuapp.com", "http://localhost:5000")
# Consulta.ids = consulta.ids_disponible()
# if not Consulta.ids:
#     Consulta.ids = list(range(1, 221))
# print(Consulta.ids
import os
if not os.path.exists('grupo1'):
    os.makedirs('grupo1')
Consulta.nombre_archivo = "grupo1"
consulta.cargar()
consulta.correr()
consulta.guardar()
