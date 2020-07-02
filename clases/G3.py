from clases.Consulta import *

class G3(Consulta):
    def __init__(self, nombre, busqueda=None, ruta="/text-search"):
        Consulta.__init__(self, ruta)
        #if id is None:
        #    self.esperar = Truye
        self.busqueda = busqueda
        self.done = False
        self.nombre = nombre
        self.json_api = None
        self.json_grupo_original = None
        self.json_grupo_adaptado = None

    def escribir(self, nombre_archivo="G3.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            with open(nombre_carpeta + f"/{nombre_archivo}", "a") as archivo:# + datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
                #""#bcb
                string = f'''
{"#"*((80-len(self.nombre) - 2)//2)} {self.nombre} {"#"*(80 - len(self.nombre) - 2 - ((80-len(self.nombre) - 2)//2))}
"{self.nombre}": {'{'}
    "busqueda": {self.busqueda},
    "respuesta": {self.respuesta},
    "todos_los_atributos": {self.atributos},
    "atributos_encontrados": {self.atributos_encontrados},
    "json_grupo_adaptado": {self.json_grupo_adaptado if self.json_grupo_adaptado in [None, False] else [int(float(i["mid"])) for i in self.json_grupo_adaptado if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},
    "json_api": {self.json_api if self.json_api in [None, False] else [int(float(i["mid"])) for i in self.json_api if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},

    "json_grupo_original": {self.json_grupo_original},

{'},'}
                '''
                archivo.write(string)#r

    def correr(self):
        try:

            cargando = threading.Thread(target=self.animate)
            cargando.start()

            resultado = self._correr()
            self.respuesta = resultado
            self.done = True#jiib.strip()
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{', '.join([i for i in self.busqueda]) if self.busqueda else self.busqueda}]   ")
            print()
        except SeDemora:
            #print("hola")
            self.done = True
            resultado = False
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{self.busqueda}]   ")
            print()
        except (KeyboardInterrupt, SystemExit):
            self.done = True
            cargando.clear()

        return resultado


    def _correr(self):
        try:
            #https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-runningd

            if self.busqueda == None or self.busqueda == {}:
                consulta = f"{self.ruta}"
                if self.busqueda is None:
                    uno = Consulta.requests_get(self.api + consulta, timeout=10)
                else:
                    uno = Consulta.requests_get(self.api + consulta, json=self.busqueda, timeout=10)
                respuesta_api = Consulta.encontrar(uno.json())
                self.json_api = respuesta_api
                if self.busqueda is None:
                    dos = Consulta.requests_get(self.grupo + consulta, timeout=10)
                else:
                    dos = Consulta.requests_get(self.grupo + consulta, json=self.busqueda, timeout=10)
                self.json_grupo_original = dos.json()
                respuesta_grupo = Consulta.encontrar(self.json_grupo_original)
                self.json_grupo_adaptado = respuesta_grupo
                if not respuesta_api and not respuesta_grupo:
                    return True
                elif respuesta_api and not respuesta_grupo:
                    return False
                elif not respuesta_api and respuesta_grupo:
                    return False
                else:
                    self.todos_atributos(respuesta_grupo)
                    largo = len(respuesta_grupo)
                    contador = 0
                    for i in range(len(respuesta_grupo)):
                        if str(respuesta_grupo[i]["mid"]).replace(".", "").isnumeric() and 1 <= int(str(respuesta_grupo[i]["mid"]).replace(".", "")) <= 220:
                            contador += 1
                    if contador >= 100:
                        return True
                    if largo >= 2:
                        return True
                    return False


            else:
                consulta = f"{self.ruta}"
                uno = Consulta.requests_get(self.api + consulta, json=self.busqueda)
                respuesta_api = Consulta.encontrar(uno.json())
                self.json_api = respuesta_api
                dos = Consulta.requests_get(self.grupo + consulta, json=self.busqueda)
                self.json_grupo_original = dos.json()
                respuesta_grupo = Consulta.encontrar(self.json_grupo_original)
                self.json_grupo_adaptado = respuesta_grupo
                if not respuesta_api and not respuesta_grupo:
                    return True
                elif respuesta_api and not respuesta_grupo:
                    return False
                elif not respuesta_api and respuesta_grupo:
                    return False
                else:
                    ids_encontrados = set([int(i["mid"]) for i in respuesta_api])
                    self.todos_atributos(respuesta_grupo)
                    ids = set()
                    for elemento in respuesta_grupo:
                        mid = elemento.get("mid")
                        if str(mid).replace(".", "").isnumeric():
                            mid = int(float(str(mid)))
                            if mid in Consulta.ids:
                                if mid not in ids_encontrados:
                                    return False
                                else:
                                    ids.add(mid)
                    largo = len((ids_encontrados - ids).intersection(Consulta.ids))
                    #print(largo)
                    if largo >= 1:
                        return False #if i in
                    return True#tYu#tRUE#FalsetRUE
        except requests.exceptions.ReadTimeout:
            self.done = True
            sys.stdout.write(f"\r¿Listo? {self.nombre}")
            print()
            print("    " + "_"*48)
            print("    Al parecer algo sucede con las consultas que ")
            print("    entregan todos los mensajes                  ")
            print("    A continuación se dan distintas opciones     ")
            print("    para resolver, resolverlo ahora o más tarde: ")
            print('''
    [0] Revisar código ahora -> Está correcto
    [1] Revisar código ahora -> Está incorrecto
    [2] Revisar código más tarde
            ''')
            entrada = input("    >> ")
            while entrada.strip() not in ["0", "1", "2"]:
                print("    No se reconoció la entrada")
                entrada = input("    >> ")
            print("    " + "_"*48)
            if entrada.strip() == "0":
                resultado = True#ye#TTTT
                return True
            elif entrada.strip() == "1":
                resultado = False
                return False
            else:
                resultado = None
                return None

        except Exception as e:
            print(e)
            self.done = True
            return False
