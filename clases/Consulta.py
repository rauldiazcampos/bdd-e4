import requests
import itertools
import threading
import time
import sys
from datetime import datetime


class SeDemora(Exception):
    def __init__(self, texto=""):
        super().__init__(texto)

class Consulta:

    diccionario = ["mid", "message", "sender", "receptant", "lat", "long", "date"]
    ids = set(list(range(1, 221)))
    diccionario_usuarios = ["uid", "name", "age", "description"]
    guarda, nombre_archivo = True, ""

    def __init__(self, ruta, api="https://iic2413-2020-1-api.herokuapp.com", grupo="http://localhost:5000"):
        self.ruta = ruta
        self.api = api
        self.grupo = grupo
        self.llaves = []
        self.g1 = []
        self.esperar = False
        self.inicio = None
        self.atributos = True
        self.atributos_encontrados = []
        self.estado = None
        self.json_grupo = None
        self.json_api = None
        self.json_grupo_adaptado = None
        self.json_grupo_original = None
        self._mensaje = ""

    def mensaje(self):
        if not self.atributos:
            self._mensaje = "Faltan atributos por mostrar"
        if self.respuesta:
            return f"{self.nombre}: {self.respuesta} {self._mensaje}"
        else:
            return f"{self.nombre}: {self.respuesta} {self._mensaje}"#"

    def encontrar(respuesta, llaves=None, filtro=4):
        primero = False
        if llaves is None:
            llaves = []
            primero = True
        if type(respuesta) == dict:
            #print("es diccionario")
            contador = 0
            for i in ["mid", "sender", "receptant", "date", "lat", "long", "message"]:
                if i in respuesta:
                    contador += 1
            if contador >= filtro:
                #print("mayor o igual a 4")
                if len(llaves) >= 1:
                    #print(":")
                    #print(respuesta, llaves)
                    if type(llaves[-1]) == int or str(llaves[-1]).isnumeric():
                        llaves.pop(len(llaves)-1)

                if primero:
                    #print("primero")
                    return Consulta.obtener(respuesta, llaves, filtro)
                else:
                    #print("else")
                    return llaves
            retorno = False
            for key in respuesta:
                retorno = Consulta.encontrar(respuesta[key], llaves.copy() + [key], filtro)

                if retorno is not False:
                    if primero:
                        return Consulta.obtener(respuesta, retorno, filtro)
                    else:
                        return retorno
        elif type(respuesta) == list:
            retorno = 0
            for key in range(len(respuesta)):
                retorno = Consulta.encontrar(respuesta[key], llaves.copy() + [key], filtro)
                #print("retorno para", key, ":", retorno, "donde respuesta[key] = ", respuesta[key])
                if retorno is not False:
                    #print("hola")
                    if primero:
                        #print("es primero")
                        return Consulta.obtener(respuesta, retorno, filtro)
                    else:
                        #print("no es primero")
                        return retorno
        if primero and filtro != 1:
            return Consulta.encontrar(respuesta, None, 1)
        return False


    def encontrar_2(respuesta, llaves=None, filtro=2):
        primero = False
        if llaves is None:
            llaves = []
            primero = True
        if type(respuesta) == dict:
            #print("es diccionario")
            contador = 0
            for i in ["uid", "name", "age", "description"]:
                if i in respuesta:
                    contador += 1
            if contador >= filtro:
                #print("mayor o igual a 4")
                if len(llaves) >= 1:
                    #print(":")
                    #print(respuesta, llaves)
                    if type(llaves[-1]) == int or str(llaves[-1]).isnumeric():
                        llaves.pop(len(llaves)-1)

                if primero:
                    #print("primero")
                    return Consulta.obtener_2(respuesta, llaves, filtro)
                else:
                    #print("else")
                    return llaves
            retorno = False
            for key in respuesta:
                retorno = Consulta.encontrar_2(respuesta[key], llaves.copy() + [key], filtro)

                if retorno is not False:
                    if primero:
                        return Consulta.obtener_2(respuesta, retorno, filtro)
                    else:
                        return retorno
        elif type(respuesta) == list:
            retorno = 0
            for key in range(len(respuesta)):
                retorno = Consulta.encontrar_2(respuesta[key], llaves.copy() + [key], filtro)
                #print("retorno para", key, ":", retorno, "donde respuesta[key] = ", respuesta[key])
                if retorno is not False:
                    #print("hola")
                    if primero:
                        #print("es primero")
                        return Consulta.obtener_2(respuesta, retorno, filtro)
                    else:
                        #print("no es primero")
                        return retorno
        if primero and filtro != 1:
            return Consulta.encontrar_2(respuesta, None, 1)
        return False


    def obtener_2(respuesta, ruta, filtro=2):
        #print(respuesta, ruta)
        for i in range(len(ruta)):
            respuesta = respuesta[ruta[i]]
            if i == len(ruta) - 2:
                super_contador = 0
                for key in respuesta:
                    contador = 0
                    for llave in ["uid", "name", "description", "age"]:
                        if llave in respuesta[key]:
                            contador += 1
                    if contador >= filtro:
                        super_contador += 1
                if super_contador == len(respuesta):
                    return list(respuesta.values())
        if type(respuesta) != list:
            return [respuesta]
        return respuesta



    def obtener(respuesta, ruta, filtro=4):
        #print(respuesta, ruta)
        for i in range(len(ruta)):
            respuesta = respuesta[ruta[i]]
            if i == len(ruta) - 2:
                super_contador = 0
                for key in respuesta:
                    contador = 0
                    for llave in ["mid", "sender", "receptant", "date", "lat", "long", "message"]:
                        if llave in respuesta[key]:
                            contador += 1
                    if contador >= filtro:
                        super_contador += 1
                if super_contador == len(respuesta):
                    return list(respuesta.values())
        if type(respuesta) != list:
            return [respuesta]
        return respuesta

    def animate(self):
        iconos2 = ['|', '/', '-', '\\']
        iconos = ['.', '..', '...', '..']
        datetime.now()
        for c in itertools.cycle(iconos2):
            if self.done:
                break
            if self.inicio:
                holi = (datetime.now() - self.inicio).seconds
                if holi >= 0:
                    self.done = True
                    raise SeDemora("holi")


            sys.stdout.write('\rCargando ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        #sys.stdout.write('\r¡Listo!     ')

    def todos_atributos(self, consulta):
        atributos = [i.strip().lower() for i in consulta[0]]
        encontrados = True
        for i in Consulta.diccionario:
            if i.strip().lower() not in atributos:
                encontrados = False
        self.atributos = encontrados # True o False
        self.atributos_encontrados = atributos # Lista
        return encontrados

    def todos_atributos_2(self, consulta):
        atributos = [i.strip().lower() for i in consulta[0]]
        encontrados = True
        for i in Consulta.diccionario_usuarios:
            if i.strip().lower() not in atributos:
                encontrados = False
        self.atributos = encontrados
        self.atributos_encontrados = atributos
        return encontrados

    def requests_get(*args, **kwargs):
        for i in range(10):
            a = requests.get(*args, **kwargs)
            if a.status_code != 503:
                return a
                break
            time.sleep(1)
            #GET
        return a

    def requests_delete(*args, **kwargs):
        for i in range(10):
            a = requests.delete(*args, **kwargs)
            if a.status_code != 503:
                return a
                break
            time.sleep(1)
        return a

    def requests_post(*args, **kwargs):
        for i in range(10):
            a = requests.post(*args, **kwargs)
            if a.status_code != 503:
                return a
                break
            time.sleep(1)
        return a

    def ids_disponibles(self):
        try:
            recibido = Consulta.requests_get(self.grupo + "/messages", timeout=10)
            recibido = Consulta.encontrar(recibido.json())
            lista = [int(i["mid"]) if str(i).isnumeric() else (int(float(str(i["mid"])))) for i in recibido if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]
            Consulta.ids = set(lista)
        except requests.exceptions.ReadTimeout:
            print("Al parecer /messages está teniendo problemas par obtener todos los mensajes")
            print("¿Desea utilizar el predeterminado? (ids del 1 al 220)? ¿O mejor obtener los mensajes haciendo consulta id por id?")
            print("    [0] Asumir que las ids van de 1 al 220")
            print("    [1] Obtener id por id (esto puede tardar unos minutos)")
            entrada = input(">> ")
            while entrada.strip() not in ["0", "1"]:
                print("No se reconoció el comando :O ¡Puede intentarlo de nuevo!")
                entrada = input(">> ")
            if entrada == "0":
                return Consulta.ids
            lista = []
            for i in range(1, 221):
                try:
                    sys.stdout.write(f"\r [{'*'*int(i*50/220)}{' '*(50-int((i)*50/220))}] ({i}/220)")
                    sys.stdout.flush()
                    recibido = Consulta.requests_get(self.grupo + "/messages/" + str(i))
                    recibido = Consulta.encontrar(recibido.json())
                    lista.append(recibido[0]["mid"] if str(recibido[0]["mid"]).isnumeric() else (int(float(str(recibido[0]["mid"])))))
                except:
                    continue
            Consulta.ids = set(lista)
        return Consulta.ids


#consulta = Consulta("/messages", "https://iic2413-2020-1-api.herokuapp.com", "localhost:5000")
#consulta.cargar_g1()
#consulta.correr_g1()
